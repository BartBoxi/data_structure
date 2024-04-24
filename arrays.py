# # #adding element at a specific position in array
# #
# # def insertElement(arr, n, x, pos):
# #     for i in range(n-1, pos-1, -1):
# #         arr[i + 1] = arr[i]
# #
# #     arr[pos] = x
# #     print(arr)
# #
# # arr = [1,2,3]
# # n = len(arr)
# # x = 5
# # pos = 1
# #
# # insertElement(arr,n,x,pos)
#
# arr = [1,2,3]
# arr.insert(2,10)
# print(arr)

# searching in sorted array using binary search

# def binarySearch(arr, low, high, key):
#     mid = (low + high)/2
#
#     if(key == arr[int(mid)]):
#         return mid
#     if(key > arr[int(mid)]):
#         return binarySearch(arr,(mid + 1), high, key)
#     if(key < arr[int(mid)]):
#         return binarySearch(arr, low, (mid - 1), key)
#     else:
#         return 0
#
# arr = [5, 6, 7, 8, 9, 10, 43, 10, 10, 22]
# n = len(arr)
# key = 10
#
# print("Index:", int(binarySearch(arr, 0, (n-1),key)))

###adjust previous binary search to find the first occurance of the key

def binarySearch(arr, low, high, key):
    mid = (low + high)/2

    if(key == arr[int(mid)]):
        if
    if(key > arr[int(mid)]):
        return binarySearch(arr,(mid + 1), high, key)
    if(key < arr[int(mid)]):
        return binarySearch(arr, low, (mid - 1), key)
    else:
        return 0
