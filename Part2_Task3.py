# 1					
# 1	3				
# 1	3	5			
# 1	3	5	7		
# 1	3	5	7	9	
# 1	3	5	7	9	11


for rows in range(6):
    temp=1
    for col in range(rows+1):
        print(temp,end=" ")
        temp+=2               #in col's
    print()
    
    
    
    """_summary_
    Row==0  #(0,1,2,3,4,5)
    row in range(6) True
    temp=1
    col==0  in range 0 T    range(1)   =0
    1 
    temp=1+2=3
    temp=3
    col==c_col+step_v=0+1=1  in range 1  F
    row=c_row+step=0+1=1 #(0,1,2,3,4,5)  T
    row in range(6) True
    temp=1
    -------
    --------

    """
   