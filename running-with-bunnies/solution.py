import numpy as np
from itertools import permutations


def getpaths(times, nextv):
    combs = [[len(times)-1]] + sum([[list(x) + [(len(times)-1)] for x in permutations(range(len(times))[1:-1], y)] for y in range(len(times))[1:-1]], [])
    paths = []
    costs = []
    for comb in combs:
        temp = list(comb)
        path = [0]
        cost = 0
        state = 0
        while temp:
            p, c = shortestpath(state, temp[0], nextv, times)
            state = temp[0]
            temp.pop(0)
            path += p
            cost += c
        paths.append(path)
        costs.append(cost)

    return paths, costs


def shortestpath(u, v, nextv, times):
    cost = 0
    state = u
    if nextv[u][v] == -1:
        return [], None

    path = []
    while (u != v):
        u = nextv[u][v]
        cost += times[state][u]
        state = u
        path.append(u)

    return path, cost


def floyd(dist, nextv, magV):
    for k in range(magV):
        for i in range(magV):
            for j in range(magV):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nextv[i][j] = nextv[i][k]

    return dist, nextv


def solution(times, times_limit):
    if len(times) < 3:
        return []
    magV = len(times)
    inf = 9999
    dist = np.full([magV, magV], fill_value=inf)
    nextv = np.full([magV, magV], fill_value=-1)

    for u in range(magV):
        for v in range(magV):
            dist[u][v] = times[u][v]
            dist[v][v] = 0
            if dist[u][v] != inf:
                nextv[u][v] = v

    dist, nextv = floyd(dist, nextv, magV)
    distsum = np.sum(dist)
    if np.sum(floyd(dist, nextv, magV)[0]) != distsum or distsum == 0:
        return [x-1 for x in range(len(times))[1:-1]]

    paths, costs = getpaths(times, nextv)
    maxlen = 0
    bestpath = []
    bestids = []
    for i, path in enumerate(paths):
        bunnyids = []
        cost = costs[i]
        for i in path:
            if i in range(len(times))[1:-1] and i - 1 not in bunnyids:
                bunnyids.append(i - 1)
        if cost <= times_limit and len(bunnyids) > len(bestids):
            bestpath = path
            bestids = bunnyids
    return sorted(bestids)


def main():
    # Test case 1
    output = solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
    if output == [1, 2]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
    if output == [0, 1]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 3
    output = solution([[0, 2, 2, 2, -1],
             [9, 0, 2, 2, 0],
             [9, 3, 0, 2, 0],
             [9, 3, 2, 0, 0],
             [-1, 3, 2, 2, 0]], -500)
    if output == [0, 1, 2]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 4
    output = solution([[1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1]], 1)
    if output == []:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 5
    output = solution([[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]], 2)
    if output == [0]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 6
    output = solution([[0, 5, 11, 11, 1],
             [10, 0, 1, 5, 1],
             [10, 1, 0, 4, 0],
             [10, 1, 5, 0, 1],
             [10, 10, 10, 10, 0]], 10)
    if output == [0, 1]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 7
    output = solution([[0, 10, 10, 10, 1],
             [0, 0, 10, 10, 10],
             [0, 10, 0, 10, 10],
             [0, 10, 10, 0, 10],
             [1, 1, 1, 1, 0]], 5)
    if output == [0, 1]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 8
    output = solution([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]], 1)
    if output == [0, 1, 2]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 9
    output = solution([[2, 2],
             [2, 2]], 1)
    if output == []:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 10
    output = solution([[0, 10, 10, 1, 10],
              [10, 0, 10, 10, 1],
              [10, 1, 0, 10, 10],
              [10, 10, 1, 0, 10],
              [1, 10, 10, 10, 0]], 6)
    if output == [0,1,2]:
        print("Pass!", output)
    else:
        print("Fail!", output)


if __name__ == "__main__":
    main()