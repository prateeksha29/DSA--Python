"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted. """


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ## Create a dictionary of order of alien dictionary
        order_dict = dict((alph, pos) for pos, alph in enumerate(order))

        if len(words) <= 1:
            return True
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                l_word1 = len(words[i])
                l_word2 = len(words[j])
                for (pos1, pos2) in zip(range(l_word1), range(l_word2)):
                    if order_dict[words[i][pos1]] < order_dict[words[j][pos2]]:
                        break
                    elif order_dict[words[i][pos1]] > order_dict[words[j][pos2]]:
                        return False
                    elif order_dict[words[i][pos1]] == order_dict[words[j][pos2]]:
                        if (pos1 < l_word1 - 1) & (pos2 == l_word2 - 1):
                            return False
        return True



