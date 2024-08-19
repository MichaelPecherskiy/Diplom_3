import allure
import routes
from pages.person_page import PersonalPage


class TestPersonalPage:

    @allure.title('Переход в Личный кабинет')
    @allure.description('Переход по клику на «Личный кабинет», переход в раздел «История заказов», выход из аккаунта.')
    def test_user_login(self, driver, create_ui_user):
        user_page = PersonalPage(driver)

        with allure.step('Открытие страницы Личного кабинета'):
            user_page.click_personal_page()

        with allure.step('Вход в систему с использованием учетных данных'):
            user_page.login_user(create_ui_user['email'], create_ui_user['password'])

        with allure.step('Проверка перехода на страницу Личного кабинета'):
            user_page.click_personal_page()
            assert user_page.get_current_url() == routes.URL_PROFILE

        with allure.step('Переход в раздел История заказов'):
            user_page.click_personal_page()
            user_page.click_history_order()
            assert user_page.get_current_url() == routes.URL_HISTORY

        with allure.step('Выход из аккаунта'):
            user_page.logout_from_account()
            assert user_page.get_current_url() == routes.URL_LOGIN

