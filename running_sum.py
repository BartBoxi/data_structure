def RunningSum(nums):
    sum = 0
    ans = []
    for i in nums:
        sum += i
        ans.append(sum)
    print(ans)




nums = [1,1,1,1]

print(RunningSum(nums))