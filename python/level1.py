# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import re

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

# locate by link_text=easonhan.info
link_text_element = dr.find_element_by_link_text(input_string)
link_text_element.click()
assert link_text_element.text == input_string

# locate by css_selector=#for-css
css_element = dr.find_element_by_css_selector('#for-css')
css_element.send_keys(input_string)
assert css_element.get_attribute('value') == input_string

# locate by xpath=#for-css
xpath_element = dr.find_element_by_xpath('//input[@id="for-xpath"]')
xpath_element.send_keys(input_string)
assert xpath_element.get_attribute('value') == input_string

# match id ~= ^for inputs and input something
inputs = dr.find_elements_by_tag_name('input')
# disable one input that id leading with for
disable_js = '$("#for-css").attr("disabled", "disabled");';
dr.execute_script(disable_js)
leading_str = 'Leading with for'
for ip in inputs:
	if re.search('^for.*', ip.get_attribute('id')): 
		if ip.get_attribute('type') == 'text' and ip.get_attribute('disabled') is None :
			ip.clear()
			ip.send_keys(leading_str)
assert dr.find_element_by_id('for-xpath').get_attribute('value') == leading_str
assert dr.find_element_by_id('for-css').get_attribute('disabled') == 'true'

# input something in readonly element
# method 1
# remove_readonly_js = '$("#readonly").removeAttr("readonly");'
# dr.execute_script(remove_readonly_js)
# read_only_element = dr.find_element_by_id('readonly')
# read_only_element.send_keys(input_string)
# assert read_only_element.get_attribute('value') == input_string

# method 2
set_value_to_readonly_js = '$("#readonly").attr("value", "%s")' %(input_string)
dr.execute_script(set_value_to_readonly_js)
assert dr.find_element_by_id('readonly').get_attribute('value') == input_string
