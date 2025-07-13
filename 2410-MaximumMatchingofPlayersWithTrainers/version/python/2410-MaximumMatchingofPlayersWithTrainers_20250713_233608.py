# Last updated: 13/07/2025, 23:36:08
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = j = count = 0
        while(i < len(players) and j < len(trainers)):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
            j += 1
        return count