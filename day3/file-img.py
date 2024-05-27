
# 二进制读rb
# with open('login_bg.jpg','rb') as f:
#     for line in f:
#         print(line)


# 二进制写rb
with open('wb_file.txt','wb') as f:
    s='路飞'
    f.write(s.encode('utf-8'))