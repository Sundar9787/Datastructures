N = int(input('Enter no of members : '))
ways = 1
def possible_ways(N,ways):
    for i in range(1,N):
        ways = ways * i 
        ans = ways * 2
        
    return ans
    
    
result = possible_ways(N,ways)
print(result)
    
