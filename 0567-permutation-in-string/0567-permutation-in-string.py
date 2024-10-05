class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        
        if s1_count == s2_count:
            return True
        
        for i in range(len(s1), len(s2)):
            left_char = s2[i - len(s1)]
            s2_count[left_char] -= 1
            if s2_count[left_char] == 0:
                del s2_count[left_char]

            new_char = s2[i]
            s2_count[new_char] += 1
            
            if s1_count == s2_count:
                return True
        return False