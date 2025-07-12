# Last updated: 12/07/2025, 22:09:33
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(0, len(details)):
            lis = details[i]
            if int(lis[11]) > 6 and int(lis[12]) == 0:
                count += 1
            elif int(lis[11]) >= 6 and int(lis[12]) != 0:
                count += 1
        return count
        