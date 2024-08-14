a = int(input('Enter apples : '))
m = int(input('Enter mangoes : '))
rs = int(input('Enter rupees: '))
def BalanceFruits(a,m,rs):
    if a > m :
        a = a - m 
        total_rupees = rs - a
    elif a < m :
        m = m - a 
        total_rupees = rs - m
    
    return total_rupees
    
print(BalanceFruits(a,m,rs))
    
