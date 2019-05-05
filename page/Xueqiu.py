#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-
from driver.Appium import Appium
from selenium.webdriver.common.by import By
from page.BasePage import BasePage
from page.Search import Search



class Xieqiu(BasePage):
    
    _search = (By.ID, "tv_search")
    
    def toSearch(self):
        self.find(self._search).click()
        return Search()