from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# def newbrowser(headless=False, detached=False):
#     options = Options()
#     if headless:
#         options.add_argument("--headless")

#     if detached:
#         options.add_experimental_option("detach", True)
    
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     return driver

class newbrowser:
    def __init__(self, headless=False, detached=True):
        self.options = Options()
        if headless:
            self.options.add_argument("--headless")

        if detached:
            self.options.add_experimental_option("detach", True)

    def getdriver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        return self.driver

    def find_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_by_linktext(self, text):
        return self.driver.find_element(By.LINK_TEXT, text)

    def find_element_by_name(self, name):
        return self.driver.find_element(By.NAME, name)

    def find_element_by_css(self, select):
        return self.driver.find_element(By.CSS_SELECTOR, select)

    def find_element_by_class(self, _class):
        return self.driver.find_element(By.CLASS_NAME, _class)