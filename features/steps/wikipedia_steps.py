from behave import given, when, then
from pages.wikipedia_page import WikipediaPage
from selenium import webdriver

@given('I am on the Wikipedia home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://es.wikipedia.org")
    context.wikipedia_page = WikipediaPage(context.driver)

@when('I search for "{term}"')
def step_impl(context, term):
    context.wikipedia_page.search_article(term)

@then('I should see the article title "{expected_title}"')
def step_impl(context, expected_title):
    actual_title = context.wikipedia_page.get_article_title()
    assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"
    context.driver.quit()
