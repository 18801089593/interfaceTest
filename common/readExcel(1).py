import xlrd


class readExcel():
    readbook = xlrd.open_workbook(r'D:\interfaceTest\testDate\data.xls')
    # 根据sheet索引或者名称获取sheet内容
    urlSheet = readbook.sheet_by_name('urlSheet')
    paramSheet = readbook.sheet_by_name('paramSheet')
    assertSheet = readbook.sheet_by_name('assertSheet')
    rownum = urlSheet.nrows


    def urlSheet1(self):
        urlList = []
        #获取interface列表
        # print(self.rownum)
        for i in range(1,self.rownum):
            rowvalue = self.urlSheet.row_values(i)
            urlList.append(rowvalue)
        return urlList

    def paramSheet1(self):
        paramList = []
        #获取param列表
        for i in range(1,self.rownum):
            rowvalue = self.paramSheet.row_values(i)
            # print(rowvalue)
            paramList.append(rowvalue)
        return paramList

    def assertSheet1(self):
        assertList = []
        #获取assert列表
        for i in range(1,self.rownum):
            rowvalue = self.assertSheet.row_values(i)
            # print(rowvalue)
            assertList.append(rowvalue)
        return assertList

    #组装所有的接口请求参数为一个list，一个元素包含：id,url,methode,param,expect
    def getData(self):
        urlList = self.urlSheet1()
        paramList = self.paramSheet1()
        assertList = self.assertSheet1()
        dataList = []
        # print(urlList)
        for a,b,c,d in urlList:
            singleList = []
            # print(a,b,c,d)
            id = int(a)
            url = b
            method = d
            param = paramList[id-1][1]
            expect = assertList[id-1][1]
            singleList.append(id)
            singleList.append(url)
            singleList.append(method)
            singleList.append(param)
            singleList.append(expect)
            dataList.append((singleList))
            # print('----single',dataList)
        print('----data', dataList)
        return dataList

read = readExcel()
read.getData()