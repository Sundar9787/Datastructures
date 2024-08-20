arr=[1,2,3,6,7,3,2,5,4,6]
freq ={}
def frequencycount(arr,freq):
    for num in arr:
        if num in freq:
            freq[num]= freq[num] + 1
            
        else:
            freq[num] = 1
            
        
    return freq
    
print(frequencycount(arr,freq))
