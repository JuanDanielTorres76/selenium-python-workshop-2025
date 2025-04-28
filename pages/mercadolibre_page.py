from selenium.webdriver.common.by import By
from .base_page import BasePage

class MercadoLibrePage(BasePage):
    SEARCH_INPUT = (By.NAME, "as_word")
    PRODUCT_TITLES = (By.XPATH, "//h2[contains(@class, 'ui-search-item__title')]")

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.driver.find_element(*self.SEARCH_INPUT).submit()

    def get_all_product_titles(self):
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [element.text for element in elements]
