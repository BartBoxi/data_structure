def missingNumber(nums) -> int:
    ##new_set = set()
    new_lst = []
    for i in range(0,len(nums)):
        new_lst.append(i)
    return new_lst


nums = [0,2,1]

print(missingNumber(nums))