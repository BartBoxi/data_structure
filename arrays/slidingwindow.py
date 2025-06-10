### find the longest subarray where
### a sum of k element is lower or equal to k

### sudo code
# function fn(nums, k):
    left = 0
    right = 0
    answer = 0
    for (int right = 0; right < nums.length: right++):
        curr += nums[right] ## here we add elements from right
        while (curr > k):
            curr -= nums[left]
            left ++

        answer = max(answer, right - left + 1) ##

    return answer


### TODO: Why is sliding window efficient?
