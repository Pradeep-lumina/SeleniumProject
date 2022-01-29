from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (4)\chromedriver.exe")


def testMethod(setup):
    driver.get("https://www.facebook.com/")


def testMethod1(setup):
    driver.get("https://www.gmail.com/")