class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        m = {}
        for pair in pairs:
            if pair[0] not in m:
                m[pair[0]] = set()
            if pair[1] not in m:
                m[pair[1]] = set()

            m[pair[0]].add(pair[1]);
            m[pair[1]].add(pair[0]);

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words2[i] in m and words1[i] in m[words2[i]]:
                continue
            if words1[i] in m and words2[i] in m[words1[i]]:
                continue
            return False
        return True
