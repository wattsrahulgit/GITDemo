import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("invokeBrowser")
class BaseClass:

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
