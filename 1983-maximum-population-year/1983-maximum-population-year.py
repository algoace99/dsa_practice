class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birth, death = [], []
        for i in logs:
            birth.append(i[0])
            death.append(i[1])
        birth.sort()
        death.sort()

        max_pop = 0
        current_pop = 0
        i,j = 0,0
        year = birth[0]
        while i < len(logs):
            if birth[i] < death[j]:
                current_pop += 1
                if current_pop > max_pop:
                    max_pop = current_pop
                    year = birth[i]
                i += 1
            else:
                current_pop -= 1
                j += 1

        return year