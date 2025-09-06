from collections import defaultdict
from typing import List


def maximumSum(nums: List[int])-> int:
    def get_digit_sum(num):
        digit_sum = 0
        while num:
            digit_sum += num % 10 ## this one will give us right digit like 8 from 48
            num // 10
        return digit_sum

    dic = defaultdict(int)
    ans = -1
