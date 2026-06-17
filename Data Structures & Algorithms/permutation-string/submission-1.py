class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_1 = Counter(s1)
        count_2 = Counter(s2[:len(s1)])

        if count_1 == count_2:
            return True
        
        for i in range(len(s1), len(s2)):
            count_2[s2[i-len(s1)]] -= 1
            count_2[s2[i]] += 1

            if count_2[s2[i-len(s1)]] == 0:
                del count_2[s2[i-len(s1)]]

            if count_2 == count_1:
                return True
            
        return False