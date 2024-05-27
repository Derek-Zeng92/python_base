
# 1.  确定 在文件 离储存的账号信息的结构

# 2.  把账户数据读到内存，为了方便调用，可以改成list
accounts={

}
with open('account.db','r') as f:
    for line in f:
        line=line.strip().split(',')
        accounts[line[0]]=line
print(accounts)
# 3.  搞个loop，要求用户输入账号信息，去判断就可以了
while True:
    user=input('Username:').strip()
    if user not in accounts: # 用户未注册
        print('该用户未注册...')
        continue
    elif accounts[user][2]=='1':
        print(f'{user}此账户已锁定请联系管理员...')
        exit('bye...')

    count = 0
    while count<3: # 控制密码
        password=input('Password:').strip()
        if password==accounts[user][1]: # 去账号dict里判断密码是否正确
            print(f'Welcome{user}...登录成功...')
            exit('bye...')
            break
        else:
            print('wrong password...')

        count+=1
        if count==3:
            print(f'输错了{count}次密码，该账号已锁定...')
            # 1. 先改内存中的dict账号信息的 用户状态
            # 2. 把dict里的数据按account.db数据格式，并且 存回文件
            accounts[user][2]='1'

            with open('account.db','w') as f2:
                for user,val in accounts.items():
                    line=','.join(val)+'\n' # 把列表再转成字符
                    f2.write(line)
                f2.close()

                exit('bye...')