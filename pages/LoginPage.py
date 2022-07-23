from base.BasePage import BasePage
import utilities.CustomLogger as cl


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _loginButton = "com.code2lead.kwad:id/Login"
    _loginPageTitle = "Login Page"
    _enterEmail = "3"
    _enterPassword = "4"
    _clickLoginButton = "com.code2lead.kwad:id/Btn3"
    _wrongCredentialResult = "Wrong Credentials"
    _adminPageTitle = "Enter Admin"

    def clickLoginButton(self):
        self.clickElement(self._loginButton, "id")
        cl.allureLogs("Click on Login Button")

    def getLoginPageTitle(self):
        element = self.getElement(self._loginPageTitle, "text")
        cl.allureLogs("Get Login page Title: " + element.text)
        return element.text

    def enterEmail(self, inputEmail):
        self.sendText(inputEmail, self._enterEmail, "index")
        cl.allureLogs("Entered email")

    def enterPassword(self, inputPassword):
        self.sendText(inputPassword, self._enterPassword, "index")
        cl.allureLogs("Entered password")

    def clickOnLogin(self):
        self.clickElement(self._clickLoginButton, "id")
        cl.allureLogs("Clicked on Login button in Login Screen")

    def getWrongCredential(self):
        element = self.getElement(self._wrongCredentialResult, "text")
        cl.allureLogs("Get wrong credential text: " + element.text)
        return element.text

    def getAdminPageTitle(self):
        element = self.getElement(self._adminPageTitle, "text")
        cl.allureLogs("Get Admin page Title: " + element.text)
        return element.text
