string = input('Enter string : ')
vowels = ['a','e','i','o','u']
def check(string,vowels):
    for char in string:
        if char in vowels:
          return True
        else:
            return False
            
            
print(check(string,vowels))
    
