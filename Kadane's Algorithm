#code
import sys
minVal = -sys.maxsize -1
test = int(input())
def kadanesAlgo(arr):
    sum_till_now = global_sum = minVal
    for i in range(0,len(arr)):
        sum_till_now = max(arr[i],sum_till_now+arr[i])
        global_sum =  max(global_sum,sum_till_now)
    return global_sum
while test >0:
    length = int(input())
    arr = list(map(int,input().strip().split()))
    # print(arr)
    print(kadanesAlgo(arr))
    test -=1
