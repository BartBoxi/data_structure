def waysToSplitArray(nums: list[int])-> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    ## here in return we will get all prefixes
    ## e.g [1, 3, 6, 10, 15, 21]
    ## if nums = [1,2,3,4,5,6]

    ans = 0
    for i in range(len(nums) -1):
        left_section = prefix[i]
        right_section = (prefix[-1] - prefix[i])
        if left_section >= right_section:
            ans += 1
    return ans











nums = [10,4,-8,7]
print(waysToSplitArray(nums))
