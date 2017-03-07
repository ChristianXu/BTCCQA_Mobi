__author__ = 'sara'

import unittest
from time import sleep
from testSet.testSend import TestSend

# from testSet import MyDriver
import testSet as Log
from comm import get_element, get_elements
from comm.common import ReadConfig
from comm import Log
# import testSet as bcommon

# readConfigLocal = readConfig.ReadConfig()

get_element = get_element
get_elements = get_elements


class TestConvert(unittest.TestCase):

    def setUp(self):
        # get Log
        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

        self.number_phone =  ReadConfig.get_value("config","phoneNumber")
        self.pin = ReadConfig.get_value("config", "pin")

        # test Start
        self.logger.info("Test convert")

    def testConvert(self):

        # sleep(2)
        # if get_element("me", "me") is not None:
        #     bcommon.logout()
        #
        # bcommon.login()

        while get_element("wallets", "wallets") is None:
            sleep(1)

        get_element("wallets", "convert").click()

        sleep(2)

        TestSend.send_numbers("123")
        # on_enter_amount_element = get_element("convert","on_enter_amount")
        # on_enter_amount_element.click()
        # on_enter_amount_element.send_keys(15)


        # get_element("wallets", "icon_convert").click()

        # while not get_element("comm", "confirm").is_enabled():
        sleep(2)

        get_element("common", "confirm").click()
        sleep(1)

        self.check_result("convert bits to cny")

        get_element("comm", "close").click()

    def check_result(self, result_msg):

        if get_element("wallets", "conversion_successful") is not None:
            print('result_msg-==========================================-----------------------------------------------')
            # self.log.write_result(result_msg+" OK")
        else:
            pass
            # self.log.write_result(result_msg+" NG")




    def tearDown(self):
        # test end
        self.logger.info("Test convert end")
