class Solution:

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        length = self.ladderLength(beginWord, endWord, wordList)
        path_dict = {}

        
        pass

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        beginSet = set()
        beginSet.add(beginWord)

        visited = {}
        for word in wordList:
            visited[word] = False

        if endWord not in visited:
            return 0

        import string

        level = 0
        while len(beginSet) != 0:

            level += 1
            newBeginSet = set()
            for word in beginSet:
                for ind in range(len(word)):

                    originalChar = word[ind]
                    for repl in string.ascii_lowercase:
                        if repl == originalChar:
                            continue
                        else:
                            newWord = word[:ind] + repl + word[ind + 1:]
                        if newWord in visited and not visited[newWord]:
                            if newWord == endWord:
                                return level + 1
                            newBeginSet.add(newWord)
                            visited[newWord] = True
            print(newBeginSet)

            beginSet = newBeginSet
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

# beginWord = "a"
# endWord = "c"
# wordList = ["a", "b", "c"]

s = Solution()
res = s.ladderLength(beginWord, endWord, wordList)
assert res == 5  # [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]

# %%
# step 1. calculate the short length

beginSet = set()
beginSet.add(beginWord)

visited = {}
for word in wordList:
    visited[word] = False

import string

level = 0
while len(beginSet) != 0:

    newBeginSet = set()
    for word in beginSet:
        for ind in range(len(word)):

            originalChar = word[ind]
            for repl in string.ascii_lowercase:
                if repl == originalChar:
                    continue
                else:
                    newWord = word[:ind] + repl + word[ind + 1:]
                if newWord in visited and not visited[newWord]:
                    newBeginSet.add(newWord)
                    visited[newWord] = True
    print(newBeginSet)

    beginSet = newBeginSet
    level += 1

print(level)

print("")
