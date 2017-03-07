__author__ = 'apple'

import unittest
from comm import get_element
from comm import ReadConfig
from comm import bsnsCommon
from time import sleep
from comm import Log
from comm.bsnsCommon  import input_number

get_element = get_element


class TestSignIn(unittest.TestCase):

    def setUp(self):

        # test Start
        self.logger = Log.Logger(loglevel=1, logger="young").getlog()
        self.logger.info("Test Sign In Start")

    def test_sign_in(self):

        sleep(2)


        get_element("sign_in", "country_code").click()

        sleep(1)

        get_element("common", "clear").click()

        input_number("852")

        sleep(2)

        get_element("sign_in", "phone_number_input").click()

        get_element("common", "clear").click()

        input_number("64521324")

        sleep(3)

        get_element("sign_in", "next").click()

        sleep(5)

        if get_element("Login", "SMS_verification") is not None:
            input_number("214638")

        sleep(2)

        while not get_element("sign_in", "create_mobi_pin") is None:
            sleep(1)

        input_number("111111")

        sleep(3)

        input_number("111111")

        sleep(1)

        get_element("sign_in", "skip_slidder").click()

        self.check_sign_in()

    def check_login(self):

        if get_element("me", "me") is not None:
            self.logger.info("Sign in OK")
        else:
            self.logger.info("Sign in  NG")

        # action = TouchAction(self.driver)
        # action.press(5, 358).perform()

    def tearDown(self):
        # bsnsCommon.logout()
        # test end
        self.logger.info("Test sign in end")