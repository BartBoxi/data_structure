# Example 4: Given an integer array nums and an integer k,
# find the sum of the subarray with the largest sum whose
# length is k.



def find_best_subarray(nums: list[int], k: int):
    # step 1:  build the first window of size k
    curr = 0
    for i in range(k):
        curr += nums[i] # here we are adding all elements in the range of k

    ans = curr # this is our starting best sum

    # here we are sliding the window
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    return ans

