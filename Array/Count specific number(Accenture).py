m = int(input('Enter M : '))
n = int(input('Enter N : '))
def CountSpecificNumbers(m, n):
    a=[]
    if m > n:
        return -1
    
    for i in range(m, n + 1):
        num_str = str(i)
        if all(digit in '149' for digit in num_str):
            a.append(i)
    
    return a

print(CountSpecificNumbers(m, n))
