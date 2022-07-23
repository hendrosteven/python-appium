from appium import webdriver


class Driver:
    def getDriver(self):
        caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '10',
            'deviceName': 'emulator-5554',
            'app': '/Users/jarvis/Documents/training/online/appium/Android_Demo_App.apk',
            'appPackage': 'com.code2lead.kwad',
            'appActivity': 'com.code2lead.kwad.MainActivity'
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        return driver
