#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-

from appium import webdriver
import unittest
from driver.Appium import Appium
from page.Xueqiu import Xieqiu


class TestXueqiu(unittest.TestCase):

    def setUp(self):
        Appium.initDriver()
        print(Appium.driver)

    def test_search(self):
        assert Xieqiu().toSearch().search("pdd").getStocks() == "拼多多"



    def test_search_username(self):
        assert Xieqiu().toSearch().sourch("Mickey").getStocks() == "Mickey"
