import unittest

import pytest

from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.loginPage = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_openLoginPage(self):
        self.loginPage.clickLoginButton()
        expectedResult = "Login Page"
        actualResult = self.loginPage.getLoginPageTitle()
        assert actualResult == expectedResult, self.loginPage.takeScreenShot(self.loginPage.driver.current_activity)

    @pytest.mark.run(order=2)
    def test_loginFailed(self):
        self.loginPage.enterEmail("hendro@gmail.com")
        self.loginPage.enterPassword("1231231")
        self.loginPage.clickOnLogin()
        expectedResult = "Wrong CredentialsX"
        actualResult = self.loginPage.getWrongCredential()
        assert actualResult == expectedResult, self.loginPage.takeScreenShot(self.loginPage.driver.current_activity)

    @pytest.mark.run(order=3)
    def test_loginSuccess(self):
        self.loginPage.driver.back()
        self.loginPage.clickLoginButton()
        self.loginPage.enterEmail("admin@gmail.com")
        self.loginPage.enterPassword("admin123")
        self.loginPage.clickOnLogin()
        expectedResult = "Enter Admin"
        actualResult = self.loginPage.getAdminPageTitle()
        assert actualResult == expectedResult, self.loginPage.takeScreenShot(self.loginPage.driver.current_activity)