from pytest_bdd import scenarios,given, when, then
from playwright.sync_api import sync_playwright
import pytest

scenarios('D:/Training/pytest_bdd_demo/features/login.feature')

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@given('the user is on the login page',target_fixture="page")
def user_on_login_page(page):
    page.goto('https://www.saucedemo.com/')
    print("Login page is opened")
    return page

@when('the user enters valid credentials',target_fixture="page")
def enter_valid_credentials(page):
    page.locator('input[name="user-name"]').fill('standard_user')
    page.locator('input[name="password"]').fill('secret_sauce')
    print("Valid credentials entered")
    return page 

@when('clicks the login button')
def click_login_button(page):
    page.locator("//input[@id='login-button']").click()
    print("Login button clicked")
    return page

@then('the user should be redirected to the dashboard page')
def verify_redirection_to_dashboard(page):
    assert page.url == 'https://www.saucedemo.com/inventory.html'
    print("User is redirected to the dashboard page")



