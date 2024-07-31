from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        print(counter)
        done = False
        min_rounds = 0

        while not done:
            for value, count in counter.items():
                if count % 3 == 0 and count > 2:
                    counter[value] -= 3
                    min_rounds += 1
                elif count % 2 == 0 and count == 2:
                    counter[value] -= 2
                    min_rounds += 1
                elif count % 3 == 2:
                    counter[value] -= 3
                    min_rounds += 1
                elif count % 3 == 1 and count > 2:
                    counter[value] -= 2
                    min_rounds += 1
                else:
                    pass
            if all(x in {0} for x in counter.values()):
                return min_rounds      
            if all(x in {0, 1} for x in counter.values()):
                return -1
            
        return min_rounds
        






        