from helper.config import VALID_CREDENTIALS


def test_successful_login(setup_load_page, validation):
    login_page = setup_load_page
    login_page.perform_login(VALID_CREDENTIALS["user_email"], VALID_CREDENTIALS["user_password"])
    validation.validate_user_logged_in()
