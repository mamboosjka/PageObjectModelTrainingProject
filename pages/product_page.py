from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_current_prod_to_basked(self):
        add_to_bskt_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_bskt_btn.click()

    def get_prod_price(self):
        return self.normalise_cost(self.browser.find_element(*ProductPageLocators.PROD_COST_INFO).text)

    def get_prod_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
