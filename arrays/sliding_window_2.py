## Find sum where the k = 8 of elements in array

## [3,1,2,7,4,2,1,1,5]

def find_length(nums: list[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1

        ans = max(ans, right - left +1)  ## remember to add +1 to include all elements

    return ans

nums = [3,1,2,7,4,2,1,1,5]
k = 8

print(find_length(nums, k))