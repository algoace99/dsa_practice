class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split(" ")
        for i in range(len(l)):
            if l[i][:len(searchWord)] == searchWord:
                return i+1
        return -1