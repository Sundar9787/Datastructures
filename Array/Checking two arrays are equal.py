arr1=[1,2,5,4,0]
arr2=[2,4,5,0,1]
class Solution:
    # Function to check if two arrays are equal or not.
    def check(arr1, arr2) -> bool:
        #code here
        for num in arr1:
            ele_1 = num
        for num in arr2:
            ele_2 = num
            
        if ele_1 == ele_2:
            return True
        else:
            return False
    print(check(arr1,arr2))
