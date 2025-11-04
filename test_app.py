from app import app


def test_home():
    """Test that the home route returns status 200 and contains 'Hello'."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data
