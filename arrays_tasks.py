# #task 1.Given an array, write functions to find the minimum
# # and maximum elements in it.
#
# import sys
# a = [4,3,45,2,23,11,26]
#
# # a_sorted = sorted(a)
# # print(a)
# # print(a_sorted[0])
# # print(min(a))
# # print(max(a))
# # min_value = a_sorted[0]
# # max_value = a_sorted[-1]
# # print(min_value, max_value)
#
# def getMin(arr, n):
#     res = arr[0]
#     print(res)
#     for i in range(1,n):
#         res = min(res, arr[i])
#     return res
#     print(res)
#
# print(getMin(a, len(a)))
#
# def getMax(arr,n):
#     res = arr[0]
#     print(res)
#     for i in range(1, n):
#         res = max(res, arr[i])
#     return res
#     print(res)
#
# print(getMax(a, len(a)))

### Deleting from an array

# removing from the last position in the array if the array
# is not empty (i.e. length is non-zero)

def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0
        arr.pop() #pop is physically removing the latest element from the list
arr = [1,2,3]
length = len(arr)
removeEnd(arr,length)
print(arr)

## deleting at an ith index

#remove value at i index before shifting elements to the left
#assuming that i is a valid index!
# def removeMiddle(arr, i, length):
#     #shift starting from i + 1 to end
