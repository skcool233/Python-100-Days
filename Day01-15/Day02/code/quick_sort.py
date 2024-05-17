def qq(arr):
    if len(arr) <= 1:
        return arr
    else:
        key = arr[0]
        left = [x for x in arr[1:] if x <= key]
        right = [x for x in arr[1:] if x > key]
        return qq(left) + [key] + qq(right)


arr = [5, 4, 3, 2, 1]
print(qq(arr))