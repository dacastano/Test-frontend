from selenium.webdriver.common.by import By


class HomeWebElements:
    logo = (By.CSS_SELECTOR, '.gPDR-main-logo-link')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, 'button.RxNS.RxNS-mod-stretch')
    trip_type_dropdown = (By.CSS_SELECTOR, '.udzg-mod-size-small')
    from_text_input = (By.CSS_SELECTOR, '.J_T2-mod-collapse-m > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input')
    to_text_input = (By.CSS_SELECTOR, '.J_T2-mod-collapse-m > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')