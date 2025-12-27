#!/usr/bin/env python3
"""Initialize database schema."""

import os
import sys
import psycopg2
from dotenv import load_dotenv

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

load_dotenv()


def setup_database() -> None:
    """Set up database tables and indexes."""
    db_url = os.getenv("DATABASE_URL", "")

    if not db_url:
        print("ERROR: DATABASE_URL not set in .env")
        sys.exit(1)

    # Parse connection string
    try:
        parts = db_url.replace("postgresql://", "").split("@")
        user_pass = parts[0].split(":")
        host_db = parts[1].split("/")
        host_port = host_db[0].split(":")

        user = user_pass[0]
        password = user_pass[1]
        host = host_port[0]
        port = host_port[1] if len(host_port) > 1 else "5432"
        dbname = host_db[1]

        print(f"Connecting to {host}:{port}/{dbname}...")

        conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )

        cursor = conn.cursor()

        # Read and execute init.sql
        with open("database/init.sql", "r") as f:
            sql_commands = f.read()

        statements = [stmt.strip() for stmt in sql_commands.split(";") if stmt.strip()]

        # Execute commands one by one
        for command in statements:
            if command.strip():
                cursor.execute(command)

        # conn.commit()


        print("✓ Database initialized successfully!")
        
        cursor.close()
        conn.close()

        # Run Veda Schema Setup
        print("Setting up Veda/Scripture Schema...")
        from scripts.setup_veda_schema import setup_schema
        setup_schema()
        print("✓ Veda/Scripture schema initialized!")

    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    setup_database()
