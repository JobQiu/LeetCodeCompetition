
def matchPeopleBike(people, bikes, grid ):
    """
    assume, 1. len(bikes) > len(people)
    return

    """

    def distance(p, b, grid = None, withoutObstacle = True):
        if withoutObstacle:
            return abs(p[0] - b[0]) +  abs(p[1] - b[1])
        else:
            visited = set()
            # use bfs to search the shortest distance
            return 0


    distances = []
    for i in range(len(people))
        p = people[i]
        for j in range(len(bikes)):
            b = bikes[j]
            distances.append((distance(p, b, grid, False), i, j))
    distances.sort(key = lambda x: x[0]) # O(NlogN) where N is len of people * len of bikes
    matchedPeople = set()
    matchedBikes = set()

    res = []
    i = 0
    while len(res) < len(people):
        distance, pIndex, bIndex = distances[i]
        if pIndex in matchedPeople or bIndex in matchedBikes:
            pass
        else:
            res.append([i, j])
            matchedPeople.add(i);
            matchedBikes.add(j);
        i+=1
    return res
