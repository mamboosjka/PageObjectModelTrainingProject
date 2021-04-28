import math
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import HeaderLocators

class BasePage():
    def __init__(self, browser, url, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, selector):
        try:
            self.browser.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def normalise_cost(self,cost: str):
        return float(cost[1:])

    def get_total_cost_on_header(self):
        durty_text = self.browser.find_element(*HeaderLocators.BASKET_TOTAL_INFO).text
        return self.normalise_cost(durty_text.replace('Basket total:', '').replace('View basket', '').strip())        

    def should_be_basket_total_increased_on(self, added_prod_coast=0.0, initial_price=0.0):
        current_bskt_price = self.get_total_cost_on_header()
        expected_bskt_price = initial_price+added_prod_coast
        assert  (current_bskt_price == expected_bskt_price), f"Basket price: {current_bskt_price} is wrong!, Expext that it its: {(expected_bskt_price)}."

    def get_text_of_status_message(self, message):
        msg_classes = message.get_attribute("class").split(' ')
        if "alert-info" in msg_classes:
            return message.find_element(*HeaderLocators.STATUS_INFO_MSG_TEXT).text
        return message.find_element(*HeaderLocators.STATUS_MSG_TEXT).text

    def find_status_msg_with(self, expected_text: str):
        messages = self.browser.find_elements(*HeaderLocators.STATUS_MSGS)
        if not messages:
            return False
        for message in messages:
            if self.get_text_of_status_message(message) == expected_text:
                return True
        return False

    def should_be_status_msg_with(self, text: str):
        assert self.find_status_msg_with(text), f"Cant find message with text: '{text}'."

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_not_be_success_message(self):
        assert not self.is_element_present(*HeaderLocators.SUCCESS_STATUS_MSG), "Success message is presented but should NOT."



