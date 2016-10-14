#can not run

#solve webdriver wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                    # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC        # available since 2.26.0
import time
import unittest

class Campaign(unittest.TestCase):
    def login(self):
        self.dr=webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get("http://papayads.com/shoptimize/signin")
        self.dr.find_element_by_class_name('signin-input').send_keys('xiongqing@papayamobile.cn')
        self.dr.find_element_by_xpath("//input[@type='password']").send_keys('papaya123')
        self.dr.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    def createCampaign(self):
        wait=WebDriverWait(dr, 10)
        #wait=dr.implicitly_wait(30)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/shoptimize/campaign_mode']"))).click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='viwe_cearte_campaign']/div/table/tbody/tr[1]/td[1]/button"))).click()
            print "success"
        except: print "something error!"
        #finally:dr.quit()

if __name__=="__main()__":
    unittest.main()
