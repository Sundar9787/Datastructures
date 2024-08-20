N = int(input('Enter no of elements : '))
arr=[]
for i in range(N):
    element = int(input(f'Enter element {i +1} : '))
    arr.append(element)
    
Date = int(input('Enter date: '))
fine = int(input("Enter fine amount : "))

def finecollection(N,arr,Date,fine):
    total_fine = 0
    if Date%2 == 0 :
        for num in arr:
            if num%2 != 0:
                total_fine = total_fine + fine
        return total_fine
    else:
        for num in arr:
            if num%2 == 0 :
                total_fine = total_fine + fine
                
        return  total_fine
        
print(finecollection(N,arr,Date,fine))
                
    
                
                
