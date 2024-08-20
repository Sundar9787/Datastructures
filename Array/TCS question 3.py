N = int(input('Enter N value : '))
R = int(input('Enter R value : '))
def intelligence(N,R):
     N_str = str(N)
     digit =[int(digit) for digit in N_str]
     sum_val = sum(digit)
     rep = sum_val *  R 
     rep_str = str(rep)
     d_2 = [int(d_2) for d_2 in rep_str]
     ans = sum(d_2)
     return ans
     
print(intelligence(N,R))
