def candy(self, ratings):
    if len(ratings) == 0:
        return 0
    result = 1
    up = down = peak = 0
    for i in range(1, len(ratings)):
        if ratings[i - 1] < ratings[i]:
            up += 1
            peak = up
            down = 0
            result += 1 + up
        elif ratings[i - 1] == ratings[i]:
            up = peak = down = 0
            result += 1
        else:
            down += 1
            up = 0
            print(peak >= down)
            result += 1 + down + [0, -1][peak >= down]
        print("{}-{}-{}-{} - {}".format(ratings[i], up, peak, down, result))
    return result


res = candy(None, [0, 1, 20, 9, 8, 7, 0, 1, 20, 9, 8, 7])
