#
#
# #zip用法
a= [1,2,3]
b = ['a','b','c']
c = ['4','5','6']
#
# # print(list(zip(a,b,c)))
d = list(zip(a,b,c))
print('dddd',d)
#
# #第一种方法
n=[]
for a,b,c in d:
    n.append((a,c))

print(n)
#
#
# #第二种方法
# a = []
# for i in d:
#     print('---i',i)
#     a.append((i[0],i[-1]))
#     a.append(i[-1])
#     print(a)
#








