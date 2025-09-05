from collections import defaultdict
from email.policy import default
from typing import List



def maximumSum(nums:List[int]) -> int:
    def get_digit_sum(num):
        digit_sum = 0
        while num: ## e.g. for 48
            digit_sum += num % 10 ## this will give us 8
            num //= 10
        return digit_sum

    dic = defaultdict(list)
    for num in nums:
        digit_sum = get_digit_sum(num)
        #print(digit_sum)
        dic[digit_sum].append(num)

    ans = -1
    for key in dic:
        curr = dic[key]
        print(curr)
        if len(curr) > 1:
            curr.sort(reverse=True) # we need to sort it because if we got digits that the sum is same
                    ### for all of them then we wont get the max value
            ### but sorting is not very optimal here anyway
            #print(curr)
            ans = max(ans, curr[0] + curr[1])
    return ans





nums = [19, 28, 37, 82, 91]



print(maximumSum(nums))

