import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_price = prod_page.get_prod_price()
    bascket_price = prod_page.get_total_cost_on_header()
    prod_page.add_current_prod_to_basked()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_status_msg_with(f"{prod_page.get_prod_name()} has been added to your basket.")
    prod_page.should_be_status_msg_with(f"Your basket total is now £{prod_price + bascket_price}")
    prod_page.should_be_basket_total_increased_on(prod_price, bascket_price)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара 
    # Добавляем товар в корзину 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    pass

def test_guest_cant_see_success_message (browser):
    # Открываем страницу товара 
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    pass

def test_message_disappeared_after_adding_product_to_basket (browser):
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    pass

