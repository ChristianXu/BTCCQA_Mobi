__author__ = 'sara'
import unittest
import logging
from time import sleep
from comm.common import DRIVER
from comm import get_element,get_elements
from comm import bsnsCommon
from comm import Log


class TestDeleteWallets(unittest.TestCase):

    def setUp(self):

        self.logger = Log.Logger(loglevel=1, logger="young").getlog()
        #test  start
        self.logger.info("Test delete wallets")


    def tesDeleteWallets(self):
        # 如果登陆 先登出
        # if get_element("me", "me").is_exist():
        #     bsnsCommon.logout()
        #
        # bsnsCommon.login()


        get_element("wallets", "wallets").click()
        get_element("wallets", "edit").click()
        get_element("wallets", "minus_icon").click()


        #添加下面钱包
        get_element("wallets","AZN").click()
        get_element("wallets", "AWG").click()
        get_element("wallets", "AMD").click()


        # bsnsCommon.delete_wallets(self.driver)

        # 添加wallet
        get_element("wallets", "wallets_add").click()




    def tearDown(self):

        # TouchAction(self.driver).tap(x=28, y=40).perform()

        bsnsCommon.logout()
        # test end
        self.logger.info("Test delete wallets")