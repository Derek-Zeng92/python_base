import random
company_staffs=[]

for i in range(0,300):
    company_staffs.append(f'员工_{i}')

def draw_lottery(count,content):
    win_p=[]
    for i in range(1,count+1):
        win_num=random.randint(0, len(company_staffs))
        win_p.append(company_staffs[win_num])
        del company_staffs[win_num]

    print(f'{content}中奖员工：{win_p}')

draw_lottery(3,'一等奖：泰国5日游+手术报销费')
draw_lottery(6,'二等奖：iPhone20Pro手机')
draw_lottery(30,'三等奖：三斤苹果')