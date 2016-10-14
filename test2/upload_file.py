# -*-coding:utf-8-*-
from selenium import webdriver
import time
import os
from test1.primary import new_camp
from test1.primary.new_camp import login
#import pdb;pdb.set_tralsce()

#dr=webdriver.Chrome()
#dr.maximize_window()

def contact():
    new_camp.dr.find_element_by_link_text("联系我们").click()
    print 'ok'

login()
time.sleep(3)
contact()

