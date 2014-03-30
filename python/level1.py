# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('locator.html')
dr.get(file_path)

# locate id=name
dr.find_element_by_id('name').send_keys('easonhan.info')

# locate name=eason
dr.find_element_by_name('eason').send_keys('easonhan.info')

# locate class_name=han
dr.find_element_by_class_name('han').send_keys('easonhan.info')

# locate by xpath using class=form-control han
dr.find_element_by_xpath('//input[@class="form-control han"]').send_keys('xpath')

# locate by css selector using class=form-control han
dr.find_element_by_css_selector('input[class="form-control han"]').send_keys('css')

