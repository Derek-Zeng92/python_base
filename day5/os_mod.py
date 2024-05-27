
import os

# 得到当前⼯作⽬录，即当前Python脚本⼯作的⽬录路径: os.getcwd()
# 返回指定⽬录下的所有⽂件和⽬录名:os.listdir()
# 函数⽤来删除⼀个⽂件:os.remove()
# 删除多个⽬录：os.removedirs（r“c：\python”）
# 检验给出的路径是否是⼀个⽂件：os.path.isfile()
# 检验给出的路径是否是⼀个⽬录：os.path.isdir()
# 判断是否是绝对路径：os.path.isabs()
# 检验给出的路径是否真地存:os.path.exists()
# 返回⼀个路径的⽬录名和⽂件名:os.path.split() e.g
# os.path.split('/home/swaroop/byte/code/poem.txt') 结果：
# ('/home/swaroop/byte/code', 'poem.txt')
# 分离扩展名：os.path.splitext() e.g os.path.splitext('/usr/local/test.py')
# 结果：('/usr/local/test', '.py')
# 获取路径名：os.path.dirname()
# 获得绝对路径: os.path.abspath()
# 获取⽂件名：os.path.basename()
# 运⾏shell命令: os.system()
# 读取操作系统环境变量HOME的值:os.getenv("HOME")
# 返回操作系统所有的环境变量： os.environ
# 设置系统环境变量，仅程序运⾏时有效：os.environ.setdefault('HOME','/home/alex')
# 给出当前平台使⽤的⾏终⽌符:os.linesep Windows使⽤'\r\n'，Linux and MAC使⽤'\n'
# 指示你正在使⽤的平台：os.name 对于Windows，它是'nt'，⽽对于Linux/Unix⽤户，它
# 是'posix'
# 2.2 time 模块
# 在平常的代码中，我们常常需要与时间打交道。在Python中，与时间处理有关的模块就包括：time，
# datetime,calendar(很少⽤，不讲)，下⾯分别来介绍。
# 我们写程序时对时间的处理可以归为以下3种：
# 时间的显示，在屏幕显示、记录⽇志等 "2022-03-04"
# 时间的转换，⽐如把字符串格式的⽇期转成Python中的⽇期类型
# 时间的运算，计算两个⽇期间的差值等
# 在Python中，通常有这⼏种⽅式来表示时间：
# 1. 时间戳（timestamp）, 表示的是从1970年1⽉1⽇00:00:00开始按秒计算的偏移量。例⼦：
# 1554864776.161901
# 2. 格式化的时间字符串，⽐如“2020-10-03 17:54”
# 3. 元组（struct_time）共九个元素。由于Python的time模块实现主要调⽤C库，所以各个平台可能
# 有所不同，mac上：time.struct_time(tm_year=2020, tm_mon=4, tm_mday=10, tm_hour=2,
#                                 tm_min=53, tm_sec=15, tm_wday=2, tm_yday=100, tm_isdst=0)
# 重命名：os.rename（old， new）
# 创建多级⽬录：os.makedirs（r“c：\python\test”）
# 创建单个⽬录：os.mkdir（“test”）
# 获取⽂件属性：os.stat（file）
# 修改⽂件权限与时间戳：os.chmod（file）
# 获取⽂件⼤⼩：os.path.getsize（filename）
# 结合⽬录名与⽂件名：os.path.join(dir,filename)
# 改变⼯作⽬录到dirname: os.chdir(dirname)
# 获取当前终端的⼤⼩: os.get_terminal_size()
# 杀死进程: os.kill(10884,signal.SIGKILL)

# 创建多级目录
# os.makedirs('c/d/e/f/g')
os.getcwd()

import sys

# 获取系统环境变量
print(sys.path)

# 获取脚本参数
# print(sys.argv)