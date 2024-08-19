from selenium.webdriver.common.by import By


class Main:
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка для перехода в Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "(//p[contains(@Class, 'AppHeader_header')])[1]")  # Кнопка для перехода в Конструктор
    BUILD_BURGER_TEXT = (By.XPATH, "//section[contains(@class, 'ingredients')]/h1[contains(@class ,'type_main')]")  # Заголовок "Соберите Заказ"
    ORDER_TRACKING_BUTTON = (By.XPATH, "//a[@href='/feed']")  # Кнопка для перехода в Ленту заказов
    ORDER_FEED_HEADER = (By.XPATH, "//div[contains(@class ,'OrderFeed' )]/h1[contains(@class,'type_main')]")  # Заголовок "Лента заказов"
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient')]/img[contains(@class,'ingredient__image')])[1]") # Первый элемент в списке ингредиентов
    BASKET_ITEM = (By.XPATH, "(//section[contains(@class, 'BurgerConstructor_basket')]//li)[1]") # Локатор "корзины"
    INGREDIENT_COUNT = (By.XPATH, ".//a[@href= '/ingredient/61c0c5a71d1f82001bdaaa6d']/div/p[contains(@class, 'counter')]")  # Количество ингредиента в корзине
    INGREDIENT_DETAILS_HEADER = (By.XPATH,"(//div[contains(@class ,'Modal_modal')]/h2[contains(@class,'Modal_modal')])[1]")  # Заголовок окна деталей ингредиента
    CLOSE_MODAL_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]")  # Кнопка закрытия окна деталей
    INGREDIENT_DETAILS_WINDOW = (By.XPATH,"(//section[contains(@class,'Modal_modal')])[1]")  # Окно деталей ингредиента
    SUBMIT_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button')]")  # Кнопка подтверждения заказа
    ORDER_CONFIRMATION_TEXT = (By.XPATH, "//div[contains(@class,'contentBox')]/p[contains(@class ,'undefined')]")  # Поп-ап подтверждения заказа
