import requests
import pytest

def test_user_authentication_invalid(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {'user': 'admin', 'password': 'admin'}

    # Mock the get request
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=401,
                                                          text=""))

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text == ""

def test_user_authentication_valid(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'qwerty'}

    # Mock the get request
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200,
                                                          text=""))

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text == ""

if __name__ == "__main__":
    pytest.main()
