import allure
import utils
from pages.main import MainPage


class TestMainPage:
    @allure.title('Проверка перехода на страницу "Конструктор"')
    @allure.description(
        'Кликаем на кнопку для перехода в Личный кабинет, затем нажимаем на кнопку "Конструктор". Проверяем, что на странице отображается блок "Соберите бургер".')
    def test_transition_to_constructor(self, driver):
        page = MainPage(driver)

        with allure.step('Переход на страницу Конструктор'):
            element = page.navigate_to_constructor()
            assert element.text == utils.CONSTRUCTOR, "Блок 'Соберите бургер' не найден на странице Конструктора."

        with allure.step('Переход на страницу Лента заказов'):
            element = page.navigate_to_order_feed()
            assert element.text == utils.FEED_ORDER, "Блок 'Лента заказов' не найден на странице Ленты заказов."

    @allure.title('Проверка всплывающего окна с деталями ингредиента')
    @allure.description(
        'Переход к Ленте заказов, клик по первому заказу, проверка наличия блока "Состав". Затем клик по ингредиенту и закрытие всплывающего окна. Проверяем, что всплывающее окно закрылось.')
    def test_check_popup_order_details(self, driver):
        page = MainPage(driver)

        with allure.step('Открытие детальной информации о заказе'):
            element = page.ingredient_detail()
            assert element.text == utils.INGREDIENT_DETAILS, "Блок с деталями ингредиента не найден."

        with allure.step('Закрытие всплывающего окна с деталями ингредиента'):
            page.close_ingredient_detail()
            assert 'opened' not in page.ingredient_info_closed(), "Всплывающее окно не закрылось."

    @allure.title('Проверка увеличения счетчика ингредиентов при добавлении в корзину')
    @allure.description(
        'Кликаем на ингредиент, перетаскиваем его в корзину и проверяем, что счетчик ингредиентов обновился.')
    def test_add_ingredient_to_cart(self, driver):
        page = MainPage(driver)

        with allure.step('Добавление ингредиента в корзину'):
            element = page.add_ingredient_to_order()
            assert element.text == str(2), "Счетчик ингредиентов не обновился должным образом."

    @allure.title('Создание заказа зарегистрированным пользователем')
    @allure.description(
        'Авторизация пользователя, добавление ингредиентов в заказ, оформление заказа и проверка поп-апа с подтверждением.')
    def test_create_order_as_logged_in_user(self, driver, create_ui_user):
        page = MainPage(driver)

        with allure.step('Открытие Личного кабинета и авторизация'):
            page.open_my_account()
            page.login_user(create_ui_user['email'], create_ui_user['password'])

        with allure.step('Добавление ингредиентов в заказ и оформление заказа'):
            page.add_ingredient_to_order()
            element = page.place_an_order()
            assert element.text == utils.GRATE_ORDER, "Поп-ап с подтверждением заказа не отображается должным образом."

