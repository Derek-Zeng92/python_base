# datetime.date：表示⽇期的类。常⽤的属性有year, month, day；
# datetime.time：表示时间的类。常⽤的属性有hour, minute, second, microsecond；
# datetime.datetime：表示⽇期时间。
# datetime.timedelta：表示时间间隔，即两个时间点之间的⻓度。
# datetime.tzinfo：与时区有关的相关信息。（这⾥不详细充分讨论该类，感兴趣的童鞋可以参考
# python⼿册）

import datetime
d=datetime.datetime.now()
print(d)
print(datetime.datetime.fromtimestamp(234324233))
print(d+datetime.timedelta(days=5))# 时间运算

print(d.replace(year=2120,month=5,day=5)) #时间替换