
with open('嫩模联系方式.txt','r',encoding='utf-8') as f:
    for line in f:
        line=line.split()
        height=int(line[3])
        weight=int(line[4])

        if height>=170 and weight<=50:
            print(line)