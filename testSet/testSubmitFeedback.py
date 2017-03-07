__author__ = 'sara'

import unittest
import logging
from comm import get_element
from comm import ReadConfig
from comm import bsnsCommon
from time import sleep
from comm import common
from comm import Log

logger = logging.getLogger()

get_element = get_element


class TestSubmitFeedback(unittest.TestCase):

    def setUp(self):

        # test Start
        logger.info("Test submit feedback!")


    def test_submit_feedback(self):

        sleep(5)

        get_element("me", "me").click()

        get_element("me", "Feedback").click()

        sleep(5)

        get_element("me", "Feedback_context").send_keys('What is this,it is really,i believe that everything will turn out fine. ')

        sleep(3)

        get_element("common", "submit").click()

        sleep(3)

        self.check_submit_success('Feedback submit successful')

        sleep(2)

        #点击左上角的返回按钮
        get_element("common", "upper_left_back").click()

    def check_submit_success(self,result_msg):

        if get_element("me", "Feedback_submit_successful") is not None:

            logger.info(result_msg + 'ok!')

            sleep(2)

            # Click close popup
            get_element("me", "close_feedback_success_popup").click()
        else:
            logger.info(result_msg + 'NG!')



    def tearDown(self):
        # bsnsCommon.logout()
        # test end
        logger.info("Test submit feedback end")