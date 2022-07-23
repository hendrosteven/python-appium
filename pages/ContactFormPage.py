from base.BasePage import BasePage
import utilities.CustomLogger as cl

class ContactFormPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators in contact form page
    _contactFormButton = "com.code2lead.kwad:id/ContactUs"
    _pageTitle = "Contact Us form"
    _enterName = "com.code2lead.kwad:id/Et2"
    _enterEmail = "com.code2lead.kwad:id/Et3"
    _enterAddress = "com.code2lead.kwad:id/Et6"
    _enterPhone = "com.code2lead.kwad:id/Et7"
    _submitButton = "com.code2lead.kwad:id/Btn2"
    _resultName = "com.code2lead.kwad:id/Tv2"

    def clickContactFormButton(self):
        self.clickElement(self._contactFormButton, "id")
        cl.allureLogs("Click on Contact Us Form Button")

    def enterName(self, name):
        self.sendText(name, self._enterName, "id")
        cl.allureLogs("Enter name")

    def enterEmail(self):
        self.sendText("hendro.steven@gmail.com", self._enterEmail, "id")
        cl.allureLogs("Enter email")

    def enterAddress(self):
        self.sendText("Jakarta", self._enterAddress, "id")
        cl.allureLogs("Enter address")

    def enterPhone(self):
        self.sendText("123456",self._enterPhone, "id")
        cl.allureLogs("Enter phone")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, "id")
        cl.allureLogs("Clicked on submit button")

    def getSubmitResult(self):
        element = self.getElement(self._resultName, "id")
        cl.allureLogs("Get submit result: "+ element.text)
        return element.text

    def getPageTitle(self):
        element = self.getElement(self._pageTitle, "text")
        cl.allureLogs("Get page title: "+ element.text)
        return element.text

