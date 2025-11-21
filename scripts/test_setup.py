#!/usr/bin/env python3
"""Test VidwaanAI setup."""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def test_imports():
    """Test if all imports work."""
    print("Testing imports...")
    try:
        import fastapi
        import typer
        import llama_index
        from sentence_transformers import SentenceTransformer
        import psycopg2
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_database():
    """Test database connection."""
    print("\nTesting database connection...")
    try:
        import psycopg2
        db_url = os.getenv("DATABASE_URL")

        if not db_url:
            print("✗ DATABASE_URL not set")
            return False

        # Parse and connect
        parts = db_url.replace("postgresql://", "").split("@")
        user_pass = parts[0].split(":")
        host_db = parts[1].split("/")
        host_port = host_db[0].split(":")

        conn = psycopg2.connect(
            dbname=host_db[1],
            user=user_pass[0],
            password=user_pass[1],
            host=host_port[0],
            port=host_port[1] if len(host_port) > 1 else "5432"
        )
        conn.close()
        print("✓ Database connection successful")
        return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False

def test_embeddings():
    """Test embedding model download."""
    print("\nTesting embeddings model...")
    try:
        from sentence_transformers import SentenceTransformer
        print("  Downloading Vyakyarth model (first run may take time)...")
        model = SentenceTransformer('krutrim-ai-labs/vyakyarth')
        embedding = model.encode("test")
        print(f"✓ Embeddings model working (dim: {len(embedding)})")
        return True
    except Exception as e:
        print(f"✗ Embeddings model failed: {e}")
        return False

def test_openai():
    """Test OpenAI API key."""
    print("\nTesting OpenAI API...")
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "sk-your-key-here":
            print("✗ OPENAI_API_KEY not configured")
            return False
        print("✓ OpenAI API key configured")
        return True
    except Exception as e:
        print(f"✗ OpenAI API test failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("VidwaanAI Setup Test")
    print("=" * 50)

    results = {
        "Imports": test_imports(),
        "Database": test_database(),
        "Embeddings": test_embeddings(),
        "OpenAI": test_openai()
    }

    print("\n" + "=" * 50)
    print("Test Results:")
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {test_name}: {status}")

    all_passed = all(results.values())
    print("=" * 50)

    if all_passed:
        print("\n✓ All tests passed! You're ready to use VidwaanAI.")
    else:
        print("\n✗ Some tests failed. Please check configuration.")
        sys.exit(1)
