import allure
from routes import URL_FORGOT_PASSWORD, URL_RESSET_PASSWORD
from pages.person_page import PersonalPage


class TestRecoverPassword:
    @allure.title('Восстановление пароля')
    @allure.description(
        'Переход на страницу восстановления пароля, ввод почты и клик по кнопке "Восстановить". Проверка, что переход на страницу восстановления пароля происходит корректно, а также проверка активности поля ввода пароля при нажатии кнопки показать/скрыть пароль.')
    def test_password_recovery(self, driver):
        page = PersonalPage(driver)

        with allure.step('Переход на страницу восстановления пароля'):
            page.click_resset_password()  # Исправлено название метода на соответствующее
            assert page.get_current_url() == URL_FORGOT_PASSWORD, "URL страницы восстановления пароля неверный."

        with allure.step('Ввод почты и клик по кнопке "Восстановить"'):
            page.data_input_click_resset()  # Исправлено название метода на соответствующее
            assert page.get_current_url() == URL_RESSET_PASSWORD, "URL страницы подтверждения сброса пароля неверный."

        with allure.step('Проверка активности поля ввода пароля'):
            active_field = page.click_show_button()  # Проверка, что кнопка работает
            assert active_field.is_displayed(), "Поле ввода пароля неактивное после нажатия кнопки 'Показать пароль'."


