#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-


from appium.webdriver.common.mobileby import MobileBy
from page.BasePage import BasePage


class Search(BasePage):
    _search = (MobileBy.ID, "search_input_text")
    _user = (MobileBy.XPATH, "//*[@text='用户']")
    _username = (MobileBy.ID, "user_name")
    _stockName = (MobileBy.ID, "stockName")

    def search(self, keyword):
        self.find(self._search).send_keys(keyword)
        return self

    def getUserName(self):
        self.find(self._user).click()
        return self.findBy(self._username).text

    def getStocks(self):
        return self.find(self._stockName).text