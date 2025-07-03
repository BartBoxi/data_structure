def getAverages(nums, k) -> List[int]:
    n = len(nums)
    window_size = 2 * k + 1
    avgs = [-1] * n

    if window_size > n:
        return avgs

    window_sum = sum(nums[:window_size])
    avgs[k] = window_sum // window_size

    for i in range(k + 1, n - k):
        window_sum = window_sum - nums[i - k - 1] + nums[i + k]
        avgs[i] = window_sum // window_size
    return avgs




