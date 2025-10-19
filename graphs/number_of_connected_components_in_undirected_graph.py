from typing import List
from collections import defaultdict


class Solution():
    def countComponents(self, n:int, edges:List[List[int]]):
        ### solution using union find algorythm

        par = [i for i in range(n)]
        rank = [1] * n
