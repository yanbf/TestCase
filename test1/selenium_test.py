# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver =webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
try:
    #定位右击的元素
    RC=driver.find_element_by_css_selector('#head > div > div.s_form')
    #对定位到的元素执行鼠标右击操作
    ActionChains(driver).context_click(RC).perform()
    time.sleep(5)
    print  'ok!'
except Exception as e:
    print e
finally:
    driver.quit()

'''
driver.find_element_by_id('kw').clear()  #clear 清空输入框内容
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(3)
'''





