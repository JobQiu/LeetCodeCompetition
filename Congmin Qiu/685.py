def findRedundantDirectedConnection(edges ):

    n = len(edges)
    parent = [-1] *(n+1)
    ds = [0]*(n+1)

    first = -1
    second = -1
    last = -1

    def find(ii):
        if ds[ii] == 0:
            return ii
        else:
            return  

    for i in range(n):
        p = edges[i][0]
        c = edges[i][1]

        if parent[c] != -1:
            first = parent[c]
            second = i
            continue
        parent[c] = i

        p1 = find(p)
        if p1 == c:
            last = i
        else:
            ds[c] = p1




    pass
