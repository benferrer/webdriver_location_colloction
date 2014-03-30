# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('locator.html')
dr.get(file_path)

input_string = 'easonhan.info'
# locate id=name
id_element = dr.find_element_by_id('name')
id_element.send_keys(input_string)
assert id_element.get_attribute('value') == input_string

# locate name=eason
name_element = dr.find_element_by_name('eason')
name_element.send_keys(input_string)
assert name_element.get_attribute('value') == input_string

# locate class_name=han
class_element = dr.find_element_by_class_name('han')
class_element.send_keys(input_string)
assert class_element.get_attribute('value') == input_string

# locate by xpath using class=form-control han
class_elem_xpath = dr.find_element_by_xpath('//input[@class="form-control han"]')
class_elem_xpath.send_keys('xpath')
assert class_elem_xpath.get_attribute('value') == (input_string + 'xpath')

# locate by css selector using class=form-control han
class_elem_css = dr.find_element_by_css_selector('input[class="form-control han"]')
class_elem_css.send_keys('css')
assert class_elem_css.get_attribute('value') == (input_string + 'xpath' + 'css')

