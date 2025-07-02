def minStartValue(nums) -> int:
    startValue = 1
    while True:
        total = startValue
        isValid = True

        for num in nums:
            total += num
            if total < 1:
                isValid = False
                break
        if isValid:
            return startValue
        else:
            startValue += 1
    return startValue

#########
# Solution 2

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0

        for num in nums:
            total += num
            min_val = min(min_val, total)
        return -min_val + 1


nums = [-3,2,-3,4,2]
print(minStartValue(nums))