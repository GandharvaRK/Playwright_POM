import json

import pytest

from api_utils.API_Base_1 import API_utils
from playwright.sync_api import Playwright, expect

with open("C:/Users/gandhark/OneDrive - Capgemini/Playwright_PoC/Playwright_POM/data/credentials.json") as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.parametrize('user_credentials_1', user_credentials_list)
def test_e2e_web(playwright : Playwright, user_credentials_1):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()



    #Create order using API
    api_utils_1 = API_utils()
    order_id = api_utils_1.create_order(playwright)

    #Login to browser
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials_1["user_email"])
    page.locator("#userPassword").fill(user_credentials_1["password"])
    page.locator("#login").click()

    #Orders history page
    page.get_by_role("button",name="ORDERS").click()
    print(order_id)
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

