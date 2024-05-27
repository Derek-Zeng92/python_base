
def calc(x,y):
    res=x**y
    print(res)

a=5
b=4
calc(a,b)

# 非固定参数
def stu_register(*args,**kwargs): # *args 会把多传入的参数变成一个元组形式  **kwargs是一个dict
    print(args)
    print(f'''
------info-----
Name:{args[0]}
Age:{args[1]}
sex:{args[2]}
Hobbie:{kwargs.get('Hobbie')}
''')
    return args[0],args[1],args[2],kwargs.get('Hobbie')

print(stu_register('Alex',22,'男',addr='成都市',Hobbie='弹吉他'))


