class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit_sum=""
        for i in s:
            digit_sum+=str((ord(i)-96))
        final_sum=0
        for _ in range(k):
            final_sum=sum(list(map(int,list(str(digit_sum)))))
            digit_sum=final_sum
            
        return int(digit_sum)
