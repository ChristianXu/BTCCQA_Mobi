__author__ = 'sara'

import unittest
import logging
from comm import get_element
from comm import ReadConfig
from comm import bsnsCommon
from time import sleep
from comm import common

logger = logging.getLogger()

get_element = get_element


class TestChangeMobiPIN(unittest.TestCase):

    def setUp(self):

        self.pin = ReadConfig.get_value("config", "pin")

        self.phone_number = ReadConfig.get_value("config", "phoneNumber")

        # test Start
        logger.info("Test change mobi PIN")

        self.new_pin = '000000'

    def test_change_mobi_PIN(self):

        sleep(5)

        if get_element("me", "me") is not None:
            bsnsCommon.logout()

        sleep(1)

        print("=========================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        bsnsCommon.login(self.phone_number,self.pin)


        sleep(2)

        get_element("me", "me").click()

        get_element("me", "Settings").click()

        get_element("me", "change_mobi_PIN").click()

        common.input_number(self.pin)

        sleep(3)

        common.input_number(self.new_pin)

        sleep(3)

        common.input_number(self.new_pin)

        sleep(2)


        self.check_change_PIN_success()

    def check_change_PIN_success(self):

        sleep(1)

        get_element("me", "Sign_out").click()

        sleep(1)

        bsnsCommon.login(self.phone_number, self.new_pin)

    # def check_change_PIN_success(self, new_pin):
    #     get_element("me", "change_mobi_PIN").click()
    #
    #     common.input_number(self.new_pin)
    #
    #     sleep(3)
    #
    #     #修改成功之后再改回为原来的
    #     common.input_number(self.pin)
    #
    #     sleep(3)
    #
    #     common.input_number(self.pin)


    def tearDown(self):
        # bsnsCommon.logout()
        # test end
        logger.info("Test change mobi PIN end!")