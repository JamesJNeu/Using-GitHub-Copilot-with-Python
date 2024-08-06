# tests/test_main.py

import sys
import os
from fastapi.testclient import TestClient


# Add the directory containing main.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(os.path.join(__file__, '..'))))
from main import app

client = TestClient(app)


# Add an additional blank line
def test_calculate_checksum():
    response = client.post("/checksum", json={"text": "example text"})
    assert response.status_code == 200
    assert response.json() == {"checksum": "f81e29ae988b19699abd92c59906d0ee"}