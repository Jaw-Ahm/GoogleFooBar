import math


def makemirrors(grid, pos, dimensions):
    m_cords = [[], []]
    for i, cord in enumerate(grid):
        for j, n in enumerate(cord):
            if n % 2 == 0:
                m_cords[i].append(cord[j] * dimensions[i] + pos[i])
            else:
                m_cords[i].append(cord[j] * dimensions[i] + (dimensions[i] - pos[i]))

    return m_cords

def getdistance(ax, ay, bx, by):
    return math.sqrt((ax-bx)**2 + (ay-by)**2)


def solution(dimensions, your_position, trainer_position, distance):
    x_dim, y_dim = dimensions[0], dimensions[1]

    maxgrid = [max((distance + your_position[0]) / x_dim, abs((distance - your_position[0]) / x_dim)),
                   max((distance + your_position[1]) / y_dim, abs((distance - your_position[1]) / y_dim))]

    grid = [list(range(0, maxgrid[0]+1)), list(range(0, maxgrid[1]+1))]

    mirrormes = makemirrors(grid, your_position, dimensions)
    mirrortrainers = makemirrors(grid, trainer_position, dimensions)

    x, y = float(your_position[0]), float(your_position[1])

    arctans_all = {}
    arctans_mt = {}
    quadrants = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

    for q in range(len(quadrants)):
        for u in range(len(mirrormes[0])):
            for v in range(len(mirrormes[1])):
                x1, y1 = float(mirrormes[0][u]) * quadrants[q][0], float(mirrormes[1][v]) * quadrants[q][1]
                dist_yp_mm = getdistance(x, y, x1, y1)
                arc_mm = math.atan2(y1 - y, x1 - x)
                if dist_yp_mm <= distance and [x1, y1] != your_position:
                    if (arc_mm not in arctans_all) or (arc_mm in arctans_all and arctans_all[arc_mm] > dist_yp_mm):
                        arctans_all[arc_mm] = dist_yp_mm
        for i in range(len(mirrortrainers[0])):
            for j in range(len(mirrortrainers[1])):
                x2, y2 = float(mirrortrainers[0][i]) * quadrants[q][0], float(mirrortrainers[1][j]) * quadrants[q][1]
                dist_yp_mt = getdistance(x, y, x2, y2)
                arc_mt = math.atan2(y2-y, x2-x)
                if dist_yp_mt <= distance:
                    if (arc_mt not in arctans_all) or (arc_mt in arctans_all and arctans_all[arc_mt] > dist_yp_mt):
                        arctans_all[arc_mt] = dist_yp_mt
                        arctans_mt[arc_mt] = dist_yp_mt

    return len(arctans_mt)


def main():
    # Test case 1
    output = solution([3,2], [1,1], [2,1], 4)
    if output == 7:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution([300,275], [150,150], [185,100], 500)
    if output == 9:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 3
    output = solution([10,10], [4,4], [3,3], 5000)
    if output == 739323:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 4
    output = solution([23,10], [6, 4], [3,2], 23)
    if output == 8:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 5
    output = solution([2,5], [1,2], [1,4], 11)
    if output == 27:
        print("Pass!", output)
    else:
        print("Fail!", output)


if __name__ == "__main__":
    main()