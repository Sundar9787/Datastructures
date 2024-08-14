arr=[1,2,3,4,5,6,7,8]
n = 6
left = 0
right = len(arr)-1

while left <= right:
    mid = (left + right) //2

    if n == arr[mid]:
        print(f'Element found at position {mid}')
        break
    elif n > arr[mid]:
        left = mid + 1 
    
    elif n < arr[mid]:
        right = mid - 1 
        
else:
    print('Element not found')
