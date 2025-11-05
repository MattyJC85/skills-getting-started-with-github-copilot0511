import pytest
from src.app import app
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    return TestClient(app)