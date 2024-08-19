from faker import Faker
fake = Faker()
import requests




def unique_email():
    """Генерирует уникальный email для тестов."""
    return fake.email()


def register_user(base_url, user_data):
    return requests.post(base_url, json=user_data)



INGREDIENT_DETAILS = 'Детали ингредиента'
GRATE_ORDER = 'идентификатор заказа'
DONE_ORDER = 'Выполнен'
CONSTRUCTOR = 'Соберите бургер'
FEED_ORDER = 'Лента заказов'
INFO_ORDER = 'Cостав'
