import json
import random
import string
from pathlib import Path

import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict


def set_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def set_payload_register(name, email, password):
    return {
        "user": {
            "name": f"{name}",
            "email": f"{email}",
            "password": f"{password}"
        }
    }


def set_payload_login(email, password):
    return {
        "user": {
            "email": f"{email}",
            "password": f"{password}"
        }
    }


def set_payload_profile(name, address, phone, city):
    # Open and read the JSON file
    with open('userdata.json', 'r') as file:
        data = json.load(file)
    return {
        "user": {
            "id": data['user_id'],
            "name": name,
            "email": data['email'],
            "phone_number": phone,
            "address": address,
            "city_id": city
        }
    }


def set_foto_profile(path):
    return {
        "user": {
            "avatar": path,
        }
    }


def set_login_seller():
    return {
        "user": {
            "email": "ajiseller@mail.com",
            "password": "ajiseller"
        }
    }


def save_session(response):
    # turn cookiejar into dict
    cookies = dict_from_cookiejar(response.cookies)

    # save them to file as JSON
    Path("cookies.json").write_text(json.dumps(cookies))


def load_session():
    # load the JSON file
    cookies = json.loads(Path("cookies.json").read_text())
    # turn the object into a cookie jar
    return cookiejar_from_dict(cookies)
