def solution(x, y):
    m = int(x)
    f = int(y)
    counter = 0
    if (m % f == 0 or f % m == 0) and (f > 1 and m > 1):
        return "impossible"
    if m / f > 2:
        counter = m / f
        m -= (f * counter)
    elif f / m > 2:
        counter = f / m
        f -= (m * counter)

    while m > 1 or f > 1:
        if (m % f == 0 or f % m == 0) and (f > 1 and m > 1):
            return "impossible"
        if m > f:
            m -= f
        elif f > m:
            f -= m
        counter += 1

    return str(counter)


def main():
    # Test case 1
    output = solution("2", "1")
    if output == "1":
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution("4", "7")
    if output == "4":
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 3
    output = solution("10", "5")
    if output == "impossible":
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 4
    output = solution("1", "1")
    if output == "0":
        print("Pass!", output)
    else:
        print("Fail!", output)


if __name__ == "__main__":
    main()