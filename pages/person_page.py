import routes
import allure
from pages.page import BasePage
from utils import unique_email
from locators.personal_page_locators import Login


@allure.step('Класс для работы с Личным кабинетом')
class PersonalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход в Личный кабинет')
    def click_personal_page(self):
        self.find_element(Login.ACCOUNT_PAGE_BUTTON).click()

    @allure.step('Выход из аккаунта')
    def logout_from_account(self):
        self.find_element(Login.LOGOUT_BUTTON).click()
        self.wait_for_url_to_be(routes.URL_LOGIN)

    @allure.step('Переход в раздел История заказов')
    def click_history_order(self):
        self.find_element(Login.ORDER_HISTORY_LINK).click()
        self.wait_for_url_to_be(routes.URL_HISTORY)

    @allure.step('Авторизация пользователя')
    def login_user(self, email, password):
        self.find_element(Login.EMAIL_INPUT).send_keys(email)
        self.find_element(Login.PASSWORD_INPUT).send_keys(password)
        self.find_element(Login.SIGN_IN_BUTTON).click()

    @allure.step('Переход к восстановлению пароля')
    def click_reset_password(self):
        self.find_element(Login.ACCOUNT_PAGE_BUTTON).click()
        self.find_element(Login.FORGOT_PASSWORD_LINK).click()

    @allure.step('Ввод данных для восстановления пароля')
    def data_input_click_reset(self):
        email = unique_email()
        self.find_element(Login.EMAIL_INPUT).send_keys(email)
        self.find_element(Login.RECOVER_BUTTON).click()
        self.wait_for_url_to_be(routes.URL_RESSET_PASSWORD)

    @allure.step('Показать пароль')
    def click_show_button(self):
        self.find_element(Login.TOGGLE_PASSWORD_VISIBILITY_BUTTON).click()
        return self.find_element(Login.ACTIVE_INPUT_FIELD)
