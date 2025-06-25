#  0  1  2 3  4
#0 A				
#1 A  A			
#2 A	A		
#3 A	   A	
#4 A  A	A  A  A

for row in range(5):
    for col in range(5):
        if col ==0 or row==4 or (row-col==0) :
            print("A",end=" ")
        else:
            print("",end="  ")
    print()