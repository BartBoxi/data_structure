### this is the solution just for one answer

#
# def twoSum(nums:list[int], target:int ) -> list[int]:
#     dic = {}
#     for i in range(len(nums)):
#         num  = nums[i] # przypisujemy wartosci z nums
#         complement = target - num
#         if complement in dic:
#             return [i, dic[complement]]
#         dic[num] = i
#     return [-1, -1]
#
# nums = [5,2,7,10,3,9,11,12,42,21,29]
# nums1 = [5,2,7,10,3,9]
# target = 8
# print(twoSum(nums1, target))




### this is the solution when we want to store all the elements that are correct answers

from typing import List
def allTwoSums(nums:List[int],target:int)-> List[List[int]]:
    dic = {}
    result = []

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in dic:
            result.append([dic[complement], i])
        dic[num] = i
    return result

nums = [5, 2, 7, 10, 3, 9, 11, 12, 42, 21, 29, 1,7,4,4]
target = 8

print(allTwoSums(nums, target))