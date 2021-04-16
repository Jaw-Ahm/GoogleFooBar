def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        count += 1
        lsb = n % 4
        if n % 2 == 0:
            n /= 2
        elif n == 3:
            n -= 1
        elif lsb == 3:
            n += 1
        elif lsb == 1:
            n -= 1
    return count

def main():
    # Test case 1
    output = solution("15")
    if output == 5:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution("4")
    if output == 2:
        print("Pass!", output)
    else:
        print("Fail!", output)


if __name__ == "__main__":
    main()