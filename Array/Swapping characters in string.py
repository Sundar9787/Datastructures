str = 'Bluecolour'
ch1 = 'o'
ch2 = 'l'
def replace(str,ch1,ch2):
    temp = '#'
    str = str.replace(ch1,temp)
    str = str.replace(ch2,ch1)
    str = str.replace(temp,ch2)
    return str
    
print(replace(str,ch1,ch2))
