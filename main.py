import requests

url = "https://secondhand.binaracademy.org"
def test_login_user():
    data = {
        "user": {
            "email": "ajiseller@mail.com",
            "password": "ajiseller"
        }
    }

    response = requests.post(url + "/users/sign_in.json", json=data)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
