import pytest
import time
from base.Driver import Driver


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    objectDriver = Driver()
    driver = objectDriver.getDriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print('After Class')
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
