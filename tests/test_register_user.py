from playwright.async_api import async_playwright
from pages.login_page import LoginPage
import pytest


@pytest.mark.asyncio
async def test_register_user():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            login_page = LoginPage(page)
            await login_page.homepage()
            await login_page.fill_name()
            await login_page.fill_email()
            await login_page.click_signup_button()
            await login_page.select_gender()
            await login_page.fill_password()
            await login_page.select_day()
            await login_page.select_month()
            await login_page.select_year()
            await login_page.click_newsletter()
            await login_page.click_optin()
            await login_page.fill_first_name()
            await login_page.fill_last_name()
            await login_page.fill_company()
            await login_page.fill_address1()
            await login_page.fill_address2()
            await login_page.select_country()
            await login_page.enter_state()
            await login_page.enter_city()
            await login_page.enter_zipcode()
            await login_page.enter_mobile_number()
            await login_page.create_account()
            await login_page.continue_button()
            await login_page.verify_username()
            await login_page.verify_delete_account()
            await login_page.verify_account_deleted()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()
