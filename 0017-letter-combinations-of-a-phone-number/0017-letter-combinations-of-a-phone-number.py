class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone_keypad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if digits == "":
            return []

        if len(digits) == 1:
            return list(phone_keypad[digits])

        rows = len(phone_keypad[digits[0]])
        cols = len(phone_keypad[digits[1]])
        
        
        # Backtracking trick-- for extendng from 2 -> 3 digits, just take all the answers
        # from P(2) and add each unique character from the last digit to the previous solution

        dp = [[0 for j in range(cols)] for i in range(rows)]
        print(dp)
        results = []

        for i in range(rows):
            for j in range(cols):
                try:
                    dp[i][j] = phone_keypad[digits[0]][i] + phone_keypad[digits[1]][j]
                    results.append(dp[i][j])
                except IndexError as e:
                    print(e)

        for digit in digits[2:]:
            new_results = []
            for char in phone_keypad[digit]:
                for i in range(len(results)):
                    new_results.append(results[i] + char)
            results = new_results
                
        return results
        #print(dp)

        