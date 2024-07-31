class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {word: 1 for word in words}
        longest_chain = 1
        words=sorted(words, key=len)
        
        for word in words:
            for i in range(len(word)):
                # find predeccesor by removing single letters from word
                if word[:i] + word[i+1:] in dp:
                    dp[word] = max(1, dp[word], dp[word[:i] + word[i+1:]] + 1)
                    longest_chain = max(dp[word], longest_chain)

        
        return longest_chain
