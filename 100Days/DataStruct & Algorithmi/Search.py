from random import randint

# 顺序查找
def SequenceSearch(arr, key):
    for index, item in enumerate(arr):
        if item==key:
            return index
    return -1

# 折半查找
def BinarySearch(arr, key):
    start,end = 0,len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid]<key:
            start = mid + 1
        elif arr[mid]>key:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    MaxSize = 10
    arr = [0]*MaxSize
    for i in range(len(arr)):
        arr[i] = randint(0,100)
    arr.sort()
    print(arr)

    key = int(input('Please input a number: '))
    print(SequenceSearch(arr, key))
    print(BinarySearch(arr, key))
