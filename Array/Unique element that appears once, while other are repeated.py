arr = [1,1,2,3,3,4,4]
n = len(arr)
left = 0
right = n -1
 
while left < right:
    mid = left + (right-left)//2
    
    if mid%2==1:
        mid = mid-1
        
    if arr[mid] == arr[mid+1]:
        left = mid + 2
        
    else:
        right = mid
        
print(arr[left])
