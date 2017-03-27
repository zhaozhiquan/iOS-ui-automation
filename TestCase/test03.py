# coding=utf-8
import unittest
import os
import random
from time import sleep
from appium import webdriver
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''忘记密码'''
	def setUp(self):
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps())
		self.case_id = self.get_col(3,0)  # case id 列
		self.preset = self.get_col(3,2)  # 预置条件列
		self.using = self.get_col(3,5)  # 查找元素方式列
		self.value = self.get_col(3,6)  # 元素列
		self.exp = self.get_col(3,7)  # 预期结果列
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()

	def test_301(self):
		u'''忘记密码，返回'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[1], self.value[1]).click()   #忘记密码
		self.element(self.driver,self.using[2], self.value[2]).click()   #返回
		el = self.element(self.driver,self.using[3], self.value[3])      #游客登录按钮
		print unicode('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[1].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[1], self.case_id[1])  # 断言

	def test_302(self):
		u'''忘记密码，手机号输入为空'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[4], self.value[4]).click()   #忘记密码
		for i in xrange(10):
			self.element(self.driver,self.using[5], self.value[5]).click()   #获取验证码

			el = self.element(self.driver,self.using[6], self.value[6])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[4].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[4], self.case_id[4])  # 断言

	def test_303(self):
		u'''忘记密码，手机号输10位'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[7], self.value[7]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[8], self.value[8])  # 手机号输入框
			el.send_keys(self.preset[8].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[8], '//*[@value=%s]'% self.preset[8]) #重新获取该元素
			if el2.text == self.preset[8]:  #判断输入的与 预置是否一致
				break
		for i in xrange(10):
			self.element(self.driver,self.using[9], self.value[9]).click()   #获取验证码
			el = self.element(self.driver,self.using[10], self.value[10])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[7].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[7], self.case_id[7])  # 断言

	def test_304(self):
		u'''忘记密码，手机号输12位'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[11], self.value[11]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[12], self.value[12])  # 手机号输入框
			el.send_keys(self.preset[12].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[12], '//*[@value=%s]'% self.preset[12]) #重新获取该元素
			if el2.text == self.preset[12]:  #判断输入的与 预置是否一致
				break
		for i in xrange(10):
			self.element(self.driver,self.using[13], self.value[13]).click()   #获取验证码
			el = self.element(self.driver,self.using[14], self.value[14])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[11].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[11], self.case_id[11])  # 断言

	def test_305(self):
		u'''忘记密码，手机号输11位'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[15], self.value[15]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[16], self.value[16])  # 手机号输入框
			el.send_keys(self.preset[16].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[16], '//*[@value=%s]'% self.preset[16]) #重新获取该元素
			if el2.text == self.preset[16]:  #判断输入的与 预置是否一致
				break

		self.element(self.driver,self.using[17], self.value[17]).click()   #获取验证码
		el = self.element(self.driver,self.using[18], self.value[18])      #提示
		try:
			print unicode('测试结果: %s' % el.text.encode('utf-8'))
			print unicode('预期结果: %s' % self.exp[15].encode('utf-8'))
			self.dy_Equal(self.driver, unicode(el.text), self.exp[15], self.case_id[15])  # 断言
		except:
			print unicode('测试结果: %s' % el)
			print unicode('预期结果: 元素不为空')
			self.dy_IsNotNone(self.driver,el,self.case_id[15])

	def test_306(self):
		u'''忘记密码，正确手机号，空验证码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[19], self.value[19]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[20], self.value[20])  # 手机号输入框
			el.send_keys(self.preset[20].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[20], '//*[@value=%s]'% self.preset[20]) #重新获取该元素
			if el2.text == self.preset[20]:  #判断输入的与 预置是否一致
				break
		for i in xrange(10):
			self.element(self.driver,self.using[21], self.value[21]).click()   #下一步

			el = self.element(self.driver,self.using[22], self.value[22])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[19].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[19], self.case_id[19])  # 断言

	def test_307(self):
		u'''忘记密码，正确手机号,错误验证码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[23], self.value[23]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[24], self.value[24])  # 手机号输入框
			el.send_keys(self.preset[24].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[24], '//*[@value=%s]'% self.preset[24]) #重新获取该元素
			if el2.text == self.preset[24]:  #判断输入的与 预置是否一致
				break

		el3 = self.element(self.driver,self.using[25], self.value[25])     #验证码输入框
		el3.send_keys(self.preset[25].encode('utf-8').decode("utf-8")) #输入
		for i in xrange(10):
			self.element(self.driver,self.using[26], self.value[26]).click()   #下一步

			el = self.element(self.driver,self.using[27], self.value[27])      #提示
			if el.text !=None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[23].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[23], self.case_id[23])  # 断言

	def test_308(self):
		u'''忘记密码，正确手机号,过期验证码'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[28], self.value[28]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[29], self.value[29])  # 手机号输入框
			el.send_keys(self.preset[29].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[29], '//*[@value=%s]'% self.preset[29]) #重新获取该元素
			if el2.text == self.preset[29]:  #判断输入的与 预置是否一致
				break

		el3 = self.element(self.driver,self.using[30], self.value[30])     #验证码输入框
		el3.send_keys(self.preset[30].encode('utf-8').decode("utf-8")) #输入
		for i in xrange(10):

			self.element(self.driver,self.using[31], self.value[31]).click()   #下一步

			el = self.element(self.driver,self.using[32], self.value[32])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[28].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[28], self.case_id[28])  # 断言

	def yanzhengma(self):
		'''
		#验证码
		:return:
		'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[33], self.value[33]).click()   #忘记密码
		for i in range(10):
			el = self.element(self.driver,self.using[34], self.value[34])  # 手机号输入框
			el.send_keys(self.preset[34].encode('utf-8').decode("utf-8")) #输入
			el2 = self.element(self.driver,self.using[34], '//*[@value=%s]'% self.preset[34]) #重新获取该元素
			if el2.text == self.preset[34]:  #判断输入的与 预置是否一致
				break

		el3 = self.element(self.driver,self.using[35], self.value[35])     #验证码输入框
		el3.send_keys(self.preset[35].encode('utf-8').decode("utf-8")) #输入

		self.element(self.driver,self.using[36], self.value[36]).click()   #下一步
		sleep(2)


	def test_309(self):
		u'''忘记密码，正确手机号,正确验证码'''
		self.yanzhengma()
		el = self.element(self.driver,self.using[37], self.value[37])      #提示
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[33].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[33], self.case_id[33])  # 断言

	def test_310(self):
		u'''忘记密码，密码输入为空'''
		self.yanzhengma()                #38
		for i in xrange(10):
			self.element(self.driver,self.using[39], self.value[39]).click()   #提交
			el = self.element(self.driver,self.using[40], self.value[40])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[38].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[38], self.case_id[38])  # 断言

	def test_311(self):
		u'''忘记密码，密码与确认密码少于6位'''
		self.yanzhengma()                #41
		el1 =self.element(self.driver,self.using[42], self.value[42])      #密码输入框
		el1.send_keys(self.preset[42].encode('utf-8').decode("utf-8"))  #输入

		el2 =self.element(self.driver,self.using[43], self.value[43])      #确认密码输入框
		el2.send_keys(self.preset[43].encode('utf-8').decode("utf-8"))  #输入
		for i in xrange(10):
			self.element(self.driver,self.using[44], self.value[44]).click()      #提交
			el = self.element(self.driver,self.using[45], self.value[45])      #提示
			if el.text != None:
				break
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[41].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[41], self.case_id[41])  # 断言

	def test_312(self):
		u'''忘记密码，密码与确认密码不一致'''
		self.yanzhengma()                #46
		el1 =self.element(self.driver,self.using[47], self.value[47])      #密码输入框
		el1.send_keys(self.preset[47].encode('utf-8').decode("utf-8"))  #输入

		el2 =self.element(self.driver,self.using[48], self.value[48])      #确认密码输入框
		el2.send_keys(self.preset[48].encode('utf-8').decode("utf-8"))  #输入
		for i in xrange(10):

			self.element(self.driver,self.using[49], self.value[49]).click()           #提交

			el = self.element_or_none(self.driver,self.using[50], self.value[49])        #提示
			if el != None:
				break
		print ('测试结果: %s' % el)
		print ('预期结果: %s' % self.exp[46].encode('utf-8'))
		self.dy_IsNotNone(self.driver,el,self.case_id[46])  # 断言

	def test_313(self):
		u'''忘记密码，密码与确认密码一致'''
		self.yanzhengma()                #51
		el1 =self.element(self.driver,self.using[52], self.value[52])      #密码输入框
		el1.send_keys(self.preset[52].encode('utf-8').decode("utf-8"))  #输入

		el2 =self.element(self.driver,self.using[53], self.value[53])      #确认密码输入框
		el2.send_keys(self.preset[53].encode('utf-8').decode("utf-8"))  #输入

		self.element(self.driver,self.using[54], self.value[54]).click()          #提交
		el = self.element(self.driver,self.using[55], self.value[55])      #提示
		print unicode('测试结果: %s' % el.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[51].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.text), self.exp[51], self.case_id[51])  # 断言

	def test_314(self):
		u'''修改密码后登录'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		el1 =self.element(self.driver,self.using[56], self.value[56])      #账号输入框
		el1.clear()
		el1.send_keys(self.preset[56].encode('utf-8').decode("utf-8"))  #输入

		el2 =self.element(self.driver,self.using[57], self.value[57])      #密码密码输入框
		el2.clear()
		el2.send_keys(self.preset[57].encode('utf-8').decode("utf-8"))  #输入
		self.element(self.driver,self.using[58], self.value[58]).click()    #登录
		sleep(10)
		el3 = self.element_or_none(self.driver,self.using[58], self.value[58])  #再次寻找游客登录按钮
		print unicode('测试结果: %s' % el3)
		print unicode('预期结果: %s' % self.exp[56].encode('utf-8'))
		self.dy_IsNone(self.driver, el3,  self.case_id[56])  # 断言

