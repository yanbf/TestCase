# -*-coding:utf-8-*-
from selenium import webdriver
import time
import os

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('checkbox.html')
dr.get(file_path)

inputs= dr.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()
time.sleep(2)

#把页面最后一个checkbox勾掉
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(2)
dr.quit()