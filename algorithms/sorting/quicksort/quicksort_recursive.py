# This representation of Quicksort in Python was made based on a video of the Augusto Galego channel.
# To see: https://www.youtube.com/watch?v=nV_WE8SEuGE&t=74s

def quicksort(arr, left, right): 
  if left < right:
    pi = partition(arr,left,right)
    quicksort(arr, left, pi-1)
    quicksort(arr, pi+1, right)


def partition(arr, left, right): 
  pivot = arr[right]

  i = left - 1

  for j in range(left,right): 
    if arr[j] <= pivot: 
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[right] = arr[right], arr[i+1]

  return i+1

nums = list([1,5,7,0,-1,6,5,-4,2])

quicksort(nums, 0, len(nums) - 1)

print(nums)