

def minAreaRect(self, points ):
    m = {}
    for p in points:
        if p[0] not in m:
            m[p[0]] = set()
        m[p[0]].add(p[1]);

    min_ = 9999

    for x1,y1 in points:
        for x2,y2 in points:
            if x1 == x2 or y1 == y2:
                continue
            if y2 in m[x1] or y1 in m[x2]:
                min_ = min(min_, abs(x1-x2) * abs(y1-y2))
    return 0 if min_ == 9999 else min_
    pass
