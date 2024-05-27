
for i in range(1,6):
    print(f'-------{i}楼--------')

    if i == 3:  # L3,跳过
        continue
    for j in range(1,9):
        if i==4 and j==4:
            print('遇到鬼屋404，over了')
            break
        print(f'L{i}-{i}0{j}室')