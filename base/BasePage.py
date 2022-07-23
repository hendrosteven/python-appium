import time

import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.CustomLogger as cl


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorString, locatorType):
        locatorType = locatorType.lower()
        element = None

        if locatorType == "id":
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.ID, locatorString)))
            return element
        elif locatorType == "xpath":
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((MobileBy.XPATH, locatorString)))
            return element
        elif locatorType == "des":
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locatorString)))
            return element
        elif locatorType == "index":
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index(%d)' % int(locatorString))))
            return element
        elif locatorType == "text":
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorString)))
            return element
        else:
            self.log.info("Locator " + locatorString + " not found")

        return element

    def getElement(self, locatorString, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorString, locatorType)
            self.log.info(
                "Element found with locatorType " + locatorType + " and with locatorString " + locatorString)
        except:
            self.log.info(
                "Element not found with locatorType " + locatorType + " and with locatorString " + locatorString)

        return element

    def clickElement(self, locatorString, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorString, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with locatorType " + locatorType + " and with locatorString " + locatorString)
        except:
            self.log.info(
                "Unable to click on Element with locatorType " + locatorType + " and with locatorString " + locatorString)

        return element

    def sendText(self, text, locatorString, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorString, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text on Element with locatorType " + locatorType + " and with locatorString " + locatorString)
        except:
            self.log.info(
                "Unable to send text on Element with locatorType " + locatorType + " and with locatorString " + locatorString)

    def screenShot(self, screenshotName):
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        fileName = screenshotName + "_" + ts + ".png"
        directory = "../screenshots/"
        path = directory + fileName
        try:
            self.driver.save_screenshot(path)
            self.log.info("Screenshot save to path: " + path)
        except:
            self.log.info("Unable to save screenshot to path: " + path)

    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
