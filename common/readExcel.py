
import xlrd
#找到并打开excel
class readExcel():
#找到并打开excel
    readbook = xlrd.open_workbook(r'D:\interfaceTest\testDate\data.xls')
    #sheet页列表
    sheetlist = readbook.sheet_names()
    sheetData = []
    # 读取表中数据
    def getData(self):
    #读取第一个sheet页数据
        sheet1 = self.readbook.sheet_by_index(0)
        sheet1_nrows = sheet1.nrows
        sheet1_ncols = sheet1.ncols
        sheetData1 = []
        for i in range(1,sheet1_nrows):
            row_values1 = sheet1.row_values(i)
            sheetData1.append(row_values1)
        #print('sheetData1',sheetData1)


        sheet2 = self.readbook.sheet_by_index(1)
        sheet2_nrows = sheet2.nrows
        sheet2_ncols = sheet2.ncols
        sheetData2 = []
        for i in range(1,sheet2_nrows):
            row_values2 = sheet2.row_values(i)
            sheetData2.append(row_values2)
        #print('sheetData2',sheetData2)


        sheet3 = self.readbook.sheet_by_index(2)
        sheet3_nrows = sheet1.nrows
        sheet3_ncols = sheet1.ncols
        sheetData3 = []
        for i in range(1, sheet3_nrows):
             row_values3 = sheet3.row_values(i)
             sheetData3.append(row_values3)
        #print('sheetData3',sheetData3)
        #
        #
        # for i in sheetData3[0][1]:
        #     sheetData2[0].append(i)
        # for i in sheetData2[0][1:]:
        #     sheetData1[0].append(i)
        # print(sheetData1[0])
        #
        #
        # for y in sheetData3[1][1]:
        #     sheetData2[1].append(y)
        # for z in sheetData2[1][1:]:
        #     sheetData1[1].append(z)
        # print(sheetData1[1])
        #
        #
        # for g in sheetData3[2][1]:
        #     sheetData2[2].append(g)
        # for h in sheetData2[2][1:]:
        #     sheetData1[2].append(h)
        # print(sheetData1[2])
        #
        # list = [sheetData1[0],sheetData1[1],sheetData1[2]]
        # print(list)



# print(list(zip(a,b,c)))
        d = (list(zip(sheetData1, sheetData2, sheetData3)))
        #print('dddd', d)

        a = []
        for i in d:
            #print('---i',i)
            #a.append((i[0][0:].append(i[1][1],i[2][1])))
            # i = ''.join((i[0][0:]))
            a.append((i[0][0],i[0][1],i[0][2],i[0][3],i[1][1],i[2][1]))
        a[0] = list(a[0])
        a[1] = list(a[1])
        a[2] = list(a[2])
        print(a)



read = readExcel()
read.getData()


















