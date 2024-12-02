class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        '''
        l = sentence.split(" ")
        for i in range(len(l)):
            if l[i][:len(searchWord)] == searchWord:
                return i+1
        return -1
        '''
        sentence_len = len(sentence)
        searchWord_len = len(searchWord)

        current_word = 1
        
        if sentence[:searchWord_len] == searchWord:
            return 1

        index = 0
        while index < sentence_len:
            if sentence[index] == " ":
                current_word += 1
                if sentence[index+1:index+searchWord_len+1] == searchWord:
                    return current_word
            index += 1
        return -1