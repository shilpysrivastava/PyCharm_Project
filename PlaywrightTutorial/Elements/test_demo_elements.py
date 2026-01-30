import time

from playwright.sync_api import Page


def test_textbox(page:Page):
    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").fill("Rahul")
    page.get_by_placeholder("name@example.com").fill("rahul@test.com")
    page.locator("#currentAddress").fill("test testing test testing")
    page.locator("#permanentAddress").fill("test testing test testing")
    page.get_by_role("button", name = "Submit").click()

def test_checkbox(page:Page):
    page.goto("https://demoqa.com/checkbox")
    # page.get_by_title("Toggle").first.click()
    # page.locator("label:has-text('Home')").check()
    page.get_by_title("Expand all").click()
    page.get_by_text("Notes").click()





