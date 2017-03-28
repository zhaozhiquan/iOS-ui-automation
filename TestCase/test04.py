# coding=utf-8
import unittest
import os
import random
from time import sleep
from appium import webdriver
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''登录'''
	def setUp(self):
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps())
		self.case_id = self.get_col(4,0)  # case id 列
		self.preset = self.get_col(4,2)  # 预置条件列
		self.using = self.get_col(4,5)  # 查找元素方式列
		self.value = self.get_col(4,6)  # 元素列
		self.exp = self.get_col(4,7)  # 预期结果列
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()

	def test_401(self):
		u'''账号输入为空'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,self.using[1], self.value[1])  # 账号输入框
		el.clear()

		el2 = self.element(self.driver,self.using[2], self.value[2])  # 密码密码输入框
		el2.clear()
		for i in xrange(10):
			self.element(self.driver,self.using[3], self.value[3]).click()       # 登录
			el3 = self.element_or_none(self.driver,self.using[4], self.value[4])  # 提示
			if el3.text != None:
				break
		try:
			print unicode('测试结果: %s' % el3.text.encode('utf-8'))
			print unicode('预期结果: %s' % self.exp[1].encode('utf-8'))
			self.dy_Equal(self.driver, unicode(el3.text), self.exp[1], self.case_id[1])  # 断言
		except:
			print unicode('测试结果: %s' % el3)
			print unicode('预期结果: 元素不为空')
			self.dy_IsNotNone(self.driver,el3,self.case_id[1])

	def test_402(self):
		u'''账号输入不为空，密码为空'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,self.using[5], self.value[5])  # 账号输入框
		el.clear()
		el.send_keys(self.preset[5].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[6], self.value[6])  # 密码密码输入框
		el2.clear()
		for i in xrange(10):
			self.element(self.driver,self.using[7], self.value[7]).click()       # 登录
			el3 = self.element(self.driver,self.using[8], self.value[8])  # 提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[5].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[5], self.case_id[5])  # 断言

	def test_403(self):
		u'''正确账号，错误密码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,self.using[9], self.value[9])  # 账号输入框
		el.clear()
		el.send_keys(self.preset[9].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[10], self.value[10])  # 密码密码输入框
		el2.clear()
		el2.send_keys(self.preset[10].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[11], self.value[11]).click()       # 登录
			el3 = self.element(self.driver,self.using[12], self.value[12])  # 提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[9].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[9], self.case_id[9])  # 断言

	def test_404(self):
		u'''错误账号，正确密码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,self.using[13], self.value[13])  # 账号输入框
		el.clear()
		el.send_keys(self.preset[13].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[14], self.value[14])  # 密码密码输入框
		el2.clear()
		el2.send_keys(self.preset[14].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[15], self.value[15]).click()       # 登录
			el3 = self.element(self.driver,self.using[16], self.value[16])  # 提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[13].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[13], self.case_id[13])  # 断言

	def test_405(self):
		u'''正确账号，密码少于6位'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,self.using[17], self.value[17])  # 账号输入框
		el.clear()
		el.send_keys(self.preset[17].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[18], self.value[18])  # 密码密码输入框
		el2.clear()
		el2.send_keys(self.preset[18].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[19], self.value[19]).click()       # 登录
			el3 = self.element(self.driver,self.using[20], self.value[20])  # 提示
			if el3.text != None:
				break
		print unicode('测试结果: %s' % el3.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[17].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el3.text), self.exp[17], self.case_id[17])  # 断言

	def test_406(self):
		u'''正确账号，正确密码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el = self.element(self.driver,self.using[21], self.value[21])  # 账号输入框
		el.clear()
		el.send_keys(self.preset[21].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[22], self.value[22])  # 密码密码输入框
		el2.clear()
		el2.send_keys(self.preset[22].encode('utf-8').decode("utf-8"))  # 输入

		self.element(self.driver,self.using[23], self.value[23]).click()       # 登录
		sleep(10)
		el3 =self.element_or_none(self.driver,self.using[24], self.value[24])  #继续查找登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[21].encode('utf-8'))
		self.dy_IsNone(self.driver,el3,self.case_id[21])       #断言为空

	def test_407(self):
		u'''选择列表中的账号登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[25], self.value[25]).click()  # 多账号查看
		el = self.elements(self.driver,self.using[26], self.value[26])
		el[1].click()                                                      #选择第二个账号
		self.element(self.driver,self.using[27], self.value[27]).click()   #登录
		sleep(10)
		el3 =self.element_or_none(self.driver,self.using[27], self.value[27])  #继续查找登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[25].encode('utf-8'))
		self.dy_IsNone(self.driver,el3,self.case_id[25])       #断言为空

	def test_408(self):
		u'''登录界面，点击左上角X按钮'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[28], self.value[28]).click()  # X按钮
		sleep(5)
		el3 = self.element_or_none(self.driver,self.using[29], self.value[29])  # 继续查找登录按钮
		print ('测试结果: %s' % el3)
		print ('预期结果: %s' % self.exp[28].encode('utf-8'))
		self.dy_IsNone(self.driver, el3, self.case_id[28])  # 断言为空
