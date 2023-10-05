import pytest
from fastapi.testclient import TestClient
from db.database import get_mongo_client
from main import asgi_app

client = TestClient(asgi_app)


@pytest.fixture(scope="module")
def clean_database():
    # Set up: connect to the database and get the collection
    mongo_client = get_mongo_client()

    # Wipe the database before running tests
    mongo_client.delete_many({})

    yield  # This is where the tests will run

    # Tear down: wipe the database after running all tests
    mongo_client.delete_many({})


def test_valid_csv_file(clean_database):
    # Create a temporary valid CSV file

    with open("test_sample.csv", "rb") as f:
        response = client.post("/upload", files={"file": ("test_sample.csv", f)})
    assert response.status_code == 200
    response_json = response.json()
    assert "documents inserted" in response_json["message"]
    assert response_json["message"] == "3 documents inserted."


def test_invalid_file_type():
    response = client.post("/upload", files={"file": ("test.txt", "some text")})
    assert response.status_code == 400
    assert response.json() == {"detail": "Only CSV files are allowed."}


def test_no_file():
    response = client.post("/upload")
    assert response.status_code == 422


def test_non_post_request():
    response = client.get("/upload")
    assert response.status_code == 405
    assert response.json() == {"detail": "Only POST requests are allowed."}


def test_invalid_endpoint():
    response = client.post("/invalid")
    assert response.status_code == 404
    assert response.json() == {"detail": "Endpoint not allowed."}
