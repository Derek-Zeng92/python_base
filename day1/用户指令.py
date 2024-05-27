
# A 90-100
# B 80-89
# C 60-79
# D 40-59
# E 0-39

performance=int(input('请输入你这学期的成绩：'))

if performance>=90:
    print('你的成绩评级为：A')
elif performance>=80:
    print('你的成绩评级为：B')
elif performance>=60:
    print('你的成绩评级为：C')
elif performance>=40:
    print('你的成绩评级为：D')
else:
    print('你的成绩评级为：E')