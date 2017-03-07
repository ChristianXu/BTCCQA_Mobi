__author__ = 'apple zou'

import unittest
import logging
from comm import get_element
from comm import ReadConfig
from comm import bsnsCommon
from time import sleep
from comm.common import input_number
from comm import Log

get_element = get_element


class TestForgetPin(unittest.TestCase):

    def setUp(self):

        self.number_phone =  ReadConfig.get_value("config","phoneNumber")
        self.pin = ReadConfig.get_value("config", "pin")
        self.new_phone_number = "18657405943"

        # test Start
        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

    #老用户老设备
    def test_forget_pin(self):

        sleep(2)
        if get_element("me", "me") is not None:
            bsnsCommon.logout()

        get_element("Login", "next").click()

        sleep(3)

        get_element("forget_pin", "forget_pin").click()

        while not get_element("forget_pin", "sms_code_verification") is None:
            sleep(1)

        sleep(2)

        if get_element("forget_pin", "sms_code_verification") is not None:
            input_number("214638")


        while not get_element("forget_pin", "create_new_mobi_PIN") is None or not get_element("forget_pin", "mobi_pin") is None:
            sleep(1)

        if get_element("forget_pin", "create_new_mobi_PIN") is not None:
            input_number("000000")

        sleep(2)

        if get_element("forget_pin", "confirm_new_mobi_PIN") is not None:
            input_number("000000")

        sleep(2)

        self.check_result("Forget PIN")

    #新用户新设备
    def test_newdev_forget_pin(self):

        sleep(2)

        get_element("common", "clear").click()

        input_number("13800001235")

        #Start Set
        get_element("forget_pin", "start_reset").click()

        get_element("forget_pin", "reset_now").click()

        if get_element("forget_pin", "sms_code_verification") is not None:
            input_number("214638")

        while not get_element("forget_pin", "create_new_mobi_PIN") is None or not get_element("forget_pin", "mobi_pin") is None:
            sleep(1)

        if get_element("forget_pin", "create_new_mobi_PIN") is not None:
            input_number("000000")

        sleep(2)

        if get_element("forget_pin", "confirm_new_mobi_PIN") is not None:
            input_number("000000")

        self.check_result("new user and new device forget PIN")


    def check_result(self, result_msg):

        if get_element("me", "me") is not None:
            self.logger.info(result_msg+" OK")
        else:
            self.logger.info(result_msg+" NG")




    def tearDown(self):

        self.logger.info("Forget PIN end!")