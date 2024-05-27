
with open('兼职白领学生空姐模特护士联系方式.txt','r+',encoding='utf-8') as f:

    # 1.加载到内存
    data=f.read()
    new_data=data.replace('马马纤','邓紫棋')

    # 2.清空文件
    f.seek(0)
    f.truncate() # 截断文件

    # 3.把新内容重新写回硬盘
    f.write(new_data)

    f.close()