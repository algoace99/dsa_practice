class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit_sum=""
        for i in s:
            digit_sum+=str((ord(i)-96))

        for _ in range(k):
            if len(str(digit_sum))==1:
                break
            digit_sum=sum(list(map(int,list(str(digit_sum)))))
            
        return int(digit_sum)
