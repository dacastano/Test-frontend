from selenium.webdriver.common.by import By


class HomeWebElements:
    logo = (By.CSS_SELECTOR, '.gPDR-main-logo-link')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, '.pageContent .SearchPage__FrontDoor .HPw7-form-fields-and-submit .HPw7-submit button')
