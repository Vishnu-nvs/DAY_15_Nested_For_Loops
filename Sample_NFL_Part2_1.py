# A	 A	A	A	A
# A			A	
# A		A		
# A	A			
# A				

for row in range(5):
    for col in range(5):
        if row == 0 or col ==0 or row + col ==4:
            print("A",end="  ")
        else:
            print("",end="   ")
    print()