# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                    # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC        # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


dr = webdriver.Firefox()
#dr = webdriver.Chrome()
dr.maximize_window()

def login():
    dr.get("http://papayads.com/shoptimize/signin")
    dr.find_element_by_class_name('signin-input').send_keys('xiongqing@papayamobile.cn')
    dr.find_element_by_xpath("//input[@type='password']").send_keys('papaya123')
    dr.find_element_by_xpath("//button[@class='btn btn-primary']").click()

def createCampaign():
    wait=WebDriverWait(dr, 10)
#点击广告系列
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/shoptimize/campaign_mode']"))).click()
#点击网站按钮
    wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[1]/button/div[2]"))).click()
#时间等待
    time.sleep(3)
#点击已有广告系列单选框
    wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[2]/input"))).click()
    time.sleep(5)
#点击下拉框
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[3]/div[1]/span/span[1]/span/span[2]"))).click()
#点击下拉框内容
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span/span/span[2]/ul/li[6]"))).click()

#点击保存&继续
    wait.until(EC.presence_of_element_located(
            (By.XPATH, "//fieldset/form/div[5]/button[1]"))).click()
    time.sleep(5)
    #dr.close()

login()
createCampaign()