from faker import Faker
from routes import USER_REGISTER, USER_DELETE
from utils import register_user
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from routes import API_HOST

fake = Faker()


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    driver = None
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1200,1000")
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    elif request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1200")
        firefox_options.add_argument("--height=1000")
        driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.get(API_HOST)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def create_ui_user(valid_user_data, delete_user):
    """
    Фикстура для создания пользователя для UI тестов.
    Генерирует уникального пользователя, возвращает данные и токены, а затем удаляет пользователя после теста.
    """
    response = register_user(USER_REGISTER, valid_user_data)
    data = response.json()
    user_info = {
        "email": valid_user_data["email"],
        "password": valid_user_data["password"],
        "name": valid_user_data["name"],
        "accessToken": data["accessToken"],
        "refreshToken": data["refreshToken"]
    }

    yield user_info
    delete_user(user_info['accessToken'])


@pytest.fixture
def unique_email():
    """Генерирует уникальный email для тестов."""
    return fake.email()


@pytest.fixture
def valid_user_data(unique_email):
    """Возвращает корректные данные пользователя с уникальным email."""
    return {
        "email": unique_email,
        "password": fake.password(length=12),
        "name": fake.name()
    }


@pytest.fixture
def updated_user_data():
    """Возвращает новые данные для обновления пользователя."""
    return {
        "email": fake.email(),
        "password": fake.password(length=12),
        "name": fake.name()
    }


@pytest.fixture
def create_user_and_get_tokens(valid_user_data):
    """Создает пользователя и возвращает его accessToken и refreshToken."""
    response = register_user(USER_REGISTER, valid_user_data)
    data = response.json()
    tokens = {
        "accessToken": data["accessToken"],
        "refreshToken": data["refreshToken"]
    }
    return tokens


@pytest.fixture
def incomplete_user_data():
    """Возвращает данные пользователя с отсутствующими полями."""
    return [
        {"email": fake.email(), "name": fake.name()},
        {"password": fake.password(length=12), "name": fake.name()},
        {"email": fake.email(), "password": fake.password(length=12)}
    ]


@pytest.fixture
def delete_user():
    """Удаляет пользователя по его accessToken."""
    def _delete_user(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(USER_DELETE, headers=headers)

        assert response.status_code == 202
        assert response.json()["success"] is True
        assert response.json()["message"] == "User successfully removed"

    return _delete_user
