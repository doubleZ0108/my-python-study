from random import randint

# 冒泡排序
def BubbleSort(arr, cmp=lambda x,y: x<y):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(0,len(arr)-i-1):
            if cmp(arr[j+1],arr[j]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# 鸡尾酒排序
def CocktailSort(arr, cmp=lambda x,y: x<y):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(0,len(arr)-i-1):
            if cmp(arr[j+1],arr[j]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True

        if swapped:
            swapped = False
            for j in range(len(arr)-i-2,i,-1):
                if cmp(arr[j],arr[j-1]):
                    arr[j-1],arr[j] = arr[j],arr[j-1]
                    swapped = True
        
        if not swapped:
            break

# 选择排序
def SelectSort(arr, cmp=lambda x,y: x<y):
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1, len(arr)):
            if cmp(arr[j],arr[minindex]):
                minindex = j
        if minindex != i:
            arr[minindex],arr[i] = arr[i],arr[minindex]
    return arr

# 归并排序
def MergeSort(arr, cmp=lambda x,y: x<y):
    if len(arr)<2:
        return arr[:]
    mid = len(arr)//2
    left = MergeSort(arr[:mid], cmp)
    right = MergeSort(arr[mid:], cmp)
    return merge(left, right, cmp)

def merge(arr1, arr2, cmp):
    merged_arr = []
    index1,index2 = 0,0
    while index1<len(arr1) and index2<len(arr2):
        if cmp(arr1[index1],arr2[index2]):
            merged_arr.append(arr1[index1])
            index1 += 1
        else:
            merged_arr.append(arr2[index2])
            index2 += 1

    merged_arr += arr1[index1:]
    merged_arr += arr2[index2:]
    return merged_arr

# 快速排序
def QuickSort(arr):
    arr = quick_sort(arr,0,len(arr)-1)
    return arr

def quick_sort(arr, low, high):
    if low>= high:
        return arr

    i,j = low, high
    key = arr[low]
    while low < high:
        while low<high and arr[high]>=key:
            high -= 1
        if arr[high]<key:
            arr[low],arr[high] = arr[high],arr[low]
            low += 1
        while low<high and arr[low]<=key:
            low += 1
        if arr[low]>key:
            arr[low],arr[high] = arr[high],arr[low]
            high -= 1
    arr[low] = key

    quick_sort(arr,i,low-1)
    quick_sort(arr,low+1,j)
    return arr


if __name__ == "__main__":
    MaxSize = 10
    arr = [0]*MaxSize
    for i in range(len(arr)):
        arr[i] = randint(0,100)

    # sorted_arr = BubbleSort(arr)
    # sorted_arr = CocktailSort(arr)
    # sorted_arr = SelectSort(arr)
    # sorted_arr = MergeSort(arr)
    # sorted_arr = QuickSort(arr)


    for arg in sorted_arr:
        print(arg, end=' ')
    print()
