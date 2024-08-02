#finding third highest value
arr = [12,45,34,82,98,110,120,32]
first = second = third = 0 
for num in arr:
    if num > first :
        third = second
        second = first 
        first = num 
        
    elif num > second and num!= first :
        third = second
        second =num
        
    
    elif num > third and num!=second and num!=first:
        third = num
        
print(f'Second highest value {second}')        
print(f'Third highest value {third}')
