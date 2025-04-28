from selenium.webdriver.common.by import By
from .base_page import BasePage

class WikipediaPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    ARTICLE_TITLE = (By.ID, "firstHeading")

    def search_article(self, term):
        self.enter_text(self.SEARCH_INPUT, term)
        self.driver.find_element(*self.SEARCH_INPUT).submit()

    def get_article_title(self):
        return self.find_element(self.ARTICLE_TITLE).text
