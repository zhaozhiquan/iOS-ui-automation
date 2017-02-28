#!/usr/bin/env python
#coding=utf-8
import xlrd
import os
class Case_xls(object):

	def get_row(self,values):
		self.values = values
		#获取第N行内容
		self.xl = xlrd.open_workbook(os.getcwd() + os.sep + 'public/iOSSdk_case.xlsx')
		self.table = self.xl.sheets()[0]
		self.row = self.table.row_values(self.values)
		return self.row
	def get_col(self,values):
		self.values = values
		#获取第N列内容
		self.xl = xlrd.open_workbook(os.getcwd()+os.sep+'public/iOSSdk_case.xlsx')
		self.table = self.xl.sheets()[0]
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
	c = a.get_col(4)
	print c



		


		

