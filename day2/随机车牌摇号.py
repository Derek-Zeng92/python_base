import random
import string

str=string.ascii_uppercase+string.digits
s=random.choice(string.ascii_uppercase)  #生成第一个字母

random.randint(0,10) #打印一个随机数

count =0
while count<3:
    car_nums=[]
    count+=1
    for i in range(20):
        num = ''.join(random.sample(str, 5))
        c_num=f'川{s}.{num}'
        car_nums.append(c_num)# 把生成的车牌号添加到数组
        print(i+1,c_num)

    choice=input('请输入你喜欢的号：').strip()#去掉空格
    if choice in car_nums:
        print(f'恭喜你选择了新车牌号：{choice}')
        exit('good luck.')
    else:
        print('仓库内没有该车牌号，请重新选择一个用户只有3次机会请注意！')