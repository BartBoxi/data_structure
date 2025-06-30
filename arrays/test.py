nums = [1,2,3,4,5,6]

prefix = [nums[0]]

for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])
print(prefix)


print(len(nums ))