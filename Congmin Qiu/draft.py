def reverse(self, s ):

    i = 0
    j = 0

    while j < len(s):
        while s[i] == " ":
            i += 1
        j = i
        while s[j] != " ":
            j += 1
        i = j
