__author__ = 'Apple'

import unittest
import comm as common
# import testSet as Log
from comm.common import DRIVER
from comm.common import ReadConfig
from comm import bsnsCommon
from comm import get_element,get_elements
from time import sleep
from comm import Log

get_element = get_element
get_elements = get_elements


class TestSendByBitcoinAddress(unittest.TestCase):

    def setUp(self):

        # get Log
        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

        # self.number_phone = readConfigLocal.getConfigValue("phoneNumber")
        self.pin = ReadConfig.get_value("config", "pin")

        self.send_number = "18651205943"

        # self.send_address = "2MsdJWp6m1grhsiwbozFRWsxvk9P9wRHV4g"
        self.send_address = "mmWx45kSpUn7BCbVwJH1nPNqBqdUiEf2eJ"

        # test Start
        # self.log.build_start_line("Test send bitcoins")


    def test_send_by_bitcoin_address(self):

        while get_element("wallets", "wallets") is None:
            sleep(1)

        get_element("wallets", "send").click()

        get_element("wallets","bitcoin_address").click()

        sleep(2)

        get_elements("wallets", "bitcoin_address")[1].click()
        sleep(2)
        get_element("wallets", "bitcoin_address_input").send_keys(self.send_address)
        # sleep(1)
        # get_element("wallets","paste").click()

        get_element("common", "continue").click()

        self.send_numbers("151")

        get_element("common", "continue").click()

        #add message
        add_message_element = get_element("wallets","add_message")
        add_message_element.click()
        add_message_element.send_keys('Test whether or not the bitcoin address sent successfully')

        get_element("common", "continue").click()

        get_element("common", "confirm").click()

        bsnsCommon.input_number(self.pin)

        self.check_result("Send bitcoins with phone number succesffully")

        get_element("common", "close").click()



    def check_result(self, result_msg):

        if get_element("wallets", "transaction_successful") is not None:
            print('result_msg-==========================================-----------------------------------------------')
            self.logger.info(result_msg+" OK")
        else:
            self.logger.info(result_msg+" NG")



    def send_numbers(self, number):

        sleep(1)
        number_list = list(number)

        int_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        xpath = "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]" \
                "/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]" \
                "/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeButton[%s]"

        for a in number_list:
            if a == "0":
                s_xpath = xpath % "11"
                DRIVER.driver.element("xpath", s_xpath).click()
            if a in int_list:
                s_xpath = xpath % a
                DRIVER.driver.element("xpath", s_xpath).click()
            else:
                continue


    def tearDown(self):
        # bsnsCommon.logout()
        # test end
        self.logger.info("Test send bitcoins")