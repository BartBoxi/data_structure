def missingNumber(nums) -> int:
    n = len(nums)
    full_set = set(range(n +1))
    nums_set = set(nums)
    missing = full_set - nums_set
    return missing.pop()


nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums))