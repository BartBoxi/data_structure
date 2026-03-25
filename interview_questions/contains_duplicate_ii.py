def containsNearbyDuplicates(nums, k):
    seen = {}
    for i, current_num in enumerate(nums):
        if current_num in seen:
            if i - seen[current_num] <= k:
                return (seen[current_num], i)
        seen[current_num] = i
    return False