# coding=utf-8
import unittest
import random
from time import sleep
from appium import webdriver
import public.methods as t
import public.case_xls as xl
class IOSSDK(unittest.TestCase,t.Methods,xl.Case_xls):
	u'''账号注册'''
	def setUp(self):
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps())
		self.case_id = self.get_col(2,0)  # case id 列
		self.preset = self.get_col(2,2)  # 预置条件列
		self.using = self.get_col(2,5)  # 查找元素方式列
		self.value = self.get_col(2,6)  # 元素列
		self.exp = self.get_col(2,7)  # 预期结果列
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.quit()

	def test_201(self):
		u'''账号注册，返回'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[1], self.value[1]).click()   #新用户注册
		self.element(self.driver,self.using[2], self.value[2]).click()   #账号注册
		self.element(self.driver,self.using[3], self.value[3]).click()   #返回
		el = self.element(self.driver,self.using[4], self.value[4])      #游客登录按钮
		print unicode('测试结果: %s' % el.get_attribute('name').encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[1].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el.get_attribute('name')), self.exp[1], self.case_id[1])  # 断言

	def test_202(self):
		u'''账号注册，输入为空'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[5], self.value[5]).click()   #新用户注册
		self.element(self.driver,self.using[6], self.value[6]).click()   #账号注册
		for i in xrange(10):
			self.element(self.driver,self.using[7], self.value[7]).click()   #下一步

			el = self.element_or_none(self.driver,self.using[8], self.value[8])      #提示
			if el.text!= None:
				break
		try:
			print unicode('测试结果: %s' % el.text.endoce('utf-8'))
			print unicode('预期结果: %s' % self.exp[15].encode('utf-8'))
			self.dy_Equal(self.driver,unicode(el.text),self.exp[15],self.case_id[15]) #断言
		except:
			print unicode('测试结果: %s' % el)
			print unicode('预期结果: 元素不为空' )
			self.dy_IsNotNone(self.driver,el,self.case_id[15])


	def test_203(self):
		u'''账号注册，输入3位数字，密码5位数字，确认密码与密码一致'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[9], self.value[9]).click()   #新用户注册
		self.element(self.driver,self.using[10], self.value[10]).click()   #账号注册

		el1 = self.element(self.driver,self.using[11], self.value[11])  # 账号输入框
		el1.send_keys(self.preset[11].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[12], self.value[12])   #密码输入框
		el2.send_keys(self.preset[12].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[13], self.value[13])   #确认密码输入框
		el3.send_keys(self.preset[13].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[14], self.value[14]).click()   #下一步
			el4 = self.element(self.driver,self.using[15], self.value[15])      #提示
			if el4.text != None:
				break
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[9].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[9], self.case_id[9])  # 断言

	def test_204(self):
		u'''账号注册，输入4位数字（用户名已被使用），密码6位字母，确认密码与密码一致     '''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[16], self.value[16]).click()   #新用户注册
		self.element(self.driver,self.using[17], self.value[17]).click()   #账号注册

		el1 = self.element(self.driver,self.using[18], self.value[18])  # 账号输入框
		el1.send_keys(self.preset[18].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[19], self.value[19])   #密码输入框
		el2.send_keys(self.preset[19].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[20], self.value[20])   #确认密码输入框
		el3.send_keys(self.preset[20].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[21], self.value[21]).click()   #下一步
			el4 = self.element(self.driver,self.using[22], self.value[22])      #提示
			if el4.text != None:
				break
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[16].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[16], self.case_id[16])  # 断言

	def test_205(self):
		u'''账号注册，输入9位字母，密码为空，确认密码与密码不一致     '''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[23], self.value[23]).click()   #新用户注册
		self.element(self.driver,self.using[24], self.value[24]).click()   #账号注册

		el1 = self.element(self.driver,self.using[25], self.value[25])  # 账号输入框
		el1.send_keys(self.preset[25].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[26], self.value[26])   #密码输入框
		el2.send_keys(self.preset[26].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[27], self.value[27])   #确认密码输入框
		el3.send_keys(self.preset[27].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[28], self.value[28]).click()   #下一步
			el4 = self.element(self.driver,self.using[29], self.value[29])      #提示
			if el4.text != None:
				break

		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[23].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[23], self.case_id[23])  # 断言

	def test_206(self):
		u'''账号注册，输入14位（中英数），密码7位（英数），确认密码为空     '''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[30], self.value[30]).click()   #新用户注册
		self.element(self.driver,self.using[31], self.value[31]).click()   #账号注册

		el1 = self.element(self.driver,self.using[32], self.value[32])  # 账号输入框
		el1.send_keys(self.preset[32].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[33], self.value[33])   #密码输入框
		el2.send_keys(self.preset[33].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[34], self.value[34])   #确认密码输入框
		el3.send_keys(self.preset[34].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[35], self.value[35]).click()   #下一步
			el4 = self.element(self.driver,self.using[36], self.value[36])      #提示
			if el4.text != None:
				break
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[30].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[30], self.case_id[30])  # 断言

	def test_207(self):
		u'''账号注册，输入15位（英数符），密码11位（英数），确认密码与密码一致'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[37], self.value[37]).click()   #新用户注册
		self.element(self.driver,self.using[38], self.value[38]).click()   #账号注册

		el1 = self.element(self.driver,self.using[39], self.value[39])  # 账号输入框
		el1.send_keys(self.preset[39].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[40], self.value[40])   #密码输入框
		el2.send_keys(self.preset[40].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[41], self.value[41])   #确认密码输入框
		el3.send_keys(self.preset[41].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[42], self.value[42]).click()   #下一步

			el4 = self.element(self.driver,self.using[43], self.value[43])      #提示
			if el4.text != None:
				break
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[37].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[37], self.case_id[37])  # 断言

	def test_208(self):
		u'''账号注册，输入16位（英数），密码21位（英数），确认密码与密码一致'''
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[44], self.value[44]).click()   #新用户注册
		self.element(self.driver,self.using[45], self.value[45]).click()   #账号注册

		el1 = self.element(self.driver,self.using[46], self.value[46])  # 账号输入框
		el1.send_keys(self.preset[46].encode('utf-8').decode("utf-8"))  # 输入

		el2 = self.element(self.driver,self.using[47], self.value[47])   #密码输入框
		el2.send_keys(self.preset[47].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[48], self.value[48])   #确认密码输入框
		el3.send_keys(self.preset[48].encode('utf-8').decode("utf-8"))  # 输入
		for i in xrange(10):
			self.element(self.driver,self.using[49], self.value[49]).click()   #下一步
			el4 = self.element(self.driver,self.using[50], self.value[50])      #提示
			if el4.text != None:
				break
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[44].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[44], self.case_id[44])  # 断言

	def test_209(self):
		u'''账号注册，注册成功，进入绑定手机界面'''
		#随机账号
		a = xrange(100,1000000000000000)
		b = random.choice(a)
		try:
			self.element(self.driver,'name', '显示登录UI').click()
		except:pass
		self.element(self.driver,self.using[51], self.value[51]).click()   #新用户注册
		self.element(self.driver,self.using[52], self.value[52]).click()   #账号注册

		el1 = self.element(self.driver,self.using[53], self.value[53])  # 账号输入框
		el1.send_keys(b)  # 输入

		el2 = self.element(self.driver,self.using[54], self.value[54])   #密码输入框
		el2.send_keys(self.preset[54].encode('utf-8').decode("utf-8")) #输入

		el3 = self.element(self.driver,self.using[55], self.value[55])   #确认密码输入框
		el3.send_keys(self.preset[55].encode('utf-8').decode("utf-8"))  # 输入

		self.element(self.driver,self.using[56], self.value[56]).click()   #下一步
		sleep(5)
		self.element(self.driver,self.using[57], self.value[57]).click()     #绑定手机
		el4 = self.element(self.driver,self.using[58], self.value[58])      #提示
		print unicode('测试结果: %s' % el4.text.encode('utf-8'))
		print unicode('预期结果: %s' % self.exp[51].encode('utf-8'))
		self.dy_Equal(self.driver, unicode(el4.text), self.exp[51], self.case_id[51])  # 断言


