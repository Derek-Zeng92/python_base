import random

# random.randrange(1,10) #返回1-10之间的⼀个随机数，不包括10
# random.randint(1,10) #返回1-10之间的⼀个随机数，包括10
# random.randrange(0, 100, 2) #随机选取0到100间的偶数
# random.random() #返回⼀个随机浮点数
# random.choice('abce3#$@1') #返回⼀个给定数据集合中的随机字符
# random.sample('abcdefghij',3) #从多个字符中选取特定数量的字符

print(random.random())

#⽣成随机字符串
import string
a=''.join(random.sample(string.ascii_lowercase + string.digits, 6))
print(a)

#洗牌
b=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.shuffle(b))
