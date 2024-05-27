
with open('seek_write.txt','w') as f:
    f.write('hello1\n')
    print('返回光标当前位置：',f.tell())
    f.write('hello2\n')
    print('返回光标当前位置：', f.tell())
    f.write('hello3\n')
    f.seek(10)
    f.write('--------')