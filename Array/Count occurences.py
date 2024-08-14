l = int(input('Enter l value : '))
u = int(input('Enter u value : '))
x = int(input('Enter x value : '))
def Countdigitoccurences(l,u,x):
    count = 0
    x_str = str(x)
    for i in range(l,u+1):
        i_str = str(i)
        for digit in i_str:
            if digit == x_str:
                count = count + 1
            
    return count
        
        
print(f'The count of {x} is : ',Countdigitoccurences(l,u,x))

