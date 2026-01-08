from selenium import webdriver

from config.browser_options import chrome_options, firefox_options, edge_options


class BrowserFactory:

    @staticmethod
    def get_driver(browser_name, headless=False):

        browser = browser_name.lower()

        if browser == "chrome":
            return webdriver.Chrome(
                options=chrome_options(headless)
            )

        elif browser == "firefox":
            return webdriver.Firefox(
                options=firefox_options(headless)
            )

        elif browser == "edge":
            return webdriver.Edge(
                options=edge_options(headless)
            )

        else:
            raise ValueError(
                f"Browser '{browser_name}' is not supported"
            )
