from helper.utils import LogLevel, log_message, take_screenshot
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from playwright.sync_api import Page


class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self.username_field = self.page.locator("[name='username']")
        self.password_field = self.page.locator("[name='password']")
        self.login_button = self.page.locator("button[type='submit']")

    def perform_login(self, user_name: str, password: str):

        log_message(self.logger, level = LogLevel.INFO, message = f"Performing Login with username: \
                    {user_name}, password: {password}")
        self.type_text(self.username_field, user_name)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)

        if(self.login_button.is_visible()):
            log_message(self.logger, level = LogLevel.ERROR, message = "Loggin Failed!")
            take_screenshot(self.page, name = "login_failed")
            return None
        return MainPage(self.page)
