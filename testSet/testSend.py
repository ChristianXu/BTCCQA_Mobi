__author__ = 'sara'

import unittest
import comm as common
# import testSet as Log
from comm.common import DRIVER
from comm.common import ReadConfig
from comm import bsnsCommon
from comm import get_element,get_elements
from time import sleep
from comm import Log

# readConfigLocal = readConfig.ReadConfig()

get_element = get_element
get_elements = get_elements


class TestSend(unittest.TestCase):

    def setUp(self):

        # get Log
        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

        self.number_phone = ReadConfig.get_value("phoneNumber")
        self.pin = ReadConfig.get_value("config", "pin")
        self.send_number = "13285152140"
        # self.send_address = "2MsdJWp6m1grhsiwbozFRWsxvk9P9wRHV4g"
        self.send_address = "mmWx45kSpUn7BCbVwJH1nPNqBqdUiEf2eJ"

        # test Start
        self.logger.info("Test send bitcoins")


    def test_offchian_send(self):

        print('testSend method......................................................................................')
        sleep(2)
        # if get_element("me", "me") is not None:
        #     bsnsCommon.logout()
        #
        # bsnsCommon.login(self.number_phone,self.pin)

        while get_element("wallets", "wallets") is None:
            sleep(1)

        get_element("wallets", "send").click()

        get_element("wallets", "phone_number").click()

        sleep(1)

        get_element("wallets", "phone_input").send_keys(self.send_number)

        get_element("common", "continue").click()

        self.send_numbers("150")

        get_element("common", "continue").click()
        sleep(2)

        get_element("common", "continue").click()

        # get_elements("common", "send")[2].click()

        get_element("common", "confirm").click()

        bsnsCommon.input_number(self.pin)

        self.check_result("Send bitcoins with phone number succesffully")

        get_element("common", "close").click()



    def test_onchian_send(self):

        while get_element("wallets", "wallets") is None:
            sleep(1)

        get_element("wallets", "send").click()

        get_element("wallets", "phone_number").click()

        sleep(1)

        get_element("wallets", "phone_input").send_keys(self.send_number)

        get_element("common", "continue").click()

        self.send_numbers("150")

        get_element("common", "continue").click()
        sleep(2)

        get_element("common", "continue").click()

        if get_element("wallets","switch_onchian") is not None:

            get_element("wallets","switch_onchian").click()

            get_element("common", "confirm").click()

            bsnsCommon.input_number(self.pin)

            self.check_result("Send bitcoins with phone number succesffully via onchain")

            get_element("wallets", "Add Memo").click()

            memo_content = get_element("wallets", "Memo Content")
            memo_content.click()
            memo_content.send_keys('Give you bitcoin via bitcoin address')

            get_element('common', 'save').click()

        else:
            get_element("common", "confirm").click()

            bsnsCommon.input_number(self.pin)

            self.check_result("Send bitcoins with phone number succesffully via onchain")

            get_element("wallets","Add Memo").click()

            memo_content = get_element("wallets","Memo Content")
            memo_content.click()
            memo_content.send_keys('Give you bitcoin via bitcoin address')

            get_element('common','save').click()
        # get_element("common", "close").click()


    def check_result(self, result_msg):

        if get_element("wallets", "transaction_successful") is not None:

            self.logger.info(result_msg+" OK")
        else:
            self.logger.info(result_msg + " NG")



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