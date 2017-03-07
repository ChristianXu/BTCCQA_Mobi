__author__ = 'Apple'

import unittest
import logging
from time import sleep
from comm import get_element, get_elements
from comm.common import ReadConfig
from comm import bsnsCommon
from comm import Log

get_element = get_element
get_elements = get_elements

logger = logging.getLogger()

class TestReceive(unittest.TestCase):

    def setUp(self):

        self.number_phone = ReadConfig.get_value("config", "phoneNumber")

        self.pin = ReadConfig.get_value("config", "pin")

        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

        # test Start
        self.logger.info("Test receive bitcoins")

    def testReceive(self):

        isOk = True
        # 如果登陆 先登出
        # if get_element("me", "me").is_exist():
        #     bsnsCommon.logout()
        #
        # bsnsCommon.login(self.number_phone, self.pin)
        sleep(3)

        while get_element("wallets", "wallets") is None:
            sleep(1)

        get_element("wallets", "wallets").click()

        get_element("wallets", "receive").click()

        sleep(3)
        phone_number = get_element("wallets", "phone_number").get_attribute("value").replace(" ", "")

        # qr_code = get_element("wallets", "qr_code")

        if self.number_phone not in phone_number:
            self.logger.info("phone number is not show")
            isOk = False

        if get_element("wallets", "qr_code").is_displayed():
            self.logger.info("qr code is not show")
            print('qr code is show')
            isOk = False

        if get_element("wallets", "private_key").is_displayed():
        # if not get_element("Transactions", "bitcoin_address").is_exist():
            self.logger.info("bitcoin address is not show")
            print('bitcoin address is  show')
            isOk = False

        if isOk:
            self.logger.info("receive bitcoins OK")
        else:
            self.logger.info("receive bitcoins NG")


    def tearDown(self):
        pass

        # TouchAction(self.driver).tap(x=28, y=40).perform()
        # bcommon.logout()
        # test end
        self.logger.info("Test receive bitcoins")