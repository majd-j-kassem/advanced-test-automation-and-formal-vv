from enum import Enum

try:

    import allure
    ALLURE_AVAILABLE = True
except ImportError:
    ALLURE_AVAILABLE = False

class LogLevel(Enum):
    INFO = "info"
    DEBUG = "debug"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

def log_message(logger, level: LogLevel, message: str, attach_to_allure: bool = True):
    if level == LogLevel.INFO:
        logger.info(message)
    elif level == LogLevel.DEBUG:
        logger.debug(message)
    elif level == LogLevel.WARNING:
        logger.warning(message)
    elif level == LogLevel.ERROR:
        logger.error(message)
    elif level == LogLevel.CRITICAL:
        logger.critical(message)

    if attach_to_allure:
        if ALLURE_AVAILABLE:
            allure.attach(message, name=f"(Log{level.value.upper()}) Message", attachment_type=allure.attachment_type.TEXT)
        else:
            logger.warning("Allure is not installed. Skipping attachment to Allure report.")

def take_screenshot(page, name : str = "screenshot"):
    try:
        screenshot_data = page.screenshot(type = "png")
        if ALLURE_AVAILABLE:
            allure.attach(screenshot_data, name = name, attachment_type = allure.attachment_type.PNG)
    except Exception:
        return None

