"""
Test script to verify RAG Chatbot setup
Run this before starting the application to check everything is configured correctly.
"""
import os
import sys
import json
from pathlib import Path


def check_mark(condition):
    """Return checkmark or X based on condition."""
    return "✅" if condition else "❌"


def test_python_version():
    """Check Python version."""
    print("\n1️⃣  Checking Python version...")
    version = sys.version_info
    is_valid = version.major == 3 and version.minor >= 9
    print(f"   {check_mark(is_valid)} Python {version.major}.{version.minor}.{version.micro}")
    if not is_valid:
        print("   ⚠️  Python 3.9+ required")
    return is_valid


def test_packages():
    """Check if required packages are installed."""
    print("\n2️⃣  Checking required packages...")
    packages = {
        "fastapi": "FastAPI",
        "anthropic": "Anthropic SDK",
        "sentence_transformers": "Sentence Transformers",
        "gradio": "Gradio",
        "numpy": "NumPy",
        "pydantic": "Pydantic",
        "uvicorn": "Uvicorn"
    }

    all_installed = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"   ✅ {name}")
        except ImportError:
            print(f"   ❌ {name} - Not installed")
            all_installed = False

    if not all_installed:
        print("\n   Run: pip install -r requirements.txt")

    return all_installed


def test_env_file():
    """Check if .env file exists and has required variables."""
    print("\n3️⃣  Checking .env file...")
    env_path = Path(".env")

    if not env_path.exists():
        print("   ❌ .env file not found")
        print("   Run: cp .env.example .env")
        return False

    print("   ✅ .env file exists")

    # Check for required variables
    with open(env_path) as f:
        content = f.read()

    required_vars = [
        "ANTHROPIC_API_KEY",
        "GRAPH_PATH",
        "EMBEDDINGS_PATH",
        "SCHEMA_PATH"
    ]

    all_vars_present = True
    for var in required_vars:
        if var in content and not content.split(f"{var}=")[1].split("\n")[0].strip() == "":
            print(f"   ✅ {var} is set")
        else:
            print(f"   ❌ {var} is missing or empty")
            all_vars_present = False

    # Check API key format
    if "ANTHROPIC_API_KEY=sk-ant-" in content:
        print("   ✅ API key format looks correct")
    else:
        print("   ⚠️  API key may not be valid (should start with 'sk-ant-')")

    return all_vars_present


def test_data_files():
    """Check if data files exist and are valid."""
    print("\n4️⃣  Checking data files...")

    # Load .env to get paths
    from dotenv import load_dotenv
    load_dotenv()

    files_to_check = {
        "graph.json": os.getenv("GRAPH_PATH"),
        "embeddings.json": os.getenv("EMBEDDINGS_PATH"),
        "schema.json": os.getenv("SCHEMA_PATH")
    }

    all_files_valid = True

    for name, path in files_to_check.items():
        if not path:
            print(f"   ❌ {name} - Path not set in .env")
            all_files_valid = False
            continue

        file_path = Path(path)
        if not file_path.exists():
            print(f"   ❌ {name} - File not found at {path}")
            all_files_valid = False
            continue

        # Check file size
        size_mb = file_path.stat().st_size / (1024 * 1024)
        print(f"   ✅ {name} - {size_mb:.2f} MB")

        # Validate JSON
        try:
            with open(file_path) as f:
                data = json.load(f)

            if name == "graph.json":
                entities = data.get('entities', [])
                print(f"      → {len(entities)} entities found")

            elif name == "embeddings.json":
                embeddings = data
                print(f"      → {len(embeddings)} embeddings found")
                # Check dimensions
                if embeddings:
                    first_embedding = list(embeddings.values())[0]
                    print(f"      → {len(first_embedding)} dimensions")

            elif name == "schema.json":
                entity_types = data.get('entity_types', {})
                print(f"      → {len(entity_types)} entity types")

        except json.JSONDecodeError as e:
            print(f"   ❌ {name} - Invalid JSON: {e}")
            all_files_valid = False
        except Exception as e:
            print(f"   ⚠️  {name} - Could not validate: {e}")

    return all_files_valid


def test_ports():
    """Check if required ports are available."""
    print("\n5️⃣  Checking port availability...")
    import socket

    ports = {
        8000: "FastAPI backend",
        7860: "Gradio UI"
    }

    all_ports_free = True
    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        sock.close()

        if result == 0:
            print(f"   ⚠️  Port {port} ({service}) is already in use")
            all_ports_free = False
        else:
            print(f"   ✅ Port {port} ({service}) is available")

    return all_ports_free


def main():
    """Run all tests."""
    print("=" * 60)
    print("  RAG Chatbot Setup Verification")
    print("=" * 60)

    results = {
        "Python version": test_python_version(),
        "Required packages": test_packages(),
        "Environment configuration": test_env_file(),
        "Data files": test_data_files(),
        "Port availability": test_ports()
    }

    print("\n" + "=" * 60)
    print("  Summary")
    print("=" * 60)

    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status}  {test_name}")
        if not passed:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 All checks passed! You're ready to start the chatbot.")
        print("\nRun: ./start.sh")
        print("Or manually start backend and UI (see README.md)")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\nSee SETUP.md for detailed setup instructions.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
