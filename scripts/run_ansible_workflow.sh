#!/bin/bash

try_ansible_play() {
  # Default action
  return 0
}

set -euo pipefail

# Colors
BOLD='\033[1m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
RESET='\033[0m'

# Defaults
PLAYBOOK="${1:-main_workflow.yml}"
TAGS="${2:-}"
EXTRA_VARS="${3:-}"
DRY_RUN="${DRY_RUN:-false}"

# Directories
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
ANSIBLE_DIR="$PROJECT_ROOT/ansible"
OUTPUT_DIR="$PROJECT_ROOT/output"

echo -e "${BOLD}${GREEN}=== VIDWAAN AI ANSIBLE WORKFLOW ===${RESET}"
echo "Playbook: $PLAYBOOK"
echo "Tags: ${TAGS:-none}"
echo "Extra Vars: ${EXTRA_VARS:-none}"
echo -e "${RESET}"

# Create output directory
mkdir -p "$OUTPUT_DIR/logs" "$OUTPUT_DIR/reports"

# Ensure Ansible uses the correct config and context
export ANSIBLE_CONFIG="$ANSIBLE_DIR/ansible.cfg"
cd "$ANSIBLE_DIR"

# Build ansible-playbook command
ANSIBLE_CMD="uv run ansible-playbook"
ANSIBLE_CMD="$ANSIBLE_CMD -i $ANSIBLE_DIR/inventory/hosts.yml"
ANSIBLE_CMD="$ANSIBLE_CMD $ANSIBLE_DIR/playbooks/$PLAYBOOK"

# Add tags if provided
if [ -n "$TAGS" ]; then
    ANSIBLE_CMD="$ANSIBLE_CMD --tags $TAGS"
fi

# Add extra vars if provided
if [ -n "$EXTRA_VARS" ]; then
    ANSIBLE_CMD="$ANSIBLE_CMD -e $EXTRA_VARS"
fi

# Add verbose flag
ANSIBLE_CMD="$ANSIBLE_CMD -v"

# Add dry-run if requested
if [ "$DRY_RUN" = "true" ]; then
    ANSIBLE_CMD="$ANSIBLE_CMD --check"
    echo -e "${YELLOW}DRY RUN MODE${RESET}"
fi

echo -e "${YELLOW}Executing: $ANSIBLE_CMD${RESET}"
echo ""

# Execute playbook
if eval "$ANSIBLE_CMD"; then
    echo -e "${GREEN}✓ Workflow completed successfully!${RESET}"
    echo "Logs available in: $OUTPUT_DIR/logs"
    echo "Reports available in: $OUTPUT_DIR/reports"
else
    echo -e "${RED}✗ Workflow failed!${RESET}"
    echo "Check logs in: $OUTPUT_DIR/logs"
    exit 1
fi
