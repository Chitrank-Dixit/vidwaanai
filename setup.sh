#!/bin/bash
# VidwaanAI Setup Script - With MCP Server Support
# This script guides you through the initial, fully containerized setup of VidwaanAI
# with optional MCP Server integration for AI agent autonomy

set -e

# --- Configuration ---
COMPOSE_FILE_APP="docker-compose-full.yml"
COMPOSE_FILE_MCP="docker-compose-mcp.yml"
APP_SERVICE="app"
DB_SERVICE="db"
MCP_SERVICE="mcp-server"

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

function print_menu {
    echo
    echo "=================================="
    echo "VidwaanAI Setup Options"
    echo "=================================="
    echo "1) Run VidwaanAI only (without MCP)"
    echo "2) Run VidwaanAI with MCP Server"
    echo "3) Run MCP Server only"
    echo "4) Stop all services"
    echo "5) View service logs"
    echo "6) Exit"
    echo "=================================="
    echo
}

# --- Prerequisites Check ---
function check_prerequisites {
    print_info "Checking for prerequisites: Docker and Docker Compose..."

    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install it to proceed."
    fi

    if ! docker info &> /dev/null; then
        print_error "Docker daemon is not running. Please start Docker and try again."
    fi

    print_success "Docker is available."
}

# --- Environment Setup ---
function setup_environment {
    if [ ! -f .env ]; then
        print_info "Creating .env file from .env.example..."
        if [ -f .env.example ]; then
            cp .env.example .env
        else
            print_warning "No .env.example found. Creating minimal .env file..."
            cat > .env << EOF
# VidwaanAI Configuration
OPENAI_API_KEY=your-api-key-here
DATABASE_URL=postgresql://vidwaan_user:vidwaan_password@db:5432/vidwaan_db
REDIS_URL=redis://cache:6379
LOG_LEVEL=INFO

# MCP Server Configuration (optional)
MCP_PORT=3000
NEO4J_URI=bolt://neo4j-mcp:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=vidwaan123_mcp
EOF
        fi
        print_warning "Please review and edit the .env file with your API keys and configuration."
    else
        print_info ".env file already exists."
    fi
}

# --- Function: Setup VidwaanAI Only ---
function setup_vidwaan_only {
    print_info "Setting up VidwaanAI without MCP Server..."
    echo

    # Check if services are already running
    if docker-compose -f "$COMPOSE_FILE_APP" ps | grep -q "Up"; then
        print_warning "Some services are already running."
        read -p "Do you want to restart them? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Stopping existing services..."
            docker-compose -f "$COMPOSE_FILE_APP" down
        else
            print_info "Using existing services."
            show_vidwaan_info
            return
        fi
    fi

    print_info "Building and starting Docker services from '$COMPOSE_FILE_APP'..."
    docker-compose -f "$COMPOSE_FILE_APP" up --build -d
    print_success "All services are starting up in the background."

    # Wait for database
    wait_for_database "$COMPOSE_FILE_APP" "$DB_SERVICE"

    # Initialize database
    initialize_vidwaan_database "$COMPOSE_FILE_APP" "$APP_SERVICE"

    print_success "VidwaanAI setup is complete!"
    show_vidwaan_info
}

# --- Function: Setup VidwaanAI with MCP ---
function setup_vidwaan_with_mcp {
    print_info "Setting up VidwaanAI with MCP Server..."
    echo

    # Check if services are already running
    if docker-compose -f "$COMPOSE_FILE_APP" ps | grep -q "Up"; then
        print_warning "VidwaanAI services are already running."
        read -p "Do you want to restart them? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Stopping existing VidwaanAI services..."
            docker-compose -f "$COMPOSE_FILE_APP" down
        else
            print_info "Using existing VidwaanAI services."
        fi
    fi

    if docker-compose -f "$COMPOSE_FILE_MCP" ps | grep -q "Up"; then
        print_warning "MCP services are already running."
        read -p "Do you want to restart them? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Stopping existing MCP services..."
            docker-compose -f "$COMPOSE_FILE_MCP" down
        else
            print_info "Using existing MCP services."
        fi
    fi

    # Start VidwaanAI
    print_info "Starting VidwaanAI services..."
    docker-compose -f "$COMPOSE_FILE_APP" up --build -d
    print_success "VidwaanAI services are starting up."

    # Start MCP
    print_info "Starting MCP Server services..."
    docker-compose -f "$COMPOSE_FILE_MCP" up --build -d
    print_success "MCP services are starting up."

    # Wait for databases
    wait_for_database "$COMPOSE_FILE_APP" "$DB_SERVICE"
    sleep 5
    wait_for_mcp_server

    # Initialize databases
    initialize_vidwaan_database "$COMPOSE_FILE_APP" "$APP_SERVICE"
    initialize_mcp_database "$COMPOSE_FILE_MCP" "$MCP_SERVICE"

    print_success "VidwaanAI with MCP setup is complete!"
    show_combined_info
}

# --- Function: Setup MCP Only ---
function setup_mcp_only {
    print_info "Setting up MCP Server only..."
    echo

    # Check if services are already running
    if docker-compose -f "$COMPOSE_FILE_MCP" ps | grep -q "Up"; then
        print_warning "MCP services are already running."
        read -p "Do you want to restart them? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Stopping existing MCP services..."
            docker-compose -f "$COMPOSE_FILE_MCP" down
        else
            print_info "Using existing services."
            show_mcp_info
            return
        fi
    fi

    print_info "Building and starting MCP Server services from '$COMPOSE_FILE_MCP'..."
    docker-compose -f "$COMPOSE_FILE_MCP" up --build -d
    print_success "MCP services are starting up."

    # Wait for MCP server
    wait_for_mcp_server

    # Initialize database
    initialize_mcp_database "$COMPOSE_FILE_MCP" "$MCP_SERVICE"

    print_success "MCP Server setup is complete!"
    show_mcp_info
}

# --- Function: Wait for Database ---
function wait_for_database {
    local compose_file=$1
    local service=$2

    print_info "Waiting for database service ('$service') to be healthy..."
    max_retries=30
    for i in $(seq 1 $max_retries); do
        health_status=$(docker-compose -f "$compose_file" ps "$service" 2>/dev/null | grep 'healthy' || true)
        if [ -n "$health_status" ]; then
            print_success "Database is healthy and ready!"
            return
        fi
        if [ $i -eq $max_retries ]; then
            print_error "Database did not become healthy in time. Check 'docker-compose -f $compose_file logs $service'."
        fi
        echo -n "."
        sleep 2
    done
}

# --- Function: Wait for MCP Server ---
function wait_for_mcp_server {
    print_info "Waiting for MCP Server to be healthy..."
    max_retries=30
    for i in $(seq 1 $max_retries); do
        if curl -f http://localhost:3000/health &>/dev/null; then
            print_success "MCP Server is healthy and ready!"
            return
        fi
        if [ $i -eq $max_retries ]; then
            print_warning "MCP Server health check timed out. It may still be starting."
            return
        fi
        echo -n "."
        sleep 2
    done
}

# --- Function: Initialize VidwaanAI Database ---
function initialize_vidwaan_database {
    local compose_file=$1
    local service=$2

    print_info "Initializing VidwaanAI database..."

    print_info "(1/2) Initializing database schema..."
    if docker-compose -f "$compose_file" exec "$service" uv run python scripts/setup_db.py 2>/dev/null; then
        print_success "Database schema initialized."
    else
        print_warning "Database schema initialization skipped or failed. This may be normal if already initialized."
    fi

    print_info "(2/2) Loading sample data..."
    if docker-compose -f "$compose_file" exec "$service" uv run python scripts/load_sample_data.py 2>/dev/null; then
        print_success "Sample data loaded."
    else
        print_warning "Sample data loading skipped or failed. This may be normal if already initialized."
    fi
}

# --- Function: Initialize MCP Database ---
function initialize_mcp_database {
    local compose_file=$1
    local service=$2

    print_info "Initializing MCP database..."

    if docker-compose -f "$compose_file" exec "$service" python -c "import src.mcp.server; print('MCP initialized')" 2>/dev/null; then
        print_success "MCP database initialized."
    else
        print_warning "MCP initialization skipped or already initialized."
    fi
}

# --- Function: Stop All Services ---
function stop_all_services {
    print_info "Stopping all services..."

    if docker-compose -f "$COMPOSE_FILE_APP" ps | grep -q "Up"; then
        print_info "Stopping VidwaanAI services..."
        docker-compose -f "$COMPOSE_FILE_APP" down
        print_success "VidwaanAI services stopped."
    fi

    if docker-compose -f "$COMPOSE_FILE_MCP" ps | grep -q "Up"; then
        print_info "Stopping MCP services..."
        docker-compose -f "$COMPOSE_FILE_MCP" down
        print_success "MCP services stopped."
    fi

    print_success "All services stopped."
}

# --- Function: View Logs ---
function view_logs {
    echo
    echo "Select service to view logs:"
    echo "1) VidwaanAI Application"
    echo "2) MCP Server"
    echo "3) All services"
    echo "4) Back to main menu"
    read -p "Choice (1-4): " -n 1 -r
    echo
    case $REPLY in
        1) docker-compose -f "$COMPOSE_FILE_APP" logs -f app ;;
        2) docker-compose -f "$COMPOSE_FILE_MCP" logs -f mcp-server ;;
        3) 
            docker-compose -f "$COMPOSE_FILE_APP" logs -f &
            docker-compose -f "$COMPOSE_FILE_MCP" logs -f &
            wait
            ;;
        4) return ;;
        *) print_error "Invalid choice" ;;
    esac
}

# --- Function: Show VidwaanAI Info ---
function show_vidwaan_info {
    echo
    print_success "VidwaanAI is ready!"
    echo
    echo "Access Points:"
    echo "  - VidwaanAI API: http://localhost:8000"
    echo "  - Swagger UI: http://localhost:8000/docs"
    echo "  - PostgreSQL: localhost:5432"
    echo "  - Redis: localhost:6379"
    echo
    echo "Common Commands:"
    echo "  Query example:  make -f Makefile-docker query Q=\"What is dharma?\""
    echo "  Shell access:   make -f Makefile-docker shell"
    echo "  View logs:      docker-compose -f $COMPOSE_FILE_APP logs -f app"
    echo "  Stop services:  docker-compose -f $COMPOSE_FILE_APP down"
    echo
}

# --- Function: Show MCP Info ---
function show_mcp_info {
    echo
    print_success "MCP Server is ready!"
    echo
    echo "Access Points:"
    echo "  - MCP Server: http://localhost:3000"
    echo "  - Health Check: curl http://localhost:3000/health"
    echo "  - List Tools: curl http://localhost:3000/tools"
    echo "  - PostgreSQL: localhost:5434"
    echo "  - Neo4j: http://localhost:7475"
    echo "  - Redis: localhost:6380"
    echo
    echo "Common Commands:"
    echo "  Check health:   curl http://localhost:3000/health"
    echo "  List tools:     curl http://localhost:3000/tools"
    echo "  View logs:      docker-compose -f $COMPOSE_FILE_MCP logs -f mcp-server"
    echo "  Stop services:  docker-compose -f $COMPOSE_FILE_MCP down"
    echo
    echo "Next Steps:"
    echo "  1. Test a tool: python -c \"import requests; requests.post('http://localhost:3000/rpc', json={'jsonrpc': '2.0', 'method': 'tools/call', 'params': {'name': 'detect_language', 'arguments': {'query': 'à¤¨à¤®à¤¸à¥à¤¤à¥‡'}}})\" "
    echo "  2. Read: HOW-TO-RUN-MCP.md for more examples"
    echo "  3. Integrate with Claude: Use MCP with Claude SDK"
    echo
}

# --- Function: Show Combined Info ---
function show_combined_info {
    echo
    print_success "VidwaanAI with MCP Server is ready!"
    echo
    echo "=================================="
    echo "VidwaanAI Access Points"
    echo "=================================="
    echo "  - VidwaanAI API: http://localhost:8000"
    echo "  - Swagger UI: http://localhost:8000/docs"
    echo "  - PostgreSQL: localhost:5432"
    echo "  - Redis: localhost:6379"
    echo
    echo "=================================="
    echo "MCP Server Access Points"
    echo "=================================="
    echo "  - MCP Server: http://localhost:3000"
    echo "  - Health Check: curl http://localhost:3000/health"
    echo "  - List Tools: curl http://localhost:3000/tools"
    echo "  - PostgreSQL: localhost:5434"
    echo "  - Neo4j: http://localhost:7475"
    echo "  - Redis: localhost:6380"
    echo
    echo "=================================="
    echo "Common Commands"
    echo "=================================="
    echo "VidwaanAI:"
    echo "  Query: make -f Makefile-docker query Q=\"What is dharma?\""
    echo "  Shell: make -f Makefile-docker shell"
    echo "  Logs:  docker-compose -f $COMPOSE_FILE_APP logs -f app"
    echo
    echo "MCP Server:"
    echo "  Health:       curl http://localhost:3000/health"
    echo "  List tools:   curl http://localhost:3000/tools"
    echo "  Test tool:    See MCP-RUNNING-EXAMPLES.md"
    echo "  Logs:         docker-compose -f $COMPOSE_FILE_MCP logs -f mcp-server"
    echo
    echo "Both:"
    echo "  View all logs: Press '5' in this script"
    echo "  Stop all:      Press '4' in this script"
    echo
    echo "=================================="
    echo "Next Steps"
    echo "=================================="
    echo "1. Read documentation: START-HERE.md or QUICK-REFERENCE.md"
    echo "2. Test MCP tools: See MCP-RUNNING-EXAMPLES.md"
    echo "3. Integrate with Claude: Use Anthropic SDK with MCP"
    echo "4. Build your integration: Follow MCP-IMPLEMENTATION-CLEAN.md"
    echo
}

# --- Main Script ---
function main {
    clear
    check_prerequisites
    setup_environment

    while true; do
        print_menu
        read -p "Enter your choice (1-6): " -n 1 -r
        echo
        case $REPLY in
            1) setup_vidwaan_only ;;
            2) setup_vidwaan_with_mcp ;;
            3) setup_mcp_only ;;
            4) stop_all_services ;;
            5) view_logs ;;
            6) 
                print_success "Exiting setup script."
                exit 0
                ;;
            *)
                print_error "Invalid choice. Please select 1-6."
                ;;
        esac

        read -p "Press Enter to continue..."
        clear
    done
}

# Run main function
main