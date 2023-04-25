from base.base_api import BaseApi

endpoint = 'https://fakestoreapi.com/'
get_users_endpoint = "users"
get_single_user_endpoint = "users/"
limits_results_endpoint = "limit/"
sort_results_endpoint = "sort"
add_new_user_endpoint = "users"
update_user_endpoint = "users/"
delete_user_endpoint = "users/id"


class Users(BaseApi):

    def get_users(self, expected_status_code):
        response = self.get_request(endpoint + get_users_endpoint)
        self.check_status_code(response, expected_status_code)
        response_data = response.json()
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response_data

    def find_users_response_length(self, response, length):
        assert len(response) == length

    def get_single_user(self, user_id, expected_status_code):
        response = self.get_request(endpoint + get_single_user_endpoint + str(user_id))
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    def create_user(self, json_data, expected_status_code):
        url = endpoint + add_new_user_endpoint
        response = self.post_request(url, json_data, headers=None)
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response

    def edit_user(self, json_data, user_id, expected_status_code):
        response = self.put_request(endpoint + update_user_endpoint + str(user_id), json_data)
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"
        return response
