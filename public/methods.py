#!/usr/bin/env python
#coding=utf-8
import os
from time import sleep, strftime
class Methods(object):
	def desired_caps(self):
		#配置信息
		desired_caps = {
			'platformName': 'iOS',
			'platformVersion': '9.3',
			'deviceName': 'iPhone 6s',
			'autoAcceptAlerts': True,
			# 'autoDismissAlerts' : True ,
			#'reuse': 3,
			'udid':'e6505fdce9a8459fd534d3a8da8352c315cb2058',
			#'bundleId':'com.zhankai.tmcs',
			'bundleId': 'com.inone.mbzj001',
			#'bundleId': 'com.inone.shenyudalu',
			#'app': './automation/iosSDK/AGJointOperationSDKDemo.app',
			'automationName':'XCUITest'
		}
		return desired_caps
	def server_url(self):
		server_url = {
			'hostname': 'localhost',
			'port': 3456
		}
		return server_url

	def screencap(self, driver, **kwargs):
		#截图
		dict1 = kwargs
		self.name = dict1['name']
		day = strftime('%Y-%m-%d')
		path = 'result/' + day + '/screencap/'
		if os.getcwd()+os.sep =='/Users/zhaozhiquan/automation/iOSSdk/TestCase/':
			self.driver.save_screenshot(os.getcwd() + os.sep +'../'+ path + self.name + '.png')

		else:
			self.driver.save_screenshot(os.getcwd()+os.sep+path + self.name + '.png')



	def dy_Equal(self,driver,value1,value2,screen_name):
		#断言,assertEqual,断言失败会截图
		self.driver = driver
		try:
			self.assertEqual(value1, value2)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertEqual(value1, value2)
	def dy_IsNone(self,driver,obj,screen_name):
		# 断言,assertIsNone,断言失败会截图
		self.driver = driver
		try:
			self.assertIsNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNone(obj)
	def dy_IsNotNone(self,driver,obj,screen_name):
		# 断言,assertIsNotNone,断言失败会截图
		self.driver = driver
		try:
			self.assertIsNotNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNotNone(obj)

	def public(self,driver):
		#获取屏幕像素,返回一个list坐标
		self.driver = driver
		window = self.driver.get_window_size()
		if self.desired_caps()['bundleId'] =='com.zhankai.tmcs':
			width = int(window[u'width'])
			height = int(window[u'height'])
		else:
			#横屏 height、width调换
			height = int(window[u'width'])
			width = int(window[u'height'])
		zuobiao = [width, height]
		return zuobiao

	def left_swipe(self, driver):
		#左划动
		self.driver = driver
		a = self.public(self.driver)
		self.driver.touch('drag', {'fromX': a[0] * 5 / 6, 'fromY': a[1] / 2, 'toX': a[0] * 1 / 6, 'toY': a[1] / 2, 'duration': 1})
		sleep(2)

	def right_swipe(self, driver):
		#右划动
		self.driver = driver
		a = self.public(self.driver)
		self.driver.touch('drag',{'fromX':a[0] * 1 / 6, 'fromY':a[1] / 2, 'toX':a[0] * 5 / 6, 'toY': a[1] / 2, 'duration': 1})
		sleep(2)

	def up_swipe(self, driver):
		#上划动
		self.driver = driver
		a = self.public(self.driver)
		self.driver.touch('drag', {'fromX':a[0] / 2, 'fromY':a[1] * 5 / 6, 'toX':a[0] / 2, 'toY':a[1] * 1 / 6,'duration': 0})
		sleep(2)

	def down_swipe(self, driver):
		#下划动
		self.driver = driver
		a = self.public(self.driver)
		self.driver.touch('drag', {'fromX':a[0] / 2, 'fromY':a[1] * 1 / 6, 'toX':a[0] / 2, 'toY':a[1] * 5 / 6, 'duration': 1})
		sleep(2)

	def element(self,driver,methods,value):
		'''
		:param driver:驱动
		:param methods: 方式
		:param value: 值
		:return: 返回对象
		'''
		self.driver = driver
		if methods == 'name':
			return self.driver.find_element_by_name(value)
		elif methods == 'xpath':
			return  self.driver.find_element_by_xpath(value)
		elif methods == 'id':
			return self.driver.find_element_by_id(value)
		elif methods == 'class':
			return self.driver.find_element_by_class_name(value)

	def elements(self,driver,methods,value):
		'''
		:param driver:驱动
		:param methods: 方式
		:param value: 值
		:return: 返回对象list
		'''
		self.driver = driver
		if methods == 'name':
			return self.driver.find_elements_by_name(value)
		elif methods == 'xpath':
			return  self.driver.find_elements_by_xpath(value)
		elif methods == 'id':
			return self.driver.find_elements_by_id(value)
		elif methods == 'class':
			return self.driver.find_elements_by_class_name(value)


	def element_or_none(self,driver,methods,value):
		'''
		:param driver:驱动
		:param methods:方式
		:param value:知
		:return:元素存在返回元素,不存在,返回None
		'''
		self.driver = driver
		try:
			element = self.element(self.driver,methods,value)
		except:
			element = None
		return element
