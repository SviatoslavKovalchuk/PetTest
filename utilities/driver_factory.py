from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int, is_headless=False):
        if int(driver_id) == DriverFactory.CHROME:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        elif int(driver_id) == DriverFactory.FIREFOX:
            firefox_options = FirefoxOptions()
            if is_headless:
                firefox_options.add_argument("--headless")
            driver = Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        elif int(driver_id) == DriverFactory.EDGE:
            edge_options = EdgeOptions()
            if is_headless:
                edge_options.add_argument("--headless")
            driver = Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
        else:
            driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver

