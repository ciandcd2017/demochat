# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#from selenium.support.ui import ExpectedConditions
#from selenium.support.ui import WebDriverWait
import unittest,time,re

class ChatAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_chat_automation(self):
        driver = self.driver
        driver.get("http://35.224.112.117:5000/login#")
        driver.find_element_by_link_text("Account for External User").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval |  | ]]
        #time = driver.get_eval("(new Date().getHours()+new Date().getMinutes()+ new Date().getSeconds()+Math.floor(Math.random()*11111)+new Date().getSeconds())")
        timed = time.ctime()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys('demousr'+ timed)
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys('demousr'+ timed + '@wipro.com')
        driver.find_element_by_id("display-name").click()
        driver.find_element_by_id("display-name").clear()
        driver.find_element_by_id("display-name").send_keys("demousr", timed)
        driver.find_element_by_id("first-name").click()
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys("firstname", timed)
        driver.find_element_by_id("last-name").click()
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys("lastname", timed)
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("wipro@123")
        driver.find_element_by_css_selector("div.row").click()
        driver.find_element_by_id("password-confirm").click()
        driver.find_element_by_id("password-confirm").clear()
        driver.find_element_by_id("password-confirm").send_keys("wipro@123")
        driver.find_element_by_id("submit").click()
        #WebDriverWait wait = new WebDriverWait(driver, 10);
		#WebElement confirmbtn = wait.until(ExpectedConditions.elementToBeClickable(By.cssselector("button.confirm")));
		#confirmbtn.click();
        driver.implicitly_wait(30)
        #time.sleep(500)
        driver.find_element_by_css_selector("button.confirm").click()
        # ERROR: Caught exception [unknown command []]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
