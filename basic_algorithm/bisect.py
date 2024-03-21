def bisect(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left+right) // 2
        if target < arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(bisect([10,20,30,40,50,60,70], 65))