#!/usr/bin/env python
#coding=utf-8
import xlrd
import os
class Case_xls(object):
	def get_row(self, xls_list, values):
		self.xls_list = xls_list
		self.values = values
		print os.getcwd()+ os.sep
		# 获取第N行内容
		if os.getcwd() + os.sep == '/Users/zhaozhiquan/automation/iOSSdk/TestCase/':
			self.xl = xlrd.open_workbook(os.getcwd() + os.sep+'../public/iOSSdk_case.xlsx')

		elif os.getcwd() + os.sep == '/Users/zhaozhiquan/automation/iOSSdk/public/':
			self.xl = xlrd.open_workbook(os.getcwd() + os.sep+'iOSSdk_case.xlsx')

		else:
			self.xl = xlrd.open_workbook(os.getcwd() + os.sep + 'public/iOSSdk_case.xlsx')
		self.table = self.xl.sheets()[self.xls_list]
		self.row = self.table.row_values(self.values)
		return self.row
	def get_col(self,xls_list,values):
		self.xls_list = xls_list
		self.values = values

		#获取第N列内容
		if os.getcwd() + os.sep == '/Users/zhaozhiquan/automation/iOSSdk/TestCase/':
			self.xl = xlrd.open_workbook(os.getcwd() + os.sep+'../public/iOSSdk_case.xlsx')

		elif os.getcwd() + os.sep == '/Users/zhaozhiquan/automation/iOSSdk/public/':
			self.xl = xlrd.open_workbook(os.getcwd() + os.sep+'iOSSdk_case.xlsx')

		else:
			self.xl = xlrd.open_workbook(os.getcwd() + os.sep + 'public/iOSSdk_case.xlsx')
		self.table = self.xl.sheets()[self.xls_list]
		self.col = self.table.col_values(self.values)
		return self.col
	def get_danyuange(self,hang,lie):
		self.hang = hang
		self.lie = lie
		self.xl = xlrd.open_workbook(os.getcwd() + os.sep + 'public/iOSSdk_case.xlsx')
		self.table = self.xl.sheets()[0]
		b = self.table.cell(self.hang,self.lie).value.encode('utf-8')
		return b
if __name__ == '__main__':
	a = Case_xls()
	c = a.get_row(0,0)
	print c



		


		

