import collections
import itertools

class Solution:
    def findSecretWord(self, wordlist, master ):

        def match(w1, w2 ):
            count = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    count += 1
            return  count

        num_match = 0
        while num_match < 6:
            counter = defaultdict(int)
            for w1 in wordlist:
                for w2 in wordlist:
                    if match(w1, w2) == 0:
                        counter[w1] += 1
            guess = min(wordlist, key = lambda x: counter[x])
            # use the word that is similar with most words

            num_match = master.guess(guess)
            wordlist = [w for w in wordlist if match(guess, w) == num_match]




class Solution:

    def match(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                count += 1
        return count

    def findSecretWord(self, wordlist, master):
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]


class Master:
    secret = "acckzz"

    def guess(self, w):
        secret = self.secret
        count = 0
        for i in range(len(secret)):
            if secret[i] == w[i]:
                count += 1
        if count == 6:
            print("you get it ")
        return count


s = Solution()
input = None
m = Master()
res = s.findSecretWord(
    ["acckzz", "ccbazz", "eiowzz", "abcczz","abcedf","fhherg"],
    m)

print("")
