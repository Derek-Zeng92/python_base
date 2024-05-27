
# 1. 数据存到文件里的格式
#     姓名，年龄，手机，身份证，学科
# 2.实现手机号、身份证，在文件里同样的数据只有一条。可以把文件里的手机、身份证这2列加载到内存里以列表的形式判断
# 3. 选学科时，给用户列出选项，供选择
db_file= 'student_data.db.txt'

def validate_phone(num):
    if not num.isdigit():
        exit('手机号必须是数字...')
    elif len(num)!=11:
        exit('手机号不是11位号码...')
    elif num in phone_list:
        exit('该手机已注册...')
    return True

def register_api():
    stu_data={} # 初始化一个空学生信息
    print('欢迎来到风暴学院'.center(50,'-'))
    print('请完成学籍注册')
    name=input('姓名：').strip()
    age = input('年龄：').strip()
    phone = input('手机号：').strip()
    validate_phone(phone)# 手机号验证
    id_num = input('身份证号：').strip()
    if id_num in id_num_list:
        exit('该身份证号已注册...')

    course_list=['Python开发','Linux云计算','网络安全','web前端开发']
    for index,course in enumerate(course_list):
        print(f'{index}.{course}')

    select_course=input('选择想学的课：')
    if select_course.isdigit():
        select_course=int(select_course)
        if select_course>=0 and select_course <len(course_list):
            picked_course=course_list[select_course]#选中的可成
        else:
            exit('不合法的选项...')
    else:
        exit('非法输入...')

    stu_data['name']=name
    stu_data['age'] = age
    stu_data['phone'] = phone
    stu_data['id_num'] = id_num
    stu_data['course'] = picked_course

    return stu_data

def commit_to_db(filename,stu_data):
    """
    把学员数据，存到文件里
    :param filename:学员数据库文件
    :param stu_data:单个学员数据的dict
    :return:
    """
    with open(filename,'a',encoding='utf-8') as f:
        row = f"{stu_data['name']},{stuent_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}"
        f.write(row)
        f.close()

def load_validated_data(filename):
    with open(filename,encoding='utf-8') as f:
        phone_list=[]
        id_num_list=[]
        for line in f:
            line=line.split(',')
            phone=line[2]
            id_num=line[3]
            phone_list.append(phone)
            id_num_list.append(id_num)
        return phone_list,id_num_list

phone_list,id_num_list=load_validated_data(db_file)

stuent_data = register_api()
print(stuent_data)
commit_to_db(db_file,stuent_data)