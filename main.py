def rotate(arr):
    r = []
    arr.reverse()
    r.append(arr[0])
    a = len(arr)- 1
    while a > 0:
        r.append(arr[a])
        a -= 1
    return r
