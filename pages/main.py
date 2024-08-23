import allure
import routes
from locators.main_page_locators import Main
from pages.page import BasePage
from locators.personal_page_locators import Login


@allure.step('Работа с основной страницей')
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие раздела "Мой аккаунт"')
    def open_my_account(self):
        self.find_element(Main.ACCOUNT_BUTTON).click()

    @allure.step('Переход в конструктор')
    def navigate_to_constructor(self):
        self.find_element(Main.ACCOUNT_BUTTON).click()
        self.wait_for_url_to_be(routes.URL_LOGIN)
        self.find_element(Main.CONSTRUCTOR_BUTTON).click()
        return self.find_element(Main.BUILD_BURGER_TEXT)

    @allure.step('Переход в ленту заказов')
    def navigate_to_order_feed(self):
        self.find_element(Main.ORDER_TRACKING_BUTTON).click()
        self.wait_for_url_to_be(routes.URL_FEED)
        return self.find_element(Main.ORDER_FEED_HEADER)

    @allure.step('Открытие информации о первом ингредиенте')
    def ingredient_detail(self):
        self.find_element(Main.FIRST_INGREDIENT).click()
        return self.find_element(Main.INGREDIENT_DETAILS_HEADER)

    @allure.step('Закрытие информации о ингредиенте')
    def close_ingredient_detail(self):
        self.find_element(Main.CLOSE_MODAL_BUTTON).click()

    @allure.step('Проверка закрытия информации о ингредиенте')
    def ingredient_info_closed(self):
        return self.get_attribute(Main.INGREDIENT_DETAILS_WINDOW, 'class')

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        source_element = self.find_element(Main.FIRST_INGREDIENT)
        target_element = self.find_element(Main.BASKET_ITEM)
        self.drop_element(source_element, target_element)
        return self.find_element(Main.INGREDIENT_COUNT)

    @allure.step('Вход в систему')
    def login_user(self, email, password):
        self.find_element(Login.EMAIL_INPUT).send_keys(email)
        self.find_element(Login.PASSWORD_INPUT).send_keys(password)
        self.find_element(Login.SIGN_IN_BUTTON).click()

    @allure.step('Оформление заказа')
    def place_an_order(self):
        self.find_element(Main.SUBMIT_ORDER_BUTTON).click()
        return self.find_element(Main.ORDER_CONFIRMATION_TEXT)

