import requests

def test_login_user():
    url = "https://secondhand.binaracademy.org/users/sign_in.json"
    data = {
        "user": {
            "email": "ajiseller@mail.com",
            "password": "ajiseller"
        }
    }

    response = requests.post(url, json=data)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
