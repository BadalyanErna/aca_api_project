import user_json
from endpoints.users import Users
from config import Config


def test_get_all_users(app_config):
    users = Users()
    response_data = users.get_users(expected_status_code=200)
    expected_length = len(response_data)
    users.find_users_response_length(response_data, expected_length)


def test_get_single_user(app_config):
    user = Users()
    response = user.get_single_user(expected_status_code=200, user_id=1)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == 1


def test_create_user(app_config):
    user = Users()
    json = user_json.create_user_json("test_user@gmail.com", "TestUser", "TestPass", "QA", "Testing", "Yerevan",
                                      "Mergelyan",
                                      "12", "0041", "0067666", "090909", "09230293")
    response = user.create_user(app_config, json)
    assert response["id"] is not None
