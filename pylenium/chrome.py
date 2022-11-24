from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        
        