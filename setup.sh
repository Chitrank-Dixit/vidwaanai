#!/bin/bash
# This script guides you through the initial, fully containerized setup of the VidwaanAI project.

set -e

# --- Configuration ---
COMPOSE_FILE="docker-compose-full.yml"
APP_SERVICE="app"
DB_SERVICE="db"

# --- Helper Functions ---
function print_info {
    echo -e "\033[36m[INFO]\033[0m $1"
}

function print_success {
    echo -e "\033[32m[SUCCESS]\033[0m $1"
}

function print_warning {
    echo -e "\033[33m[WARNING]\033[0m $1"
}

function print_error {
    echo -e "\033[31m[ERROR]\033[0m $1"
    exit 1
}

# --- Prerequisites Check ---
print_info "Checking for prerequisites: Docker and Docker Compose..."

if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install it to proceed."
fi

if ! docker info &> /dev/null; then
    print_error "Docker daemon is not running. Please start Docker and try again."
fi

print_success "Docker is available."

# --- Step 1: Configure Environment ---
if [ ! -f .env ]; then
    print_info "Creating .env file from .env.example..."
    cp .env.example .env
    print_warning "Please review and edit the .env file with your API keys (e.g., OPENAI_API_KEY)."
    print_warning "The setup will continue, but some features may not work without API keys."
else
    print_info ".env file already exists."
fi

# --- Step 2: Build and Start Docker Services ---
print_info "Building and starting Docker services from '$COMPOSE_FILE'..."
docker-compose -f "$COMPOSE_FILE" up --build -d
print_success "All services are starting up in the background."

# --- Step 3: Wait for Database ---
print_info "Waiting for the database service ('$DB_SERVICE') to be healthy..."
max_retries=30
for i in $(seq 1 $max_retries); do
    health_status=$(docker-compose -f "$COMPOSE_FILE" ps "$DB_SERVICE" | grep 'healthy')
    if [ -n "$health_status" ]; then
        print_success "Database is healthy and ready!"
        break
    fi
    if [ $i -eq $max_retries ]; then
        print_error "Database did not become healthy in time. Check 'docker-compose logs db'."
    fi
    sleep 2
done

# --- Step 4: Initialize Database and Load Data ---
print_info "Running first-time setup scripts inside the app container..."

print_info "(1/2) Initializing database schema..."
docker-compose -f "$COMPOSE_FILE" exec "$APP_SERVICE" uv run python scripts/setup_db.py
print_success "Database schema initialized."

print_info "(2/2) Loading sample data..."
docker-compose -f "$COMPOSE_FILE" exec "$APP_SERVICE" uv run python scripts/load_sample_data.py
print_success "Sample data loaded."


# --- Final Message ---
echo
print_success "VidwaanAI Docker setup is complete!"
echo
print_info "You can now interact with the application using 'make -f Makefile-docker <command>'."
print_info "For example, to run a query:"
echo "  make -f Makefile-docker query Q=\"What is dharma?\""
echo
print_info "To open a shell inside the running app container:"
echo "  make -f Makefile-docker shell"
echo
print_info "To stop all services:"
echo "  make -f Makefile-docker down"
echo