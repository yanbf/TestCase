#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize.window()
driver.get("http://ads.papayamobile.com/shoptimize/signin")
time.sleep(3)

driver.find_element_by_class_name('signin-input').send_keys('xiongqing@papayamobile.cn')
driver.find_element_by_xpath("//input[@type='password']").send_keys('papaya123')
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
time.sleep(3)

def create_offer():
	#driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
	driver.find_element_by_id("create_offer").click()
	time.sleep(3)

	driver.find_element_by_id('rdManual').click()
	driver.find_element_by_xpath("//input[@type='text']").send_keys('maunual_product')
	
	'''注：元素定位一定要找准是上传，定位方式:
执行sendKeys的元素一定要符合 input 和 type="file" 条件,
否则就是你没找对上传文件的对象，会上传失败的。id('upload')'''
	
	driver.find_element_by_id('upload').send_keys('E:\\amazon-us.csv')
	time.sleep(10)
	driver.find_element_by_xpath("//button[@class='btn btn-primary p-btn ot0']").click()
	print 'it is great!'
	
	
create_offer()
print 'OK'
#driver.quit()
