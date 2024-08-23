import allure
import routes
from pages.person_page import PersonalPage


import allure


@allure.epic("Личный кабинет")
class TestPersonalPage:

    @allure.title('Переход в Личный кабинет')
    @allure.description('Переход по клику на «Личный кабинет».')
    def test_open_personal_page(self, driver, create_ui_user):
        user_page = PersonalPage(driver)
        user_page.click_personal_page()
        user_page.login_user(create_ui_user['email'], create_ui_user['password'])
        user_page.click_personal_page()
        assert user_page.get_current_url() == routes.URL_PROFILE

    @allure.title('Переход в раздел История заказов')
    @allure.description('Переход в раздел «История заказов» в Личном кабинете.')
    def test_open_order_history(self, driver, create_ui_user):
        user_page = PersonalPage(driver)
        user_page.click_personal_page()
        user_page.login_user(create_ui_user['email'], create_ui_user['password'])
        user_page.click_personal_page()
        user_page.click_history_order()
        assert user_page.get_current_url() == routes.URL_HISTORY

    @allure.title('Выход из аккаунта')
    @allure.description('Выход из аккаунта в Личном кабинете.')
    def test_logout_from_account(self, driver, create_ui_user):
        user_page = PersonalPage(driver)
        user_page.click_personal_page()
        user_page.login_user(create_ui_user['email'], create_ui_user['password'])
        user_page.logout_from_account()
        assert user_page.get_current_url() == routes.URL_LOGIN
