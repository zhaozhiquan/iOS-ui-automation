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
			'bundleId': 'com.test.tmcs001',
			#'bundleId':'com.zhankai.tmcs',
			#'bundleId': 'com.inone.mbzj001',
			#'bundleId': 'com.netease.cloudphotos',
			#'app': '/Users/zhaozhiquan/automation/iOSSdk/CloudAlbum_iPhone_V3.0.app',
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
		'''

		:param driver: 驱动
		:param value1: 对比值1,一般是 element.text
		:param value2: 对比值2,一般是预期结果
		:param screen_name: 以case id 为名称
		:return:
		'''
		#断言,assertEqual,断言失败会截图
		self.driver = driver
		try:
			self.assertEqual(value1, value2)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertEqual(value1, value2)

	def dy_NotEqual(self,driver,value1,value2,screen_name):
		'''

		:param driver: 驱动
		:param value1: 对比值1,一般是 element.text
		:param value2: 对比值2,一般是预期结果
		:param screen_name: 以case id 为名称
		:return:
		'''
		# 断言,assertNotEqual,断言失败会截图
		self.driver = driver
		try:
			self.assertNotEqual(value1, value2)
		except:
			self.screencap(self.driver, name=screen_name)
			self.assertNotEqual(value1, value2)

	def dy_IsNone(self,driver,obj,screen_name):
		'''

		:param driver: 驱动
		:param obj: 对象
		:param screen_name:截图名称
		:return:
		'''
		# 断言,assertIsNone,断言失败会截图
		self.driver = driver
		try:
			self.assertIsNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNone(obj)
	def dy_IsNotNone(self,driver,obj,screen_name):
		'''

		:param driver:驱动
		:param obj: 对象
		:param screen_name:截图名称
		:return:
		'''
		# 断言,assertIsNotNone,断言失败会截图
		self.driver = driver
		try:
			self.assertIsNotNone(obj)
		except:
			self.screencap(self.driver,name=screen_name)
			self.assertIsNotNone(obj)

	def public(self,driver):
		'''

		:param driver:驱动
		:return: 一个屏幕像素list
		'''
		#获取屏幕像素,返回一个list坐标
		self.driver = driver
		window = self.driver.get_window_size()

		width = int(window[u'width'])
		height = int(window[u'height'])
		zuobiao = [width, height]
		return zuobiao

	def left_swipe(self, driver):
		'''

		:param driver: 驱动
		:return:
		'''
		#左划动
		self.driver = driver
		a = {"direction": "left"}
		return self.driver.execute_script('mobile: swipe', a)


	def right_swipe(self, driver):
		'''

		:param driver:驱动
		:return:
		'''
		#右划动
		self.driver = driver
		a = {"direction": "right"}
		return self.driver.execute_script('mobile: swipe', a)

	def up_swipe(self, driver):
		'''

		:param driver:驱动
		:return:
		'''
		#上划动
		self.driver = driver
		a = self.public(self.driver)
		#macaca
		#self.driver.touch('drag', {'fromX':a[0] / 2, 'fromY':a[1] * 5 / 6, 'toX':a[0] / 2, 'toY':a[1] * 1 / 6,'duration': 0})
		#appium ios
		a = {"direction": "up"}
		return self.driver.execute_script('mobile: swipe', a)

	def down_swipe(self, driver):
		'''

		:param driver:驱动
		:return:
		'''
		#下划动
		self.driver = driver
		a = {"direction": "down"}
		return self.driver.execute_script('mobile: swipe', a)

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

	def tap(self,driver,value,dealy=None):
		'''
		:param driver:驱动
		:param value: 坐标比例,传入元组
		:param dealy: 延迟
		:return:
		'''
		self.driver = driver
		zuobiao = self.public(driver)
		value = (int(value[0] * zuobiao[0]), int(value[1] * zuobiao[1]))
		return self.driver.tap([value], dealy)

