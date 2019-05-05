#! /user/bin/env pyhton3
# -*- coding: UTF-8 -*-

from appium import webdriver

class Appium(object):

    driver = None
    "@type driver: WebDriver"

    @classmethod
    def getDriver(cls):
        return cls.driver

    @classmethod
    def initDriver(cls):
        print("setup")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyboard"] = "true"  # 使用unicode编码方式发送字符串
        caps["resetKeyboard"] = "true"  # 隐藏键盘

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
