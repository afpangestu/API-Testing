import requests

url = "https://secondhand.binaracademy.org"
USER_ID = 0
def test_login_user():
    jsonBody = {
        "user": {
            "email": "ajiseller@mail.com",
            "password": "ajiseller"
        }
    }

    response = requests.post(url + "/users/sign_in.json", json=jsonBody)

    # Verify status code
    assert response.status_code == 200

    data = response.json()

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print(data)

    # Store response value to variable
    USER_ID = data['user']['id']
    print(USER_ID)

def test_get_offer_by_userid():
    response = requests.get(url + f"/users/{USER_ID}/offers.json")

    # Verify status code (BAKAL ERROR SOALNYA SESI LOGIN GAK KE SIMPEN
    assert response.status_code == 401

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    print(data)