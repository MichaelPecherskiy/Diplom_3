import pytest
import allure
from routes import URL_FORGOT_PASSWORD, URL_RESSET_PASSWORD
from pages.person_page import PersonalPage


@pytest.mark.usefixtures("driver")
class TestRecoverPassword:

    @allure.title('Переход на страницу восстановления пароля')
    @pytest.mark.description('Переход на страницу восстановления пароля')
    def test_navigate_to_password_recovery_page(self, driver):
        page = PersonalPage(driver)
        page.click_resset_password()  # Исправлено название метода на соответствующее
        assert page.get_current_url() == URL_FORGOT_PASSWORD, "URL страницы восстановления пароля неверный."

    @allure.title('Ввод почты и переход на страницу подтверждения сброса пароля')
    @pytest.mark.description('Ввод почты и переход на страницу подтверждения сброса пароля')
    def test_email_input_and_reset(self, driver):
        page = PersonalPage(driver)
        page.data_input_click_resset()  # Исправлено название метода на соответствующее
        assert page.get_current_url() == URL_RESSET_PASSWORD, "URL страницы подтверждения сброса пароля неверный."

    @allure.title('Проверка активности поля ввода пароля после нажатия кнопки "Показать пароль"')
    @pytest.mark.description('Проверка активности поля ввода пароля после нажатия кнопки "Показать пароль"')
    def test_check_password_field_active(self, driver):
        page = PersonalPage(driver)
        active_field = page.click_show_button()  # Проверка, что кнопка работает
        assert active_field.is_displayed(), "Поле ввода пароля неактивное после нажатия кнопки 'Показать пароль'."



