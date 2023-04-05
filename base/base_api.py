import requests


class BaseApi:

    def get_request(self, url, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers, verify=False)
        return response

    def post_request(self, url, json_data, headers=None):
        response = requests.post(url, json_data, headers=headers, verify=False)
        return response

    def put_request(self, url, json_data, headers=None):
        response = requests.put(url, json_data, headers=headers, verify=False)
        return response

    def delete_request(self, url, json_data, headers=None):
        response = requests.delete(url, json=json_data, headers=headers, verify=False)
        return response

    def check_status_code(self, response, expected_status_code):
        assert response.status_code == expected_status_code

