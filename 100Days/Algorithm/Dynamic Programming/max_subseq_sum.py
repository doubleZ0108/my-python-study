'''
动态规划法

最大子列和
'''

# 动态规划法
def dp(arr):
    overall,partical = {},{}
    overall[0] = partical[0] = arr[0]
    for i in range(1,len(arr)):
        partical[i] = max(partical[i-1]+arr[i], arr[i])
        overall[i] = max(overall[i-1], partical[i])
    return overall[len(arr)-1]

# 在线处理方法
def online(arr):
    thisSum, maxSum = 0,arr[0]
    for i in range(len(arr)):
        thisSum += arr[i]
        maxSum = thisSum if thisSum>maxSum else maxSum
        thisSum = 0 if thisSum<0 else thisSum
    return maxSum


if __name__ == "__main__":
    arr = list(map(int, input('请输入序列: ').split(' ')))
    print(online(arr))
    print(dp(arr))
