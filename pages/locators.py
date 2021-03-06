from selenium.webdriver.common.by import By


class HeaderLocators():
    BASKET_TOTAL_INFO = (By.CSS_SELECTOR, "div.basket-mini.pull-right")
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, "div.basket-mini.pull-right>span>a.btn")
    STATUS_MSGS = (By.CSS_SELECTOR, "div#messages>div.alert")
    SUCCESS_STATUS_MSG = (By.CSS_SELECTOR, "div#messages>div.alert-success")
    STATUS_MSG_TEXT = (By.CSS_SELECTOR, "div.alertinner")
    STATUS_INFO_MSG_TEXT = (By.CSS_SELECTOR, "div.alertinner>p:nth-child(1)")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    EMAIL_FOR_LOGIN_FLD = (By.CSS_SELECTOR, "input#id_login-username")
    PASS_FOR_LOGIN_FLD = (By.CSS_SELECTOR, "input#id_login-password")
    FORGET_PASS_LINK = (By.CSS_SELECTOR, "form#login_form a")
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.btn-lg.btn-primary[name="login_submit"][type="submit"]')
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    EMAIL_FOR_REG_FLD = (By.CSS_SELECTOR, "input#id_registration-email")
    PASS_FOR_REG_FLD = (By.CSS_SELECTOR, "imput#id_registration-password1")
    CONFIRM_PASS_FLD =(By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, 'button.btn-lg.btn-primary[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PROD_COST_INFO = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
