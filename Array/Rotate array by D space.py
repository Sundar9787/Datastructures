def rotate_left(arr, d):
    n = len(arr)
    d = d % n  # In case d is greater than n
    return arr[d:] + arr[:d]

# Example usage
arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = rotate_left(arr, d)
print(rotated_arr)  
