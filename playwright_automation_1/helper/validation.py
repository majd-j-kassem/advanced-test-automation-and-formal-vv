from page_objects.base_page import BasePage
from helper.utils import LogLevel, log_message, take_screenshot
from playwright.sync_api import expect

class AppValidation(BasePage):

    def __init__(self, setup_all_pages):
        self.login_page, self.main_page = setup_all_pages
        super().__init__(self.login_page)

    def validate_user_logged_in(self):
        login_button = self.login_page.login_button

        try:
            expect(login_button).not_to_be_visible(), "Fiaild to login"
        except Exception as e:
            log_message(self.logger, level = LogLevel.ERROR, message = f"Login Faild")
            take_screenshot(self.page, name = "Login Faild")
            raise Exception("Login button still appears, failed login") from e