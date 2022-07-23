import unittest
import pytest
from pages.ContactFormPage import ContactFormPage
import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):
    log = cl.customLogger()

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.contactForm = ContactFormPage(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        name = "Hendro"
        self.contactForm.enterName(name)
        self.contactForm.enterEmail()
        self.contactForm.enterAddress()
        self.contactForm.enterPhone()
        self.contactForm.clickSubmitButton()
        expectedResult = "Name: HendroX"
        actualResult = self.contactForm.getSubmitResult()
        assert actualResult == expectedResult, self.contactForm.takeScreenShot(self.contactForm.driver.current_activity)

    @pytest.mark.run(order=1)
    def test_openContactForm(self):
        cl.allureLogs("App launched")
        self.contactForm.clickContactFormButton()
        expectedResult = "Contact Us form"
        actualResult = self.contactForm.getPageTitle()
        assert actualResult == expectedResult, self.contactForm.takeScreenShot(self.contactForm.driver.current_activity)
