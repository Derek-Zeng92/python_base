
# w+ 写读模式，它会创建一个新文件写一段内容，可以再把写的内容读出来
# r+ 读写模式，但是写在文件最后，和追加一样
# a+ 追加读模式，文件一打开光标会在文件尾部，写的数据全会是追加的形式

with open('嫩模联系方式.txt','r+',encoding='utf-8') as f:
    print(f.readline())
    print(f.tell())
    f.write('又来一个新模特...')