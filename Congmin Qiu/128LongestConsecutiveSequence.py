def longestConsecutive(nums):
    index2length = {}
    for n in nums:
        if n in index2length:
            continue

        if n + 1 in index2length and n + index2length[n + 1] in index2length:
            drop_mid = index2length[n + 1] != 1
            index2length[n] = 1 + index2length[n + 1]
            index2length[n + index2length[n + 1]] = 1 + index2length[n + 1]
            if drop_mid:
                index2length.pop(n + 1)

        if n - 1 in index2length and n - index2length[n - 1] in index2length:
            if n in index2length and n + index2length[n] in index2length:
                newLength = index2length[n - 1] + index2length[n]
                index2length[n - 1 - index2length[n - 1]] = newLength
                index2length[n + index2length[n]] = newLength
                index2length.pop(n)
            else:
                index2length[n] = 1 + index2length[n - 1]
                index2length[n - 1 + index2length[n - 1]] = 1 + index2length[n - 1]
                index2length.pop(n - 1)

            pass

        if n not in index2length:
            index2length[n] = 1

    print("123")


nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)
