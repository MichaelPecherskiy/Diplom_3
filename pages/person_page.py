import routes
from pages.page import Page
from utils import unique_email
from locators.personal_page_locators import Login


class PersonalPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_page(self):
        self.find_element(Login.ACCOUNT_PAGE_BUTTON).click()

    def logout_from_account(self):
        self.find_element(Login.LOGOUT_BUTTON).click()
        self.wait_for_url_to_be(routes.URL_LOGIN)

    def click_history_order(self):
        self.find_element(Login.ORDER_HISTORY_LINK).click()
        self.wait_for_url_to_be(routes.URL_HISTORY)

    def login_user(self, email, password):
        self.find_element(Login.EMAIL_INPUT).send_keys(email)
        self.find_element(Login.PASSWORD_INPUT).send_keys(password)
        self.find_element(Login.SIGN_IN_BUTTON).click()

    def click_resset_password(self):
        self.find_element(Login.ACCOUNT_PAGE_BUTTON).click()
        self.find_element(Login.FORGOT_PASSWORD_LINK).click()

    def data_input_click_resset(self):
        email = unique_email()
        self.find_element(Login.EMAIL_INPUT).send_keys(email)
        self.find_element(Login.RECOVER_BUTTON).click()
        self.wait_for_url_to_be(routes.URL_RESSET_PASSWORD)

    def click_show_button(self):
        self.find_element(Login.TOGGLE_PASSWORD_VISIBILITY_BUTTON).click()
        return self.find_element(Login.ACTIVE_INPUT_FIELD)
