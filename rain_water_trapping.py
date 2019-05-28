import sys
def rain_water_trapping(arr):
    l_arr = [None]*len(arr)
    r_arr = [None]*len(arr)
    max_l =max_r= -(sys.maxsize-1)
    result=0
    for i in range(len(arr)):
        l_arr[i]=max_l = max(max_l,arr[i])
    for i in range(len(arr)-1,-1,-1):
        r_arr[i] =max_r= max(max_r,arr[i])
    for i in range(len(arr)):
        min_level = min (l_arr[i],r_arr[i])
        result +=min_level - arr[i]
    print(l_arr)
    print(r_arr)
    return result
arr=[3,0,0,2,0,4]
print(rain_water_trapping(arr))
