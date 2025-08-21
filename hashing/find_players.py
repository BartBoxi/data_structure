from typing import List
from collections import defaultdict

def findWinners(matches : List[List[int]]) -> List[List[int]]:
    zero_loss = set()
    one_loss = set()
    more_losses = set()

    for match in matches:
        winner = match[0]
        loser = match[1]
        if winner not in one_loss and winner not in more_losses: ### important was and here
            zero_loss.add(winner)
        if loser in zero_loss:
            zero_loss.remove(loser)
            one_loss.add(loser)
        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)
        elif loser in more_losses:
            more_losses = more_losses
        else:
            one_loss.add(loser)
    return [sorted(list(zero_loss)), sorted(list(one_loss))]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))





















