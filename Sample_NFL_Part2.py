# 1	1	1	1	1	1	1
# 1						1
# 1						1
# 1						1
# 1	1	1	1	1	1	1

temp=1
for row in range(5):
    for col in range(7):
        if row==0 or row==4 or col==0 or col==6:
            print(temp,end=" ")
        else:
            print("",end="  ")
    print()

