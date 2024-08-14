arr_1=([1,2,3,4,5,9])
arr_2=([2,6,7,8,9,10])
intersection =[]

intersection= set(arr_1) & set(arr_2)

print(sorted(list(intersection)))
