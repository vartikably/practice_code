#imput the length of array
n = int(input())
#input for array
arr = list(map(int,input().split()))
max1 = -2147483648
min1 = 2147483647
max2 = -2147483648
min2 = 2147483647
for i in range(0,n):
    max1 = max(max1,arr[i]+i)
    min1 = min(min1,arr[i]+i)
    max2 = max(max2, arr[i] - i)
    min2 = min(min2, arr[i] - i)
print(max(max1-min1,max2-min2))
