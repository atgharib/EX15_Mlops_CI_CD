import pytest
from app import app
from forms import InputForm

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_predict(client):
    form_data = {
        'mean_radius': 17.99,
        'mean_perimeter': 122.80,
        'mean_area': 1001.0,
        'mean_concavity': 30.0,
        'mean_concave_points': 14.0,
        'worst_radius': 16.0,
        'worst_perimeter': 164.80,
        'worst_area': 2019.0,
        'worst_concavity': 70.0,
        'worst_concave_points': 26.0        
    }
 
    response = client.post('/predict', data=form_data)
    assert response.status_code == 302  # Redirect

    response = client.get(response.location)
    assert response.status_code == 200

def test_input(client):
    response = client.get('/input')
    assert response.status_code == 200
    assert 'mean_radius' in response.get_data(as_text=True)
    assert 'mean_perimeter' in response.get_data(as_text=True)
    assert 'mean_area' in response.get_data(as_text=True)
    assert 'mean_concavity' in response.get_data(as_text=True)
    assert 'mean_concave_points' in response.get_data(as_text=True)
    assert 'worst_radius' in response.get_data(as_text=True)
    assert 'worst_perimeter' in response.get_data(as_text=True)
    assert 'worst_area' in response.get_data(as_text=True)
    assert 'worst_concavity' in response.get_data(as_text=True)
    assert 'worst_concave_points' in response.get_data(as_text=True)
    assert 'Send' in response.get_data(as_text=True)  # check for the submit button

def test_result(client):
    response = client.get('/result?predicted_class=some_class')
    assert response.status_code == 200
    assert 'some_class' in response.get_data(as_text=True)
