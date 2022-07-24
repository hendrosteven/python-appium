import unittest
import pytest
from pages.SomeValuePage import SomeValuePage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class SomeValueTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.someValuePage = SomeValuePage(self.driver)

    @pytest.mark.run(order=6)
    def test_openEnterSomeValuePage(self):
        self.someValuePage.clickEnterValueButton()
        expectedResult = "Enter some Value"
        actualResult = self.someValuePage.getPageTitle()
        assert actualResult == expectedResult, self.someValuePage.takeScreenShot(self.someValuePage.driver.current_activity)

    @pytest.mark.run(order=7)
    def test_enterSomeValue(self):
        expectedResult = "Hendro Steven"
        self.someValuePage.enterText(expectedResult)
        self.someValuePage.clickSubmitButton()
        actualResult = self.someValuePage.getPreviewText()
        assert actualResult == expectedResult, self.someValuePage.takeScreenShot(self.someValuePage.driver.current_activity)