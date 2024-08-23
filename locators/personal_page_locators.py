from selenium.webdriver.common.by import By


class Login:
    ACCOUNT_PAGE_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка для перехода в Личный кабинет
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")  # Поле для ввода email при авторизации
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@type, 'password')]")  # Поле для ввода пароля
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(@class, 'button')]")  # Кнопка для входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href= '/forgot-password']")  # Ссылка на восстановление пароля
    RECOVER_BUTTON = (By.XPATH, "//button[contains(@Class, 'button_button')]")  # Кнопка для восстановления пароля
    TOGGLE_PASSWORD_VISIBILITY_BUTTON = (By.XPATH,"//div[contains(@class,'input__icon-action')]")  # Кнопка для показа пароля
    ACTIVE_INPUT_FIELD = (By.XPATH, "//div[@class ='input__container']/div[contains( @class,'input_status_active')]")  # кнопка активного поля ввода
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")  # Кнопка Истории заказов в личном кабинете
    ORDER_HISTORY = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")  # Ссылка на Историю заказов в Личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "(//button[contains(@class,'Account_button')])")  # Кнопка выхода из личного кабинета
