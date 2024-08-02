#finding missing number
arr =[1,2,3,5,6]
def  finding_missing(arr):
    n = len(arr) + 1 
    total_sum = sum(arr)
    series = n *(n+1)//2
    missing_value = series - total_sum
    return missing_value

print(f'Missing Value is {finding_missing(arr)}')
