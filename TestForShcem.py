from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as ec  # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginTest(Exception):
    def __init__(self, msg):
        self.msg = msg

def get_data():
    driver = webdriver.Chrome()

    driver.get("http://member.test.shcem.com/Account/Index")
    driver.find_element_by_id("txtLoginMobile").clear(
    driver.find_element_by_id("txtLoginPwd").clear()
    driver.find_element_by_id("txtLoginMobile").send_keys("13800000001")
    driver.find_element_by_id("txtLoginPwd").send_keys("111111")
    driver.find_element_by_id("btnLogin").click()

    try:
        driver.maximize_window()

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, "退出")))
        driver.get("http://trade.test.shcem.com/LeadsLiner/MyLeadsLiner")

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "我要买货")))

        element = driver.find_element_by_class_name("aOptDireciton")
        element2 = driver.find_element_by_class_name("buy-now-price")

        ActionChains(driver).move_to_element(element).click(element2).perform()

        time.sleep(10)

    except TimeoutException:
        print("登录失败")

    time.sleep(5)


if __name__ == "__main__":
    
    print("success")
    get_data()
