
# abs 取绝对值
# print(abs(-10))

# all 所有值都是Ture才会返回Ture
# a=[1,2,3,4,5,6,7]
# a=[1,2,3,4,5,6,7,0]
# print(all(a))

# any，任意一个值为True
# a=[1,2,3,4,5,6,7,0]
# a=[0,0]
# print(any(a))

# chr获取码表
# print(chr(97))

# dict 生成一个字典
# print(dict())
# print(dict(name='alex',age=28))

# dir 打印当前环境所有变量
# print(dir())

# locals() 打印当前作用域所有键值对
# name='alex'
# age=22
# print(locals())

# map() map循环
# t=range(10)
# print(t)
# def calc(x):
#     return x**2
# m=map(calc,t)# 并没有执行（迭代器）
# for i in m: #每循环一次，就把列表里的每一个元素扔给calc函数执行
#     print(i)

# max,min,sum  最大值，最小值，求和
# l=range(10)
# print(max(l))
# print(min(l))
# print(sum(l))

# ord() 和chr相反
# print(ord('a'))

# round 保留几位小数
# print(round(3.145674,2))

# type 看数据类型
# print(type('fsdf'))

# zip()  配对
# a=['alex','jery','rain']
# b=['rose','cicy']
#
# for i in zip(a,b):
#     print(i)

# filter() 把列表里的每个元素交给第一个参数(函数)运行，若结果为真就保留这个值
l = list(range(10))

def compare(x):
    if x>5:
        return x
print(l)
for i in filter(compare,l):
    print(i)