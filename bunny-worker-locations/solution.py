def solution(x, y):
    max = x + y - 1
    dif = max - x
    ans = ((max) * (max + 1)) / 2 - dif
    return str(ans)


def main():
    # Test case 1
    output = solution(5, 10)
    if output == "96":
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution(3, 2)
    if output == "9":
        print("Pass!", output)
    else:
        print("Fail!", output)

    # # Test case 3
    # output = solution([4, 3, 5, 7, 8], 12)
    # if output == [0,2]:
    #     print("Pass!", output)
    # else:
    #     print("Fail!", output)
    #
    # # Test case 3
    # output = solution([1, 4, 20, 3, 10, 5], 33)
    # if output == [2, 4]:
    #     print("Pass!", output)
    # else:
    #     print("Fail!", output)
    #
    # # Test case 5
    # output = solution([1, 4, 0, 0, 3, 10, 5], 1)
    # if output == [0,0]:
    #     print("Pass!", output)
    # else:
    #     print("Fail!", output)


if __name__ == "__main__":
    main()