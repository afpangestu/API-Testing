import json
import os
from pathlib import Path
from helper import *

import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict

BASE_URL = "https://secondhand.binaracademy.org"


def test_register_user():
    userName = set_random_string(8)
    userEmail = set_random_string(8) + "@gmail.com"
    userPass = set_random_string(8)
    jsonBody = set_payload_register(
        name=userName,
        email=userEmail,
        password=userPass
    )
    response = requests.post(BASE_URL + "/users.json", json=jsonBody)
    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    print('\nResponse : ', data)
    USER_ID = data['user']['id']
    USER_NAME = data['user']['name']
    USER_EMAIL = data['user']['email']
    save_json = {
        "user_id": USER_ID,
        "name": USER_NAME,
        "email": USER_EMAIL,
        "password": userPass
    }
    # Store cookie session to json file
    save_session(response)
    # Store data register to json file
    Path("userdata.json").write_text(json.dumps(save_json))


def test_login_user():
    # Open and read the JSON file
    with open('userdata.json', 'r') as file:
        user_data = json.load(file)
    jsonBody = set_payload_login(
        email=user_data['email'],
        password=user_data['password']
    )
    # Send request
    response = requests.post(BASE_URL + "/users/sign_in.json", json=jsonBody)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    print('\nResponse : ', data)

    # Store cookie session to json file
    save_session(response)


def test_login_seller():
    # Get payload for seller login
    jsonBody = set_login_seller()
    # Send request
    response = requests.post(BASE_URL + "/users/sign_in.json", json=jsonBody)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    data = response.json()
    print('\nResponse : ', data)

    # Store response value to variable
    SELLER_ID = data['user']['id']
    SELLER_NAME = data['user']['name']

    # Open and read the JSON file
    with open('userdata.json', 'r') as file:
        seller_data = json.load(file)

    seller_data.update(
        {"seller_id": f"{SELLER_ID}", "seller_name": f"{SELLER_NAME}"}
    )

    # turn cookiejar into dict
    cookies = dict_from_cookiejar(response.cookies)

    # save them to file as JSON
    Path("cookies.json").write_text(json.dumps(cookies))
    Path("userdata.json").write_text(json.dumps(seller_data))


def test_get_offer_by_userid():
    # Open and read the JSON file
    with open('userdata.json', 'r') as file:
        data = json.load(file)

    # load the JSON file
    cookies = json.loads(Path("cookies.json").read_text())
    # turn the object into a cookie jar
    cookies = cookiejar_from_dict(cookies)

    response = requests.get(BASE_URL + f"/users/{data['user_id']}/offers.json", cookies=cookies)

    # Verify status code (BAKAL ERROR SOALNYA SESI LOGIN GAK KE SIMPEN
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    print('\nResponse : ', data)


def test_get_profile():
    response = requests.get(BASE_URL + "/profiles.json", cookies=load_session())
    data = response.json()
    print('\nResponse: ', data)


def test_update_fotoprofile():
    # INI SUCCESS TAPI IMG GAK KE KIRIM
    files = {"user['avatar']['filename']": (os.path.basename('img/garudabiru.jpg'), open('img/klepon1.png', 'rb'), 'application/json; charset=utf-8')}
    # INI JUGA SUCCESS TAPI IMG GAK KE KIRIM
    # files = {"user['avatar']": open('img/garudabiru.jpg', 'rb')}
    response = requests.put(BASE_URL + "/profiles.json", cookies=load_session(), files=files)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    data = response.json()
    print('\nResponse : ', data)


def test_update_profile():
    jsonBody = set_payload_profile(
        name="adwadad wwdiriawda",
        address="JAWDayakarta iyeeYe",
        phone="aawdad+62924124",
        city=1,
    )
    response = requests.put(BASE_URL + "/profiles.json", cookies=load_session(), json=jsonBody)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    data = response.json()
    print('\nResponse : ', data)

# def test_updateJsonFile():
#     # Open and read the JSON file
#     with open('userdata.json', 'r') as file:
#         data = json.load(file)
#
#     data.update({"key_baru": "value_JAJAJAJA"})
#     Path("userdata.json").write_text(json.dumps(data))
