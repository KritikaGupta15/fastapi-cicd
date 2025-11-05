from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_endpoints():
    # Test creating a product
    response = client.post(
        "/products",
        json={"name": "API Test Product", "price": 49.99, "description": "Test description"}
    )
    assert response.status_code == 201
    
    # Test retrieving the product
    product_id = response.json()["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "API Test Product"
    
    # Test updating the product
    response = client.put(
        f"/products/{product_id}",
        json={"name": "Updated Product", "price": 59.99}
    )
    assert response.status_code == 200
    
    # Test deleting the product
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
