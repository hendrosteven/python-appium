import time

from base.Driver import Driver
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from pages.ContactFormPage import ContactFormPage

objectDriver = Driver()
log = cl.customLogger()


driver = objectDriver.getDriver()
log.info("Launching Apps")

# bp = BasePage(driver)
# bp.clickElement('ENTER SOME VALUE', 'text')
# time.sleep(3)
# bp.sendText('Welcome to Appium', 'com.code2lead.kwad:id/Et1', 'id')
# bp.clickElement('com.code2lead.kwad:id/Btn1', 'id')
#
# bp.screenShot(driver.current_activity)

cf = ContactFormPage(driver)
cf.clickContactFormButton()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterPhone()
cf.clickSubmitButton()