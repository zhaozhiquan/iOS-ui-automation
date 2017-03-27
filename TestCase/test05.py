# coding=utf-8
import unittest
import os
import random
from time import sleep
from appium import webdriver
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''第三方登录'''
	def setUp(self):
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps())
		self.case_id = self.get_col(5,0)  # case id 列
		self.preset = self.get_col(5,2)  # 预置条件列
		self.using = self.get_col(5,5)  # 查找元素方式列
		self.value = self.get_col(5,6)  # 元素列
		self.exp = self.get_col(5,7)  # 预期结果列
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()

	def test_501(self):
		u'''第三方登录，返回'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[1], self.value[1]).click()  #第三方登录
		self.element(self.driver,self.using[2], self.value[2]).click()  #账号登录
		el = self.element(self.driver,self.using[3], self.value[3])     #登录按钮
		print ('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print ('预期结果: %s' % self.exp[1].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[1], self.case_id[1])  # 断言

	def test_502(self):
		u'''第三方登录，点击左上角X按钮'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[4], self.value[4]).click()  #第三方登录
		self.element(self.driver,self.using[5], self.value[5]).click()  #X按钮
		el3 = self.element_or_none(self.driver,self.using[6], self.value[6])  # 查找登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[4].encode('utf-8'))
		self.dy_IsNone(self.driver, el3, self.case_id[4])  # 断言为空

	def test_503(self):
		u'''第三方登录，微信取消登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[7], self.value[7]).click()  #第三方登录
		self.element(self.driver,self.using[8], self.value[8]).click()  #选择微信按钮
		sleep(5)
		self.element(self.driver,self.using[9], self.value[9]).click()  #取消按钮
		sleep(2)
		el3 = self.element(self.driver,self.using[10], self.value[10])  # 账号登录按钮
		print ('测试结果: %s' % el3.get_attribute('name').encode('utf-8'))
		print ('预期结果: %s' % self.exp[7].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.get_attribute('name')), self.exp[7], self.case_id[7])  # 断言

	def test_504(self):
		u'''第三方登录，微博取消登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[11], self.value[11]).click()  #第三方登录
		self.element(self.driver,self.using[12], self.value[12]).click()  #选择微博按钮
		sleep(10)
		self.element(self.driver,self.using[13], self.value[13]).click()  #取消按钮
		sleep(2)
		el3 = self.element(self.driver,self.using[14], self.value[14])  # 账号登录按钮
		print unicode('测试结果: %s' % el3.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[11].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.get_attribute('name')), self.exp[11], self.case_id[11])  # 断言

	def test_505(self):
		u'''第三方登录，QQ取消登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[15], self.value[15]).click()  #第三方登录
		self.element(self.driver,self.using[16], self.value[16]).click()  #选择QQ按钮
		sleep(5)
		self.element(self.driver,self.using[17], self.value[17]).click()  #取消按钮
		sleep(2)
		el3 = self.element(self.driver,self.using[18], self.value[18])  # 账号登录按钮
		print unicode('测试结果: %s' % el3.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[15].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.get_attribute('name')), self.exp[15], self.case_id[15])  # 断言

	def test_506(self):
		u'''第三方登录，微信登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[19], self.value[19]).click()  #第三方登录
		self.element(self.driver,self.using[20], self.value[20]).click()  #选择微信按钮
		sleep(5)
		self.element(self.driver,self.using[21], self.value[21]).click()  #登录按钮
		sleep(5)
		el3 = self.element_or_none(self.driver,self.using[22], self.value[22])  # 查看登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[19].encode('utf-8'))
		self.dy_IsNone(self.driver,el3,self.case_id[19])

	def test_507(self):
		u'''第三方登录，微博登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[23], self.value[23]).click()  #第三方登录
		self.element(self.driver,self.using[24], self.value[24]).click()  #选择微博按钮
		sleep(10)
		self.element(self.driver,self.using[25], self.value[25]).click()  #登录按钮
		sleep(5)
		el3 = self.element_or_none(self.driver,self.using[26], self.value[26])  # 查看登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[23].encode('utf-8'))
		self.dy_IsNone(self.driver, el3, self.case_id[23])

	def test_508(self):
		u'''第三方登录，微博登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[27], self.value[27]).click()  #第三方登录
		self.element(self.driver,self.using[28], self.value[28]).click()  #选择微博按钮
		sleep(5)
		self.element(self.driver,self.using[29], self.value[29]).click()  #登录按钮
		sleep(5)
		el3 = self.element_or_none(self.driver,self.using[30], self.value[30])  # 查看登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[27].encode('utf-8'))
		self.dy_IsNone(self.driver, el3, self.case_id[27])

