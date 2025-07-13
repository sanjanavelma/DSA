# Last updated: 13/07/2025, 23:41:32
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        c = 0
        players.sort()
        trainers.sort()
        for i in trainers:
            if i>=players[c]:
                c+=1
                if c==len(players):
                    break
        return c