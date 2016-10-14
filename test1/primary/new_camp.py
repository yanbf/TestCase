# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                    # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC        # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

#def openChrome():
    #global dr
dr= webdriver.Chrome()
dr.maximize_window()

def login():
    dr.get("http://papayads.com/shoptimize/signin")
    dr.find_element_by_class_name('signin-input').send_keys('xiongqing@papayamobile.cn')
    dr.find_element_by_xpath("//input[@type='password']").send_keys('papaya123')
    dr.find_element_by_xpath("//button[@class='btn btn-primary']").click()


def createCampaign():
    wait=WebDriverWait(dr, 10)
    #wait=dr.implicitly_wait(30)
    try:
        #点击广告系列
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/shoptimize/campaign_mode']"))).click()
        #点击网站按钮
        wait.until(EC.presence_of_element_located((By.XPATH, "//td[1]/button/div[2]"))).click()
        time.sleep(3)

        #新建Campaign
        wait.until(EC.presence_of_element_located(
            (By.XPATH,'//form/div[2]/div[2]/div[2]/input'))).send_keys('newAd')
         # 定位下拉列表
        wait.until(EC.presence_of_element_located(
            (By.XPATH,"//form/div[4]/div[2]/div[1]/span/span[1]/span/span[2]"))).click()
        # 定位选择项
        wait.until(EC.presence_of_element_located(
            (By.XPATH,"//span/span/span[2]/ul/li[6]"))).click()
        # webdriver.ActionChains(dr).move_to_element(option).perform()
        # 保存&继续
        dr.find_element_by_xpath('//div[5]/button[1]').click()
        time.sleep(5)
        print "yes!"        # print "success"  #import pdb;pdb.set_trace()
    except Exception as e: 
        print e
    finally:
        dr.quit()

if __name__ == '__main__':
    openChrome()
    login()
    createCampaign()