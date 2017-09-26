# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import getpass
from selenium.webdriver.support.ui import Select
import time
import os

def init_browser():
	driver = webdriver.Firefox()
	driver.get("https://www.gumtree.com.au/p-post-ad.html") # redirects to login
	return driver

def get_credentials():
	username = raw_input("Enter username:")
	password = getpass.getpass("Enter password:")
	return [username, password]

def login(driver, username, password):
	driver.find_element_by_id('login-email').send_keys(username)
	driver.find_element_by_id('login-password').send_keys(password)
	driver.find_element_by_id('btn-submit-login').click()
	return driver 

def post_new_add(driver):	
	try:
		ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'cat_9299'))).click() # vehicle
		ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'cat_18322'))).click() # motorcycle / scooter
		ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'cat_18626'))).click() # motorcycle
		ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'typ_OFFER'))).click() # I'm selling
	except TimeoutException: 
		pass

	# Nego
	#ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH , '//*[@id="syi-form"]/div[1]/div[2]/fieldset[1]/div/div[1]/div[2]/div[2]/label'))).click()
	print("Inputting price cunt")
	# Price
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'pstad-price'))).clear()
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'pstad-price'))).send_keys('price here')

	# Listing type
	Select(driver.find_element_by_id('motorcycles.forsaleby_s')).select_by_visible_text('Private seller')
	time.sleep(1)	

	#make
	Select(driver.find_element_by_id('motorcycles.motorcyclesmake_s')).select_by_visible_text('make here')
	time.sleep(1)	
	
	#model
	Select(driver.find_element_by_id('motorcycles.motorcyclesmake_s+motorcycles.model_s')).select_by_visible_text('model here')
	time.sleep(1)	
	
	#model
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.carenginedisplacement_i'))).clear()
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.carenginedisplacement_i'))).send_keys('displacement here')
	

	#type	
	Select(driver.find_element_by_id('motorcycles.type_s')).select_by_visible_text('type here')
	time.sleep(1)
	
	#subtype	
	Select(driver.find_element_by_id('motorcycles.type_s+motorcycles.subtype_s')).select_by_visible_text('sub-type here')
	time.sleep(1)

	#ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.learnerapproved_s-n'))).click() # L approved: negative
	
	#model
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.caryear_i'))).clear()
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.caryear_i'))).send_keys('year here')
	time.sleep(1)
	
	#kms
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.carmileageinkms_i'))).clear()
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'motorcycles.carmileageinkms_i'))).send_keys('kms here')
	time.sleep(1)
	

	#color
	Select(driver.find_element_by_id('motorcycles.colour_s')).select_by_visible_text('color here')
	time.sleep(1)
	
	#rego	
	Select(driver.find_element_by_id('motorcycles.registered_s')).select_by_visible_text('Yes')
	time.sleep(1)
	
	#title
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'title'))).clear()
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'title'))).send_keys('Title here')
	time.sleep(5)
	
	#desc
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'pstad-descrptn'))).clear()
	ui.WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((By.ID, 'pstad-descrptn'))).send_keys("Desc here")

	time.sleep(10)

	driver.find_element_by_xpath('//*[@id="loaded-files"]/li[1]/div').click()
	


TIMEOUT = 5
driver = None
creds = get_credentials()
post_new_add(login(init_browser(), creds[0], creds[1]))
try:	
	pass
except Exception, e:
	try:
		print("Exception occured!")
		print(str(e) + "\n" + str(e.getMessage()))
		driver.close()
	except Exception:
		print("Driver not found")


