from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def test_charge():
    driver = webdriver.Chrome(executable_path="E:\\Code\PythonTestingSelenium\chromedriver.exe")
    driver.get("https://www.saucedemo.com/")

    #list1 = []
    list = driver.find_elements_by_xpath("//div[@id='login_credentials']/br")
    #list1.append(driver.find_elements_by_xpath("//div[@id='login_credentials']/br").text)
    print(len(list))

    driver.find_element_by_css_selector("#user-name").send_keys("standard_user")
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
