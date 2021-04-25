from decimal import *

getcontext().prec = 256
sqrt2 = Decimal(2).sqrt() -1


def summation(n):
    if n == 0:
        return 0
    else:
        n_prime = int(n * sqrt2)
        return n * n_prime + (n*(n+1)) / 2 - (n_prime*(n_prime+1)) / 2 - summation(n_prime)


def solution(s):
    total = summation(int(s))
    return str(total)


def main():
    # Test case 1
    output = solution('77')
    if output == "4208":
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution('5')
    if output == "19":
        print("Pass!", output)
    else:
        print("Fail!", output)


if __name__ == "__main__":
    main()