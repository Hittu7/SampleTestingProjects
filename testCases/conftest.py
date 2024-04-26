from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    #service = Service()
    #options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(service=service, options=options)
    #driver = webdriver.Chrome(executable_path='C:/Users/Hitesh/PycharmProjects/nopcommerce_backend_project/chromedriver_win32 (4)/chromedriver.exe')
    return driver

