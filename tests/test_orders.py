import allure
import utils
from pages.page_order import OrderPage


class TestOrder:

    @allure.title('Просмотр деталей заказа')
    @allure.description('Открываем ленту заказов, выбираем первый заказ и проверяем отображение его деталей.')
    def test_order_info(self, driver):
        with allure.step('Открыть ленту заказов и выбрать первый заказ'):
            order = OrderPage(driver)
            order_details = order.view_order_details()
        with allure.step('Проверить детали заказа'):
            assert order_details.text == utils.INFO_ORDER

    @allure.title('Проверка отображения заказа пользователя в ленте заказов')
    @allure.description('Авторизация пользователя, создание нового заказа, проверка его наличия в ленте заказов.')
    def test_order_from_history(self, driver, create_ui_user):
        with allure.step('Авторизация пользователя'):
            order = OrderPage(driver)
            order.click_personal_page()
            order.login_user(create_ui_user['email'], create_ui_user['password'])

        with allure.step('Создать новый заказ'):
            order_number = order.add_ingredient_and_place_order()

        with allure.step('Проверить наличие заказа в ленте заказов'):
            formatted_order_number = order_number.lstrip('0')
            assert formatted_order_number in order.get_orders_in_progress().lstrip('0')

    @allure.title('Проверка увеличения общего счётчика заказов')
    @allure.description('Авторизация, оформление заказа, проверка увеличения общего количества выполненных заказов.')
    def test_counter_all_time(self, driver, create_ui_user):
        with allure.step('Получить начальное количество выполненных заказов'):
            order = OrderPage(driver)
            initial_count = int(order.get_total_orders_all_time())

        with allure.step('Авторизация и создание нового заказа'):
            order.click_personal_page()
            order.login_user(create_ui_user['email'], create_ui_user['password'])
            order.add_ingredient_and_place_order()

        with allure.step('Проверить увеличение общего количества выполненных заказов'):
            new_count = int(order.get_new_order_number())
            assert new_count == initial_count + 1

    @allure.title('Проверка увеличения счётчика заказов за сегодня')
    @allure.description('Авторизация, создание нового заказа и проверка увеличения счётчика заказов за текущий день.')
    def test_counter_today(self, driver, create_ui_user):
        with allure.step('Получить начальное количество заказов за сегодня'):
            order = OrderPage(driver)
            initial_today_count = order.get_total_orders_today()

        with allure.step('Создать новый заказ'):
            order.click_personal_page()
            order.login_user(create_ui_user['email'], create_ui_user['password'])
            order.add_ingredient_and_place_order()

        with allure.step('Проверить увеличение счётчика заказов за сегодня'):
            new_today_count = int(order.get_total_orders_today())
            assert new_today_count == int(initial_today_count) + 1

    @allure.title('Появление нового заказа в списке "В работе"')
    @allure.description('Авторизация, создание нового заказа, проверка его появления в разделе "В работе".')
    def test_new_order_in_progress(self, driver, create_ui_user):
        with allure.step('Авторизация и создание нового заказа'):
            order = OrderPage(driver)
            order.click_personal_page()
            order.login_user(create_ui_user['email'], create_ui_user['password'])
            order_number = order.add_ingredient_and_place_order()
            formatted_order_number = order_number.lstrip('0')
        with allure.step('Проверить появление нового заказа в списке "В работе"'):
            assert formatted_order_number in order.get_orders_in_progress().lstrip('0')
