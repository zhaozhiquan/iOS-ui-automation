# coding=utf-8
import unittest
import os
from time import sleep
from macaca import WebDriver
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	def setUp(self):
		self.driver = WebDriver(self.desired_caps(), self.server_url())
		self.driver.init()
		self.case_id = self.get_col(0)  # case id 列
		self.preset = self.get_col(2)  # 预置条件列
		self.using = self.get_col(5)  # 查找元素方式列
		self.value = self.get_col(6)  # 元素列
		self.exp = self.get_col(7)  # 预期结果列

	def tearDown(self):
		self.driver.quit()
	def test_101(self):
		u'''查看用户协议'''
		sleep(10)
		self.driver.element(self.using[51], self.value[51]).click()  # 用户协议
		sleep(5)
		el = self.driver.element(self.using[52], self.value[52])	 #协议内容
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[51].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[0], self.case_id[51])  # 断言


	def test_102(self):
		u'''用户协议界面，返回登录界面'''
		sleep(10)
		self.driver.element(self.using[53], self.value[53]).click()  # 用户协议
		sleep(3)
		self.driver.element(self.using[54], self.value[54]).click()  #返回
		sleep(1)
		el = self.driver.element(self.using[55], self.value[55])     #忘记密码
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[53].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[0], self.case_id[53])  # 断言


