# 1	1	1	1	1
# 3				3
# 5				5
# 7				7
# 9	9	9	9	9
temp=1
for row in range(5):
    for col in range(5):
        if row ==0 or row==4 or col==0 or col==4:
            print(temp,end="  ")
        else:
            print("",end="   ")
    print()
    temp=temp+2