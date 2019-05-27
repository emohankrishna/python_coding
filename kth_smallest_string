def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
# partition()
def kth_smallest(arr,begin,end,k):
    if k-1 >= begin and k-1 <= end:
        part_index = partition(arr,begin,end)
        if k-1 == part_index:
            return arr[part_index]
        if k-1 < part_index:
            return kth_smallest(arr,begin,part_index-1,k)
        else:
            return kth_smallest(arr,part_index+1,end,k)


arr=[772, 468, 507, 463, 877, 690, 721, 656, 126, 739, 647, 161, 445, 159, 162, 244, 125, 84, 560, 398, 329, 525, 257, 158, 545, 580, 990, 843, 348, 456, 69, 376, 897, 518, 197, 51, 968]
k=4
print(sorted(arr))
print(kth_smallest(arr,0,len(arr)-1,k))
