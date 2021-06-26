import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utlilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.enterPassword().send_keys("qwerty@123")
        homePage.selectCheckbox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitButton().click()

        message = homePage.successMessage().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param


