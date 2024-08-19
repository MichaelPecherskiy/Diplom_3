from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def click_on_element(self, locator, wait=None):
        if wait:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(wait))
        self.wait_and_find_element(locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_to_be(self, expected_url, time=20):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))

    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_attribute(self, locator, value):
        return self.find_element(locator).get_attribute(value)

    def drop_element(self, drag, drop):
        return ActionChains(self.driver).drag_and_drop(drag, drop).pause(1).perform()


    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_text_element_change(self, locator, value):
        self.find_element(locator)
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, value))

    def get_text_element(self, locator):
        return self.find_element(locator).text
