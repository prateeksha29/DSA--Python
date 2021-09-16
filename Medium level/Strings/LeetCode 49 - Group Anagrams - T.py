"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = ["a"]
Output: [["a"]]
"""

# using sorted strings
# sorted each string and using the order as the key for anagrams
# Time complexity: O(NKlogK) where k is the length of the longest string
# Space complexity: O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            ss = str(sorted(list(s)))
            hashmap[ss].append(s)
        return hashmap.values()

# Using count of characters
# using alphabet list of 26 letters and using this to form the dict keys
#Potential edge case of aab and abb is 111 both so use use a dilimiter in between, hence, take tuple
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # count_s = '#'.join(str(x) for x in count)
            ans[tuple(count)].append(s)
        return ans.values()