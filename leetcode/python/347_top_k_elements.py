def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = {}
    for i in nums:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    sorted_keys = sorted(res.keys(), key = lambda x:res[x], reverse=True)
    return sorted_keys[:k]


nums = [1,1,1,2,2,2,2,3,3,3,3,5,5,5,5,5,5]
print(topKFrequent(nums, k =2)) 