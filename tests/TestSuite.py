import unittest
from tests.LoginTest import LoginTest
from tests.ContactFormTest import ContactFormTest

loginTest = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
contactFormTest = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)

testSuite = unittest.TestSuite([contactFormTest, loginTest])

unittest.TextTestRunner(verbosity=1).run(testSuite)
