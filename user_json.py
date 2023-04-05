import json


def create_user_json(email, username, password, firstname, lastname, city, street, number, zipcode, lat, long, phone):
    data = {
        "email": email,
        "username": username,
        "password": password,
        "name": {
            "firstname": firstname,
            "lastname": lastname
        },
        "address": {
            "city": city,
            "street": street,
            "number": number,
            "zipcode": zipcode,
            "geolocation": {
                "lat": lat,
                "long": long
            }
        },
        "phone": phone
    }

    json_data = json.dumps(data)
    return json_data


def update_user_json(email, username, password, firstname, lastname, city, street, number, zipcode, lat, long, phone):
    data = {
        "email": email,
        "username": username,
        "password": password,
        "name": {
            "firstname": firstname,
            "lastname": lastname
        },
        "address": {
            "city": city,
            "street": street,
            "number": number,
            "zipcode": zipcode,
            "geolocation": {
                "lat": lat,
                "long": long
            }
        },
        "phone": phone
    }

    json_data = json.dumps(data)
    return json_data


def delete_user_json(user_id):
    data = {
        "id": user_id
    }

    return data
