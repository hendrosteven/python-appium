from base.BasePage import BasePage
import utilities.CustomLogger as cl


class SomeValuePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _enterValueButton = "com.code2lead.kwad:id/EnterValue"
    _enterValueText = "com.code2lead.kwad:id/Et1"
    _submitButton = "com.code2lead.kwad:id/Btn1"
    _previewText = "com.code2lead.kwad:id/Tv1"
    _pageTitle = "Enter some Value"

    def clickEnterValueButton(self):
        self.clickElement(self._enterValueButton, "id")
        cl.allureLogs("Click on Enter Value Button")

    def enterText(self, inputText):
        self.sendText(inputText, self._enterValueText, "id")
        cl.allureLogs("Entered some text")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, "id")
        cl.allureLogs("Click on Submit Button")

    def getPreviewText(self):
        element = self.getElement(self._previewText, "id")
        cl.allureLogs("Get preview text: " + element.text)
        return element.text

    def getPageTitle(self):
        element = self.getElement(self._pageTitle, "text")
        cl.allureLogs("Get page title text: " + element.text)
        return element.text
