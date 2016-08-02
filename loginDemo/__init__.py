# coding=UTF-8
__author__ = 'wangtao'
import unittest
import os
import glob
from appium import webdriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


success = True
class XcfAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.xiachufang'
        desired_caps['appActivity'] = '.activity.StartPageActivity'
        desired_caps['app'] = PATH('/Users/wangtao/xcf/testapk/xcf_testapk.apk')


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

loginPhoneNum = '15901549596'
loginPassword = '123456'


def tearDown(self):
    # end the session
    self.driver.quit()

def phoneNumLoginSuccess(self):
    ff = self.driver.find_element_by_id('tab_widget_content_self')
    if (ff != ''):
         ff.click()
    else:
        ff = self.driver.find_element_by_id('re_login_close')
        ff.click()
        ff = self.driver.find_element_by_id('tab_widget_content_self')
        ff.click()
        ff = self.driver.find_element_by_id('entrance_login')
        ff.click()













