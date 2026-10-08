import logging

from playwright.sync_api import Locator, Page

from helper.utils import LogLevel, log_message, take_screenshot


class BasePage:
    def __init__(self, page:Page):
        self.page = page 
        self.logger = logging.getLogger(self.__class__.__name__)

    def safe_execute(self, action, action_name: str, *args):
        try:
            log_message(self.logger, level = LogLevel.INFO, message = f"Executing action: {action_name} with arguments: {args}")
            action(*args)

        except Exception as e:
            log_message(self.logger, level = LogLevel.ERROR, message = f"Failed executing action: {action_name} with arguments: {args}")
            take_screenshot(self.page, action_name)

            raise
    def click_element(self, locator: Locator):
        self.safe_execute(locator.click, "click_element")

    def type_text(self, locator: Locator, text: str):
        self.safe_execute(locator.fill, "type_text", text)

    def navigate_to(self, url:str):
        self.safe_execute(self.page.goto, "navigate_to", url)