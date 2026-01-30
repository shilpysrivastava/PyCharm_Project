from playwright.sync_api import Page


def test_textbox(page:Page):
    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").fill("Rahul")
    page.get_by_placeholder("name@example.com").fill("rahul@test.com")
    page.locator("#currentAddress").fill("test testing test testing")
    page.locator("#permanentAddress").fill("test testing test testing")
    page.get_by_role("button", name = "Submit").click()
