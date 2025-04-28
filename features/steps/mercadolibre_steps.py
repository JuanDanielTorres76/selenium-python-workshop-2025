from behave import given, when, then
from selenium import webdriver
from pages.mercadolibre_page import MercadoLibrePage

@given('I am on the MercadoLibre home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.mercadolibre.com.co")
    context.mercadolibre_page = MercadoLibrePage(context.driver)

@when('I search for the product "{product_name}"')
def step_impl(context, product_name):
    context.mercadolibre_page.search_product(product_name)

@then('I should see results containing the word "{word}"')
def step_impl(context, word):
    titles = context.mercadolibre_page.get_all_product_titles()
    assert any(word.lower() in title.lower() for title in titles), f"No results containing '{word}' were found."
    context.driver.quit()
