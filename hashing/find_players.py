from collections import defaultdict
from typing import List


def findWinners(matches : List[List[int]]) -> List[List[int]]:
    loosers = {}
    for list in matches:
        for number in list:
            if number[1] not in loosers:
                loosers.add(number)
        return loosers






from typing import List


def findWinners(matches : List[List[int]]) -> List[List[int]]:
    loosers = {}
    winners = {}
    for match in matches:
        loser = match[1]
        winner = match[0]
        loosers.append(loser)
        winners.add(winner)

    answer = winners - loosers
    return answer

matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]

print(findWinners(matches))


