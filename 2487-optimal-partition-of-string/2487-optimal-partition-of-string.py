from collections import Counter

class Solution:
    def partitionString(self, s: str) -> int:

        partition_count = 1
        partition = set()
        for letter in s:
            if letter in partition:
                partition_count += 1
                partition = set()
            partition.add(letter)
        # handle last letter manually :(
        #if s[-1:]
        return partition_count
            
        