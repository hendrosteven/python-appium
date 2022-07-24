import unittest
from tests.LoginTest import LoginTest
from tests.ContactFormTest import ContactFormTest
from tests.SomeValueTest import SomeValueTest

loginTest = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
contactFormTest = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
someValueTest = unittest.TestLoader().loadTestsFromTestCase(SomeValueTest)

testSuite = unittest.TestSuite([contactFormTest, loginTest, someValueTest])

unittest.TextTestRunner(verbosity=1).run(testSuite)
