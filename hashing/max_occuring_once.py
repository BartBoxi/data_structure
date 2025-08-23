from typing import List

def largestUniqueNumber(nums:List[int]) -> int:
    uni_numbers = set()
    not_unique = set()
    for num in nums:
        if num not in not_unique:
            if num not in uni_numbers:
                uni_numbers.add(num)
            else:
                uni_numbers.remove(num)
                not_unique.add(num)
    if len(uni_numbers) == 0:
        return -1
    else:
        return max(sorted(list(uni_numbers))) ## with sorting this solution is 0(n log n)
                                ## but once it is removed it will be 0(n)


nums = [9,9,8,8]
print(largestUniqueNumber(nums))