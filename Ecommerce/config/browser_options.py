from selenium import webdriver


def chrome_options(headless=False):
    options = webdriver.ChromeOptions()

    # 🔹 Run with a fresh profile (MOST IMPORTANT)
    options.add_argument("--incognito")

    # 🔑 MUST-HAVE flags   # 🔹 Disable password & breach features via flags
    options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheckup")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")


    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_enabled": False,
        "password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)



    if headless:
        options.add_argument("--headless=new")

    return options


# ---------------- FIREFOX OPTIONS ----------------
def firefox_options(headless=False):
    options = webdriver.FirefoxOptions()

    # Disable notifications
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("dom.push.enabled", False)

    # Headless mode
    if headless:
        options.add_argument("--start-maximized")

    # Start maximized workaround for Firefox
    options.add_argument("--width=1920")


    return options

# ---------------- EDGE OPTIONS ----------------
def edge_options(headless=False):
    options = webdriver.EdgeOptions()

    # Disable automation infobar
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Disable notifications
    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    # Headless mode
    if headless:
        options.add_argument("--headless=new")

    # Start maximized
    options.add_argument("--start-maximized")

    return options