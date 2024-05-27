import time

# time.localtime([secs]) ：将⼀个时间戳转换为当前时区的struct_time。若secs参数未提供，
# 则以当前时间为准。
# time.gmtime([secs]) ：和localtime()⽅法类似，gmtime()⽅法是将⼀个时间戳转换为UTC时区
# （0时区）的struct_time。
# time.time() ：返回当前时间的时间戳。
# time.mktime(t) ：将⼀个struct_time转化为时间戳。
# time.sleep(secs) ：线程推迟指定的时间运⾏,单位为秒。
# 索引（Index） 属性（Attribute） 值（Values）
# 0 tm_year（年） ⽐如2011
# 1 tm_mon（⽉） 1 - 12
# 2 tm_mday（⽇） 1 - 31
# 3 tm_hour（时） 0 - 23
# 4 tm_min（分） 0 - 59
# 5 tm_sec（秒） 0 - 61
# 6 tm_wday（weekday） 0 - 6（0表示周⼀）
# 7 tm_yday（⼀年中的第⼏天） 1 - 366
# 8 tm_isdst（是否是夏令时） 默认为-1
# time.strftime(format[, t]) ：把⼀个代表时间的元组或者struct_time（如由
# time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传⼊
# time.localtime()。
# 举例： time.strftime(“%Y-%m-%d %X”, time.localtime()) #输出’2017-10-01
# 12:14:23’
# time.strptime(string[, format]) ：把⼀个格式化时间字符串转化为struct_time。实际上它
# 和strftime()是逆操作。
# 举例： time.strptime(‘2017-10-3 17:54’,”%Y-%m-%d %H:%M”) #输出
# time.struct_time(tm_year=2017, tm_mon=10, tm_mday=3, tm_hour=17, tm_min=54,
#                  tm_sec=0, tm_wday=1, tm_yday=276, tm_isdst=-1)

print(time.gmtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
