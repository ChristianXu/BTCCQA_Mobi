__author__ = 'sara'
import unittest
import logging
from time import sleep
from comm.common import DRIVER
from comm import get_element,get_elements
from comm import bsnsCommon
logger = logging.getLogger()


class TestAddDeleteWallets(unittest.TestCase):

    def setUp(self):

        #test start
        logger.info("Test add and delete wallets")


    def testAddDeleteWallets(self):
        # 如果登陆 先登出
        # if get_element("me", "me").is_exist():
        #     bsnsCommon.logout()
        #
        # bsnsCommon.login()

        while not get_element("Transactions", "Transactions").is_exist():
            sleep(1)

        get_element("wallets", "wallets").click()
        get_element("wallets", "wallets_icon").click()

        #添加下面钱包
        get_element("wallets","AZN").click()
        get_element("wallets", "AWG").click()
        get_element("wallets", "AMD").click()

        # bsnsCommon.delete_wallets(self.driver)

        # 添加wallet
        get_element("wallets", "wallets_add").click()


        # 判断wallet添加成功
        # w_list = ["AZN", "AWG", "AMD"]
        # wallets = get_element("wallets", "wallets").get_element_list()
        #
        # isAddOk = True
        #
        # isDeleteOk = True
        # name_list = []
        # for wallet in wallets:
        #     wallet_name = wallet.get_attribute("name")
        #     name_list.append(wallet_name)
        #
        # for w in w_list:
        #
        #     if w not in name_list:
        #         isAddOk = False
        #         break
        #
        # bsnsCommon.delete_wallets(self.driver)
        #
        # wallets = get_element("Transactions", "wallets").get_element_list()
        # name_list = []
        #
        # for wallet in wallets:
        #     wallet_name = wallet.get_attribute("name")
        #     name_list.append(wallet_name)
        #
        # for w in w_list:
        #
        #     if w in name_list:
        #         isDeleteOk = False
        #         break
        #
        # if isAddOk:
        #     self.log.write_result("Add wallet OK")
        # else:
        #     self.log.write_result("Add wallet NG")
        #
        # if isDeleteOk:
        #     self.log.write_result("Delete wallet OK")
        # else:
        #     self.log.write_result("Delete wallet NG")

    def tearDown(self):

        # TouchAction(self.driver).tap(x=28, y=40).perform()

        bsnsCommon.logout()
        # test end
        self.log.build_end_line("Test add wallets")