def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]

print(answer_queries(nums, queries, limit=13))