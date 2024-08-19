from pages.page import Page
from locators.personal_page_locators import Login
from locators.order_locators import Order
from locators.main_page_locators import Main


class OrderPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_page(self):
        return self.click_on_element(Login.ACCOUNT_PAGE_BUTTON)

    def view_order_details(self):
        self.click_on_element(Order.ORDER_FEED_LINK)
        self.click_on_element(Order.FIRST_ORDER_ITEM)
        return self.find_element(Order.ORDER_DETAILS_TEXT)

    def add_ingredient_and_place_order(self):
        source_element = self.find_element(Main.FIRST_INGREDIENT)
        target_element = self.find_element(Main.BASKET_ITEM)
        self.drop_element(source_element, target_element)
        self.click_on_element(Order.PLACE_ORDER_BUTTON)
        return self.get_new_order_number()

    def login_user(self, email, password):
        self.send_keys_to_element(Login.EMAIL_INPUT, email)
        self.send_keys_to_element(Login.PASSWORD_INPUT, password)
        self.click_on_element(Login.SIGN_IN_BUTTON)

    def get_new_order_number(self):
        self.wait_text_element_change(Order.ORDER_PRICE_DISPLAY, '9999')
        return self.get_text_element(Order.ORDER_PRICE_DISPLAY)

    def get_orders_in_progress(self):
        self.close_order_popup()
        self.click_on_element(Order.ORDER_FEED_LINK)
        self.click_on_element(Order.ACTIVE_ORDER_ITEM)
        return self.get_text_element(Order.ORDER_NUMBER_DISPLAY)

    def get_total_orders_all_time(self):
        self.click_on_element(Order.ORDER_FEED_LINK)
        self.wait_and_find_element(Order.TOTAL_ORDERS_COUNT)
        return self.get_text_element(Order.TOTAL_ORDERS_COUNT)

    def get_total_orders_today(self):
        self.click_on_element(Order.ORDER_FEED_LINK)
        self.wait_and_find_element(Order.TODAY_ORDERS_COUNT)
        return self.get_text_element(Order.TODAY_ORDERS_COUNT)

    def place_order_and_verify(self):
        self.click_on_element(Main.CONSTRUCTOR_BUTTON)
        self.add_ingredient_and_place_order()
        self.close_order_popup()
        self.click_on_element(Order.ORDER_FEED_LINK)

    def close_order_popup(self):
        self.click_on_element(Order.MODAL_CLOSE_BUTTON)


