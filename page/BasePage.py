#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from driver.Appium import Appium



class BasePage(object):
    black_words = ["//*[@text='好的']"]
    def findBy(self, by=By.ID, value=None):
        try:
            return Appium.getDriver().find_element(by, value)
        except:
            for w in self.black_words:
                elements = Appium.getDriver().find_element(By.XPATH, w)
                if len(elements) > 0:
                    elements[0].click()
                    return Appium.getDriver().find_element(by, value)


    def find(self, locate):
        return self.findBy(*locate)
