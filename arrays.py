# # # #adding element at a specific position in array
# # #
# # # def insertElement(arr, n, x, pos):
# # #     for i in range(n-1, pos-1, -1):
# # #         arr[i + 1] = arr[i]
# # #
# # #     arr[pos] = x
# # #     print(arr)
# # #
# # # arr = [1,2,3]
# # # n = len(arr)
# # # x = 5
# # # pos = 1
# # #
# # # insertElement(arr,n,x,pos)
# #
# # arr = [1,2,3]
# # arr.insert(2,10)
# # print(arr)
#
# # searching in sorted array using binary search
#
# # def binarySearch(arr, low, high, key):
# #     mid = (low + high)/2
# #
# #     if(key == arr[int(mid)]):
# #         return mid
# #     if(key > arr[int(mid)]):
# #         return binarySearch(arr,(mid + 1), high, key)
# #     if(key < arr[int(mid)]):
# #         return binarySearch(arr, low, (mid - 1), key)
# #     else:
# #         return 0
# #
# # arr = [5, 6, 7, 8, 9, 10, 43, 10, 10, 22]
# # n = len(arr)
# # key = 10
# #
# # print("Index:", int(binarySearch(arr, 0, (n-1),key)))
#
# ###adjust previous binary search to find the first occurance of the key
#
# # def binarySearch(arr, low, high, key):
# #     mid = (low + high)/2
# #     first_occurance = []
# #
# #     if(key == arr[int(mid)]):
# #         first_occurance =  mid
# #         binarySearch(arr,low,(mid - 1), key)
# #     if(key > arr[int(mid)]):
# #         return binarySearch(arr,(mid + 1), high, key)
# #     if(key < arr[int(mid)]):
# #         return binarySearch(arr, low, (mid - 1), key)
# #     else:
# #         return 0
# #
# # arr = [5, 6, 7, 8, 9, 10, 43, 10, 10, 22]
# # n = len(arr)
# # key = 10
# #
# # binarySearch(arr, 0, (n-1), key)
#
# # searching in a sorted array using fibonacci search
# ###First we look for Fm > n where n is lenght of n
# # then we are doing:
# # 1. compare x with element on Fm-1 --> if Fm-1== x --> return Fm-1
# # 2. jesli jednak szukana wartosc jest mniejsza to odrzuc elementy na pozycjach Fm-1
# # do n, ustaw m = m -1 i wroc do punktu 1
# # 3. jesli jednak szukana wartosc jest wieksza to odrzuc elementy na pozychi 1 do Fm-1.
# # pozostalem elementy ponumeruj, ustaw m = m-2 i wroc do punktu 1
# # jesli po zakonczeniu petli na wskazanej pozycji nie ma szukanego elementu to oznacza, ze nie istnieje
# # ###
#
# def fibonacci_search(lst, target):
#     size = len(lst)
#
#     start = -1
#
#     f0 = 0
#     f1 = 1
#     f2 = 1
#     while(f2 < size):
#         f0 = f1
#         f1 = f2
#         f2 = f1 + f0
#
#     while(f2 > 1):
#         index = min(start + f0, size -1)
#         if lst[index] < target:
#             f2 = f1
#             f1 = f0
#             f0 = f2 - f1
#             start = index
#         elif lst[index] > target:
#             f2 = f0
#             f1 = f1 -f0
#             f0 = f2 - f1
#         else:
#             return index
#     if (f1) and (lst[size - 1] == target):
#         return size -1
#     return None
#
# lst = [1,5,8,13,15,16,20,26]
# target = 13
# print(fibonacci_search(lst, target))
# #
# # ###Sure, let's break down the code step by step:
# #
# # Initialization:
# # size = len(lst): This variable stores the length of the list lst.
# # start = -1: This variable initializes the starting index for the search. It's set to -1 initially because in the beginning, the search range is undefined.
# # Fibonacci Numbers Generation:
# # Three variables f0, f1, and f2 are used to generate Fibonacci numbers. The loop generates Fibonacci numbers until f2 exceeds or equals the size of the list lst. This loop is essentially finding the smallest Fibonacci number that is greater than or equal to the size of the list.
# # Fibonacci Search Algorithm:
# # Once the Fibonacci numbers are generated, the algorithm enters the search phase.
# # In the search phase, it starts with f2 being the smallest Fibonacci number greater than or equal to the size of the list.
# # It enters a loop where it iterates until the Fibonacci number f2 becomes 1 (indicating that the search range has become a single element).
# # Within this loop, it calculates the index to be checked based on the Fibonacci numbers.
# # If the element at the calculated index is less than the target, it updates the Fibonacci numbers and the start index to continue searching in the upper part of the list.
# # If the element at the calculated index is greater than the target, it updates the Fibonacci numbers and the start index to continue searching in the lower part of the list.
# # If the element at the calculated index is equal to the target, it returns the index where the target is found.
# # Handling Edge Case:
# # After the loop, there's an edge case check.
# # If f1 is not 0 (which means the search range is not empty), and the last element of the list equals the target, it returns the index of the last element. This is because the algorithm might have terminated the search before reaching the last element, so this check ensures that the last element is not missed if it's equal to the target.
# # The purpose of setting start = -1 initially is to indicate that the search hasn't started yet. And the if condition you asked about ensures that if the last element of the list equals the target and it hasn't been found during the search, it returns the index of the last element.###
#

#Deleting at an ith index
#Remove value at index i before shifting elements to the left
# Assuming i is a valid index
# def removeMiddle(arr, i, lenght):
#     #shift starting from i + 1 to end
#     for index in range(i + 1, lenght):
#         arr[index -1] = arr[index]
#         print(arr)
#
# arr = [1,2,3,4,5]
# removeMiddle(arr, 2, len(arr))

# def insertEnd(arr, n, length, capacity):
#     if length < capacity:
#         arr[length] = n

### length is the number of elements inside the array whereas capacity refers to
### the maximum number of elements the array can hold

### 26 Remove Duplicates from Sorted Array
#Solution
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = 1
#         for r in range(1, len(nums)):
#             if nums[r] != nums[r - 1]:
#                 nums[l] = nums[r]
#                 l += 1
#         return l
#

arr = [1,1,1,2,3,0,4,2]
val = 1

def count_occ(arr, val):
    l = 0
    for i in range(len(arr)):
        if arr[i] == val:
            l += 1
    print(l)


count_occ(arr, val)
