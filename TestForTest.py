import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as ec  # available since 2.26.0
from selenium.webdriver.support.ui import Select


class LoginTest(object):
    def __init__(self):
        self.start_time = "2017-07-28 09:30:00"
        os.environ["PATH"] = os.getcwd() + '\\Resource\;' + os.environ["PATH"]
        self.buy_list = [
            u"太湖淡水银鱼150g*2份超特惠",
            u"东来顺老北京正宗羊蝎子500g（全部都是肉！香喷喷食肉动物最爱！）",
            u"【C水果特惠】墨西哥进口牛油果4个装"
        ]

    def loop_action(self):
        driver = webdriver.Chrome()
        self.login(driver)

        for item in self.buy_list:
            self.select_item(driver, item)
            while True:
                if time.strftime('%Y-%m-%d %X', time.localtime()) >= self.start_time:
                    self.get_data(driver)
                    break
                print(time.clock())
                time.sleep(0.1)

        driver.quit()

    @staticmethod
    def login(driver):
        driver.get("http://116.247.104.75:3033/Login.aspx")
        driver.find_element_by_id("ctl00_MainContent_txtUserName").clear()
        driver.find_element_by_id("ctl00_MainContent_txtPassword").clear()
        driver.find_element_by_id("ctl00_MainContent_txtUserName").send_keys("enmore")
        driver.find_element_by_id("ctl00_MainContent_txtPassword").send_keys("yiguo_ng")
        driver.find_element_by_id("ctl00_MainContent_btnLogin").click()

        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, "管理")))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        except TimeoutException:
            print("登录失败")

    @staticmethod
    def select_item(driver, item_name):
        s1 = Select(driver.find_element_by_id('ctl00_MainContent_ddlCommodity'))

        for select in s1.options:
            if select.text == item_name:
                s1.select_by_visible_text(select.text)
                driver.find_element_by_id("ctl00_MainContent_txtAmount").clear()
                driver.find_element_by_id("ctl00_MainContent_txtUserName").clear()
                driver.find_element_by_id("ctl00_MainContent_txtPhone").clear()
                driver.find_element_by_id("ctl00_MainContent_txtAmount").send_keys("1")
                driver.find_element_by_id("ctl00_MainContent_txtUserName").send_keys("张盛晓")
                driver.find_element_by_id("ctl00_MainContent_txtPhone").send_keys("13818886142")
                break

    @staticmethod
    def get_data(driver):
        try:
            driver.find_element_by_id("ctl00_MainContent_btnBuy").click()
            WebDriverWait(driver, 2).until(ec.alert_is_present())
            message = driver.switch_to.alert
            print(message.text)
            message.accept()
            print("购买成功")
        except TimeoutException:
            print("购买失败")


if __name__ == "__main__":
    action = LoginTest()
    action.loop_action()
