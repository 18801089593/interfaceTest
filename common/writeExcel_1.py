import xlrd
from xlutils.copy import copy
import os


class writeExcel(object):

    rb = xlrd.open_workbook(r'D:\interfaceTest\testDate\data.xls')
    # rs = rb.sheet_by_index(2)
    wb = copy(rb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(2)


    def writeData(self,id,real,status):
        try:
            print('写入')
            #根据id写入对应的实际结果和接口测试状态
            self.ws.write(id,2,real)
            self.ws.write(id,3,status)
            self.wb.save('D:/interfaceTest/testDate/data_1.xls')
            return 'ok'
        except Exception as msg:
            print(msg)