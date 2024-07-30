class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #take the work with minimum lenth and loop through the two strs and add it alternativelly
        #the add the remaining chars in the longest string
        l=min(len(word1),len(word2))
        ans=[]
        i=0
        while(i<l):
            ans.append(word1[i])
            ans.append(word2[i])
            i+=1
        if(len(word1)<=len(word2)):
            return "".join(ans)+word2[i:]
        else:
            return "".join(ans)+word1[i:]