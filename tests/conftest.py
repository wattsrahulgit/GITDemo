import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def invokeBrowser(request):
    driver = webdriver.Chrome(executable_path="E:\\Code\PythonTestingSelenium\chromedriver.exe")
    # driver.get("https://www.saucedemo.com/")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
