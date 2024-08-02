arr_1=[1,2,4,5,6]
arr_2=[2,3,5,7,8]
seen = arr_1
def merge_array(arr_1,arr_2):
    for element  in arr_2:
        if element not in seen:
            arr_1.append(element)
    return sorted(arr_1)

print(merge_array(arr_1,arr_2))
