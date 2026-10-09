import logger
import pytest
from playwright_automation_1.helper.config import URL
from playwright_automation_1.helper.utils import log_level, log_message
from playwright_automation_1.page_objects.login_page import LoginPage


@pytest.fixture
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headed", default = False)
    browser = playwright.chromium.launch(headless = not headed)
    page = browser.new_page()

    try:
        yield page

    finally:
        log_message(logger, message = "Closing the browser", log_level = log_level.INFO)
        browser.close()

@pytest.fixture
def setup_page(setup_playwright):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(URL)
    log_message(logger, message = f"Navigating to the {URL}", log_level = log_level.INFO)
    yield login_page
    