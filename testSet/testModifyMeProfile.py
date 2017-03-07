__author__ = 'Apple'

import unittest
from time import sleep
import logging
import testSet as Log
from comm import get_element, get_elements
from comm import ReadConfig as readConfig
from comm.common  import clear_text
from comm import bsnsCommon
from comm import Log

get_element = get_element
get_elements = get_elements


class TestModifyMeProfile(unittest.TestCase):

    def setUp(self):

        # get Log
        self.logger = Log.Logger(loglevel=1, logger="young").getlog()

        self.phone_number = readConfig.get_value("config", "phoneNumber")
        self.pin = readConfig.get_value("config", "pin")

        # test Start
        self.logger.info("Test Modify Me Page")

    def testModifyMeProfile(self):

        sleep(2)
        # if get_element("me", "me") is not None:
        #     bsnsCommon.logout()

        # bsnsCommon.login()

        while get_element("me", "me") is None:
            sleep(1)

        get_element("me", "me").click()

        get_element("me", "avatar").click()

        get_element("me", "edit").click()

        modify_name_ele = get_element("me", "modify_name")
        modify_name_ele.click()
        modify_name_ele.clear()
        sleep(2)
        get_element('me', 'input_nickname').send_keys("Tset")

        first_name_ele = get_element('me', 'first_name')
        first_name_ele.click()
        first_name_ele.clear()
        first_name_ele.send_keys("Apple")

        last_name_ele = get_element('me', 'last_name')
        last_name_ele.click()
        last_name_ele.clear()
        last_name_ele.send_keys("Zou")

        home_address_ele = get_element('me', 'home_address')
        home_address_ele.click()
        home_address_ele.clear()
        home_address_ele.send_keys('Shanghai')

        get_element('me', 'country').click()
        get_element('me', 'choose_country').click()

        sleep(3)

        city_ele = get_element('me', 'city')
        city_ele.click()
        city_ele.clear()
        city_ele.send_keys('Xuhui district')


        sleep(2)

        postal_code_ele = get_element('me', 'postal_code')
        postal_code_ele.click()
        postal_code_ele.clear()
        postal_code_ele.send_keys('12345')

        get_element('me', 'save').click()

        #Back me home page
        get_element("me", "back").click()



    def tearDown(self):

        sleep(1)
        # bsnsCommon.logout()
        # test end
        self.logger.info("Test Modify Me Profile")
