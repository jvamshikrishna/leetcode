class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        #sorting solution
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     res[sorted_word].append(word)

        # return list(res.values())

        # character count soltion:
        for word in strs:
            count = [0] * 26

            for character in word:
                count[ord(character)-ord("a")] +=1

            res[tuple(count)].append(word)

        return res.values()