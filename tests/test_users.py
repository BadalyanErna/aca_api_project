import user_json
from endpoints.users import Users


def test_get_all_users(app_config):
    users = Users()
    response_data = users.get_users(expected_status_code=200)
    expected_length = len(response_data)
    users.find_users_response_length(response_data, expected_length)


def test_get_single_user(app_config):
    user = Users()
    response = user.get_single_user(expected_status_code=200, user_id=1)
    response_data = response.json()
    assert response_data["id"] == 1

def test_get_results_by_limit(app_config):
    user = Users()

def test_create_user(app_config):
    users = Users()
    json_data = user_json.create_user_json("test_user@gmail.com", "TestUser", "TestPass", "QA", "Testing", "Yerevan",
                                           "Mergelyan",
                                           "12", "0041", "0067666", "090909", "09230293")
    response = users.create_user(json_data, expected_status_code=200)
    assert response.status_code == 200
    assert "id" in response.json()


def test_update_user(app_config):
    users = Users()
    response_data = user_json.update_user_json("test_user@gmail.com", "ChangedUsername", "TestPass", "ChangedName",
                                           "ChangedLastName", "Yerevan",
                                           "Mergelyan", "12", "0041", "0067666", "090909", "09230293")
    response = users.edit_user(response_data, user_id=1, expected_status_code=200)
