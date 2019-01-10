class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        ban = set(banned)

        import re
        words = re.findall('r\W', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
