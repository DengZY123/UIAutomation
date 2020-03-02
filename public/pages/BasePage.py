import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config.config import Config

class BasePage():

    # 加载配置文件
    profile = webdriver.FirefoxProfile(Config.profile_path)

    def __init__(self):
        try:
           self.driver = webdriver.Firefox(firefox_profile=self.profile)
        except Exception:
            raise NameError("no firefox")


    def open(self,url):
        print(url)
        if url != "":
            self.driver.get(url)
        else:
            raise ValueError("pleast input a url")

    def findElement(self,value,type="xpath"):
        driver = self.driver
        try:
            if type == "xpath":
                elem = driver.find_element_by_xpath(value)
            elif type == "css":
                elem = driver.find_element_by_css(value)
        except Exception:
            raise NameError("This element not found"+str(value))
        return elem

    def click(self,element):
        element.click()

    def type(self,element,text):
        element.send_keys(text)

    def move(self,element):
        Action = ActionChains(self.driver)
        Action.move_to_element(element).perform()

    def move_offset(self,element,x,y):
        Action = ActionChains(self.driver)
        Action.move_to_element_with_offset(element,x,y).perform()

    def move_and_clcik(self,element):
        Action = ActionChains(self.driver)
        Action.move_to_element(element).perform()
        Action.move_by_offset(-139,222)
        Action.move_by_offset(-100, 0)
        Action.move_by_offset(0, 30)
        Action.click()
        Action.perform()


    def quit(self):
        self.driver.quit()