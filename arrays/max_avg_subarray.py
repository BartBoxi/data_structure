def findMaxAverage(nums: list[int], k: int) -> float:
    curr = 0
    for i in range(k):
        curr += nums[i] / k

    ans = curr

    for i in range(k, len(nums)):
        curr += (nums[i] - nums[i - k]) / k
        ans = max(ans, curr)
    return ans

nums = [1,12,-5,-6,50,3]
k1 = 4



print(findMaxAverage(nums, k1))

