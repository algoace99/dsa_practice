class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        '''
        count = 0
        for l in range(len(s)-2):
            if len(set(s[l:l+3])) == 3:
                count += 1
        return count
        '''
        l = 0
        st = set()
        ans = 0
        for r in range(len(s)):
            st.add(s[r])
            while r-l+1 > 3:
                if s[l] != s[r] and s[l] != s[r-1] and s[l] != s[r-2]:
                    st.remove(s[l])
                l += 1
            if len(st) == 3: 
                ans += 1
        return ans