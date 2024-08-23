from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.step('Базовый класс для работы со страницами')
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента по локатору')
    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, wait=None):
        if wait:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(wait))
        self.wait_and_find_element(locator).click()

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание изменения URL')
    def wait_for_url_to_be(self, expected_url, time=20):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))

    @allure.step('Ожидание и поиск элемента')
    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Получение атрибута элемента')
    def get_attribute(self, locator, value):
        return self.find_element(locator).get_attribute(value)

    @allure.step('Перетаскивание элемента')
    def drop_element(self, drag, drop):
        return ActionChains(self.driver).drag_and_drop(drag, drop).pause(1).perform()

    @allure.step('Отправка текста в элемент')
    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Ожидание изменения текста элемента')
    def wait_text_element_change(self, locator, value):
        self.find_element(locator)
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Получение текста элемента')
    def get_text_element(self, locator):
        return self.find_element(locator).text
