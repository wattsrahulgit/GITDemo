from datetime import time

import pytest
from selenium import webdriver

from pageObject.HomePage import HomePage
from tests.conftest import invokeBrowser
from utlilities.BaseClass import BaseClass


class TestOne():
    def test_loginPage(self):
        driver = webdriver.Chrome(executable_path="E:\\Code\PythonTestingSelenium\chromedriver.exe")
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element_by_css_selector("#user-name").send_keys("standard_user")
        # driver.find_element_by_css_selector("#user-name").send_keys("standard_user")
        driver.find_element_by_css_selector("#password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
        driver.implicitly_wait(4)

        products = driver.find_elements_by_xpath("//div[@class='inventory_item_name']")

        for product in products:
            if product.text == "Sauce Labs Backpack":
                product.click()
                break

        button = driver.find_element_by_css_selector("[class*='btn_inventory']")
        button.click()

        driver.find_element_by_css_selector(".shopping_cart_link").click()

        cartItem = driver.find_element_by_css_selector("div[class=inventory_item_name]")
        print(cartItem.text)
        driver.find_element_by_css_selector("#checkout").click()
        driver.find_element_by_css_selector("#first-name").send_keys("XYZ")
        driver.find_element_by_xpath("//input[@id='last-name']").send_keys("ABC")
        driver.find_element_by_id("postal-code").send_keys("132663")
        driver.find_element_by_css_selector("#continue").click()
        # time.sleep(3)
        driver.find_element_by_css_selector("#finish").click()




