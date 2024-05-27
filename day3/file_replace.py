
import sys

print(sys.argv)
old_str=sys.argv[1]
new_str=sys.argv[2]
filename=sys.argv[3]

with open(filename,'r+') as f:
    data=f.read()
    old_str_cont=data.count(old_str)
    new_data=data.replace(old_str,new_str)

    f.seek(0)
    f.truncate()

    f.write(new_data)

    f.close()
    print(f'成功替换字符{old_str}to{new_str},共{old_str_cont}次...')
