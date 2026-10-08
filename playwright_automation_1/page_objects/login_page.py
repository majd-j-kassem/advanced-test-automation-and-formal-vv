from playwright_automation_1.helper.utils import LogLevel, log_message, take_screenshot
from playwright_automation_1.page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self.username_field = self.page.locator("[name='email']")
        self.password_field = self.page.locator("[name='pass']")
        self.login_button = self.page.locator("[name='Log In']")

    def perform_login(self, user_name: str, password: str):

        log_message(self.logger, log_level = LogLevel.INFO, message = f"Performing Login with username: \
                    {user_name}, password: {password}")
        self.type_text(self.username_field, user_name)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)

        if(self.login_button.is_visible()):
            log_message(self.logger, log_level = LogLevel.ERROR, message = "Loggin Failed!")
            take_screenshot(self.page, name = "login_failed")
            return None
        return self.MainPage(page)
