# Last updated: 4/24/2025, 6:50:26 PM
# think of sliding window or two pointer, where you start with right and always check if it is in char set, if its not just add it to char set. if it is present remove the left and increment left position, but keep in mind to always have max length as max function so that distinct charcater max length remain undisturbed
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        left = 0
        max_length =0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length