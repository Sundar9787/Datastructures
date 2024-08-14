#removing duplicates from array 
arr =[1,2,1,3,2,3,4]
def find_dup(arr):
    n = len(arr)
    count=[0] * n
    duplicates=[]
    
    for num in arr:
        count[num] = count[num] + 1 
        
    for i in range(n):
        if count[i] > 1:
            duplicates.append(i)
            
    if duplicates:
        return sorted(duplicates)
    
    else:
        return -1
        
print(find_dup(arr))
