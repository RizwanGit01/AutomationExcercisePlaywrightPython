from playwright.async_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def homepage(self):
        await self.page.goto("https://automationexercise.com/")
        await self.page.wait_for_load_state("load")
        await expect(self.page).to_have_url("https://automationexercise.com/")
        await expect(self.page.locator("//span[normalize-space()='Automation']").nth(1)).to_have_text("Automation")
        await self.page.locator("//a[normalize-space()='Signup / Login']").click()
        new_user_signup = await self.page.text_content("//h2[normalize-space()='New User Signup!']")
        assert new_user_signup == "New User Signup!"

    async def fill_name(self):
        await self.page.locator("//input[@placeholder='Name']").fill("zephyr")
        await expect(self.page.locator("//input[@placeholder='Name']")).to_have_value("zephyr")

    async def fill_email(self):
        await self.page.locator("//input[@data-qa='signup-email']").fill("zephyr@gmail.com")
        await expect(self.page.locator("//input[@data-qa='signup-email']")).to_have_value("zephyr@gmail.com")

    async def click_signup_button(self):
        await self.page.locator("//button[normalize-space()='Signup']").click()

    async def select_gender(self):
        await self.page.locator("//input[@id='id_gender1']").click()
        await expect(self.page.locator("//input[@id='id_gender1']")).to_be_checked()

    async def fill_password(self):
        await self.page.locator("//input[@id='password']").fill("1234")
        await expect(self.page.locator("//input[@id='password']")).to_have_value("1234")

    async def select_day(self):
        await self.page.locator("//select[@id = 'days']").select_option("1")
        await expect(self.page.locator("//select[@id = 'days']")).to_have_value("1")

    async def select_month(self):
        await self.page.locator("//select[@id = 'months']").select_option("1")
        await expect(self.page.locator("//select[@id = 'months']")).to_have_value("1")

    async def select_year(self):
        await self.page.locator("//select[@id = 'years']").select_option("1990")
        await expect(self.page.locator("//select[@id = 'years']")).to_have_value("1990")

    async def click_newsletter(self):
        await self.page.locator("//input[@id = 'newsletter']").click()
        await expect(self.page.locator("//input[@id = 'newsletter']")).to_be_checked()

    async def click_optin(self):
        await self.page.locator("//input[@id = 'optin']").click()
        await expect(self.page.locator("//input[@id = 'optin']")).to_be_checked()

    async def fill_first_name(self):
        await self.page.locator("//input[@id = 'first_name']").fill("test")
        await expect(self.page.locator("//input[@id = 'first_name']")).to_have_value("test")

    async def fill_last_name(self):
        await self.page.locator("//input[@id = 'last_name']").fill("test")
        await expect(self.page.locator("//input[@id = 'last_name']")).to_have_value("test")

    async def fill_company(self):
        await self.page.locator("input[id = 'company']").fill("test company")
        await expect(self.page.locator("input[id = 'company']")).to_have_value("test company")

    async def fill_address1(self):
        await self.page.locator("//input[@id = 'address1']").fill("123 Main St")
        await expect(self.page.locator("//input[@id = 'address1']")).to_have_value("123 Main St")

    async def fill_address2(self):
        await self.page.locator("//input[@id = 'address2']").fill("Rancho Cucamonga")
        await expect(self.page.locator("//input[@id = 'address2']")).to_have_value("Rancho Cucamonga")

    async def select_country(self):
        await self.page.locator("//select[@id = 'country']").select_option("United States")
        await expect(self.page.locator("//select[@id = 'country']")).to_have_value("United States")
    
    async def enter_state(self):
        await self.page.locator("//input[@id = 'state']").fill("CA")
        await expect(self.page.locator("//input[@id = 'state']")).to_have_value("CA")
    async def enter_city(self):
        await self.page.locator("//input[@id = 'city']").fill("Los Angeles")
        await expect(self.page.locator("//input[@id = 'city']")).to_have_value("Los Angeles")
    async def enter_zipcode(self):
        await self.page.locator("//input[@id = 'zipcode']").fill("90038")
        await expect(self.page.locator("//input[@id = 'zipcode']")).to_have_value("90038")
    async def enter_mobile_number(self):
        await self.page.locator("//input[@id = 'mobile_number']").fill("1234567890")
        await expect(self.page.locator("//input[@id = 'mobile_number']")).to_have_value("1234567890")

    async def create_account(self):
        await self.page.locator("//button[@data-qa = 'create-account']").click()
        await expect(self.page).to_have_url("https://automationexercise.com/account_created")
        account_created = await self.page.text_content("//h2[normalize-space()='Account Created!']")
        assert account_created == "Account Created!"
        await expect(self.page).to_have_title("Automation Exercise - Account Created")

    async def continue_button(self):
        await self.page.locator("//a[@data-qa = 'continue-button']").click()
        await expect(self.page).to_have_url("https://automationexercise.com/")

    async def verify_username(self):
        username = await self.page.text_content("//b[normalize-space()='zephyr']")
        assert username == "zephyr"
    
    async def verify_delete_account(self):
        await self.page.locator("//a[normalize-space()='Delete Account']").click()
        await expect(self.page).to_have_url("https://automationexercise.com/delete_account")

    async def verify_account_deleted(self):
        account_deleted = await self.page.text_content("//b[normalize-space()='Account Deleted!']")
        assert account_deleted == "Account Deleted!"
        await self.page.locator("//a[normalize-space()='Continue']").click()
        await expect(self.page).to_have_url("https://automationexercise.com/")
    
