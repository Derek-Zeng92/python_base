
black_girl_age=26

count =0

while count<3:
    count+=1
    guess=int(input('年龄猜测，请输入你的猜测：'))

    if guess>26:
        print('打死你，你猜大了！')
    elif guess<26:
        print('-v-，有这么年轻吗？')
    else:
        print('恭喜你猜对了，翠花嫁给你')