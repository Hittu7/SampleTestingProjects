import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig



import time
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3)
        time.sleep(2)
        act_title=self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(3)
        self.lp=LoginPage(self.driver)

        self.lp.setUserName(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False












