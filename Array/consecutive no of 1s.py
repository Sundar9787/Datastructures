#counting consecutive no of 1s

arr=[1,1,0,3,4,5,1,1,1,1,2,3,1,1,0,41,1,1,1]
max_count = 0
current_count = 0 
for num in arr:
    if num == 1 :
        current_count = current_count + 1 
        max_count = max(current_count,max_count)
    
    else:
        current_count = 0
        
print(max_count)
