# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait                    # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC        # available since 2.26.0
import time


dr=webdriver.Chrome()
dr.maximize_window()
def login():
    dr.get("http://ads.papayamobile.com/shoptimize/signin")
    dr.find_element_by_class_name('signin-input').send_keys('xiongqing@papayamobile.cn')
    dr.find_element_by_xpath("//input[@type='password']").send_keys('papaya123')
    dr.find_element_by_xpath("//button[@class='btn btn-primary']").click()
def createCampaign():
    wait=WebDriverWait(dr, 10)
    #wait=dr.implicitly_wait(30)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/shoptimize/campaign_mode']"))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='viwe_cearte_campaign']/div/table/tbody/tr[1]/td[1]/button"))).click()
        #定位单选按钮
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='viwe_cearte_campaign']/div/fieldset/form/div[2]/div[2]/div[1]/label[2]/input"))).click()
        #定位下拉列表
        time.sleep(5)
        dr.find_element_by_xpath("//*[@id='viwe_cearte_campaign']/div/fieldset/form/div[2]/div[2]/div[3]/div[1]/span/span[1]/span/span[2]").click()
        print 'ok1'
        time.sleep(8)
        down=Select(dr.find_element_by_xpath("//*[@id='viwe_cearte_campaign']/div/fieldset/form/div[2]/div[2]/div[3]/div[1]/select"))
        print 'ok2'
        time.sleep(5)
        down.select_by_value("1486").click()
        #dr.find_element_by_xpath("//option[@value='1486']").click()
        #down.find_element_by_xpath("//*[@id='viwe_cearte_campaign']/div/fieldset/form/div[2]/div[2]/div[3]/div[1]/select/option[28]").click()
        #wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='viwe_cearte_campaign']/div/fieldset/form/div[2]/div[2]/div[3]/div[1]/select/option[28]"))).click()

        print "success"
    except: print "something error!"
    finally:dr.quit()
login()
createCampaign()
