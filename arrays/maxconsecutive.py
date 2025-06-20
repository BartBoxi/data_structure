def max_consecutive(nums: list[int], k = int):
    L = 0
    max_len = 0
    zeros_count = 0
    for R in range(len(nums)):
        if nums[R] == 0:
            zeros_count += 1
        while zeros_count > k:
            if nums[L] == 0:
                zeros_count -= 1
            L += 1

        max_len = max(max_len, R - L + 1)
    return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0]

k = 2


print(max_consecutive(nums, k))


