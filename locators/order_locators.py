from selenium.webdriver.common.by import By


class Order:
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed']")  # Ссылка на Ленту заказов
    FIRST_ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'OrderHistory_dataBox')]")  # Первый элемент в списке заказов
    ORDER_DETAILS_TEXT = (By.XPATH, "//div[contains(@class,'Modal_orderBox')]/p[contains(@class, 'main-medium')]")  # Текст деталей заказа
    ACTIVE_ORDER_ITEM = (By.XPATH, "(//ul[contains(@class,'orderList')]/li[contains(@class,'default')])[1]")  # Заказ, находящийся в процессе выполнения
    ORDER_PRICE_DISPLAY = (By.XPATH, "//h2[contains(@class,'title_shadow')]")  # Отображение цены оформленного заказа
    ORDER_NUMBER_DISPLAY = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")  # Отображение номера заказа
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_type_primary')]")  # Кнопка для оформления заказа
    TOTAL_ORDERS_COUNT = (By.XPATH, "//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]")  # Общее количество заказов за все время
    TODAY_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")  # Количество заказов за сегодняшний день
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]")  # Кнопка закрытия модального окна
