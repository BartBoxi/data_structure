# given a binary array nums, return the max number of consecutive 1's in the array

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxCount = 0
    currentCount = 0
    for n in nums:
        if n == 1:
            currentCount += 1
            maxCount = max(maxCount, currentCount)
        else:
            currentCount = 0
    return maxCount

list = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(list))