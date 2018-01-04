# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class Python_testcases_RC(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://146.148.54.18:5000/login")
        self.selenium.start()
    
    def test_python_testcases__r_c(self):
        sel = self.selenium
        sel.open("/login")
        time.sleep(2)
        sel.click("link=Account for External User")
        time = sel.get_eval("(new Date().getHours()+new Date().getMinutes()+ new Date().getSeconds()+Math.floor(Math.random()*11111)+new Date().getSeconds())")
        sel.type("id=username", "demouser" + time)
        sel.type("id=email", "demouser" + time + "@wipro.com")
        sel.type("id=display-name", "demouser" + time)
        sel.type("id=first-name", "firstname" + time)
        sel.type("id=last-name", "lastname" + time)
        sel.type("id=password", "wipro@123")
        sel.type("id=password-confirm", "wipro@123")
        sel.click("id=submit")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
