from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counter = Counter(word)
        keys_count = 8
        presses = 1
        keys_assigned = 0

        #print(letter_counter.most_common())
        fast_keypad = {}
        # 8 KEYS CAN HAVE MOST COMMON LETTERS AS FIRST LETTER
        for i, (letter, count) in enumerate(letter_counter.most_common()):
            # most_common = letter_counter.most_common(1)
            # for most_common_letter in most_common:
        
            if len(fast_keypad) < 8:
                presses = 1
            elif len(fast_keypad) >= 8 and len(fast_keypad) < 16:
                presses = 2
            elif len(fast_keypad) >= 16 and len(fast_keypad) < 24:
                presses = 3
            else:
                presses = 4
        
            fast_keypad[letter] = presses
                #del letter_counter[most_common_letter]
        print(fast_keypad)
        min_presses = 0
        # calc min presses
        for letter in word:
            min_presses += fast_keypad[letter]
        
        return min_presses

        