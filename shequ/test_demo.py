import pytest
import selenium
from selenium import webdriver
import time


class TestMember:



    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.find_elements_by_class_name("d-button-label")[-1].click()
        self.driver.find_element_by_id("login-account-name").send_keys("897037117@qq.com")
        self.driver.find_element_by_id("login-account-password").send_keys("wbh19960331")
        self.driver.find_element_by_id("login-button").click()
        time.sleep(3)
        self.driver.get("https://ceshiren.com/admin/users/list/active")

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.save_screenshot('1.jpeg')
        self.driver.quit()

    def test_member(self):

        self.driver.find_element_by_class_name("ember-text-field").send_keys("lianyang19860928@163.com")
        time.sleep(3)
