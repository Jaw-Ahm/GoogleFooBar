def solution(l, t):
    for i, num in enumerate(l):
        sum = num
        j = i
        if sum == t:
            return [i, j]
        while sum < t and j+1 < len(l):
            j += 1
            sum += l[j]
            if sum == t:
                return [i, j]
    return [-1,-1]


def main():
    # Test case 1
    output = solution([1, 2, 3, 4], 15)
    if output == [-1,-1]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution([4, 3, 10, 2, 8], 12)
    if output == [2,3]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 3
    output = solution([4, 3, 5, 7, 8], 12)
    if output == [0,2]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 3
    output = solution([1, 4, 20, 3, 10, 5], 33)
    if output == [2, 4]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 5
    output = solution([1, 4, 0, 0, 3, 10, 5], 1)
    if output == [0,0]:
        print("Pass!", output)
    else:
        print("Fail!", output)




if __name__ == "__main__":
    main()