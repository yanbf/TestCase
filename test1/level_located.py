# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

dr =webdriver.Chrome()
file_path='file:///' + os.path.abspath('level_located.html')
dr.get(file_path)

#定位到link1点击获取下拉框
dr.find_element_by_link_text('Link1').click()
#找到id 为dropdown1的父元素
WebDriverWait(dr, 10).until(lambda the_driver:the_driver.find_element_by_id('dropdown1').is_displayed())
#在父亲元件下找到link 为Action 的子元素
menu = dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')
print 'ok'
#鼠标定位到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()
print  'ok1'
time.sleep(2)
dr.quit()


