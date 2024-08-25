class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0 and n<=1:
            return True
        if len(flowerbed)==1 and flowerbed[0]==1 and n>0:
            return False 
        count=0
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0: 
                count+=1
                flowerbed[i]=1
            elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0: 
                count+=1
                flowerbed[i]=1
            else:
                if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    count+=1
                    flowerbed[i]=1
        if count>=n:
            return True
        else:
            return False