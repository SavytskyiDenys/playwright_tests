import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text.lower()}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/SavytskyiDenys')
    body = r.json()
    headers = r.headers
    assert body['name'] == 'Denys Savytskyi'
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/users/Savytskyi_Denys')
    assert r.status_code == 404
