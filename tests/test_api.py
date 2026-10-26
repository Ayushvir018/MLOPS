# Import Testclient so we can send simulated http requests
from fastapi.testclient import TestClient
#import app object defie in main.py
from main import app
#reusable test client for all test function
client=TestClient(app)

#first test function for home page
def test_health_endpoint():
    """
    varify that app is running and can respond
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_valid_iris_prediction():
    """
    Test prediction with valid iris features
    """
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    #send simulated POST req with JSON input
    response = client.post("/predict", json=payload)
    # endpoint accept valid input
    assert response.status_code == 200
    
    result=response.json()
    assert "prediction" in result
    assert "class_name" in result

    assert result["class_name"] in ["Setosa","Versicolor","Virginica"]
    assert result['prediction'] in [0,1,2]
    

