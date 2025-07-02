### solution 1
# def RunningSum(nums):
#     sum = 0
#     ans = []
#     for i in nums:
#         sum += i
#         ans.append(sum)
#     print(ans)

def runningSum(nums):
    running_sum_array = [nums[0]]
    for i in range(1, (len(nums))):
        curr = running_sum_array[i-1] + nums[i]
        running_sum_array.append(curr)
    return running_sum_array



nums = [1,1,1,1]

print(runningSum(nums))