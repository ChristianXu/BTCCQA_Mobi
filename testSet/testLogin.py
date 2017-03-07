__author__ = 'sara'

import unittest
from comm import get_element
from comm import ReadConfig
from comm import bsnsCommon
from time import sleep
from comm import Log

get_element = get_element


class TestLogin(unittest.TestCase):

    def setUp(self):

        self.number_phone = ReadConfig.get_value("config", "phoneNumber")

        self.pin = ReadConfig.get_value("config", "pin")

        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

        print(self.number_phone)

        # test Start
        self.logger.info("Test login (not first login)")

    def test_login(self):
        sleep(2)
        if get_element("me", "me") is not None:
            bsnsCommon.logout()

        bsnsCommon.login(self.number_phone,self.pin)

        while get_element("me", "me") is None:
            sleep(1)

        get_element("me", "me").click()

        phone_number = get_element("me", "user_phone").get_property("value")

        self.logger.info("phone_number ===========>"+phone_number)

        self.check_login(phone_number)

        # bcommon.logout()

    def check_login(self, number):
        value = number.replace(" ", "")

        if self.number_phone in value:
            self.logger.info("login OK")
        else:
            self.logger.info("login NG")

        # action = TouchAction(self.driver)
        # action.press(5, 358).perform()

    def tearDown(self):
        bsnsCommon.logout()
        # test end
        self.logger.info("Test login (not first login) end")