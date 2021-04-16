from fractions import Fraction
import numpy as np


def getfractions(m):
    fracs = []
    ans = []
    for i in m:
        fracs.append(Fraction(i).limit_denominator())

    lcd = np.lcm.reduce([x.denominator for x in fracs])

    for i in fracs:
        ans.append((i.numerator * (lcd / i.denominator)))

    ans.append(lcd)
    return ans


def orderarray(m):
    arr = np.array(m, dtype=float)
    z_order = []
    nz_order = []
    for i in range(len(arr)):
        rowsum = np.sum(arr[i])
        if rowsum == 0:
            z_order.append(i)
        else:
            nz_order.append(i)
            arr[i] = np.true_divide(arr[i], rowsum)
    new_order = z_order + nz_order
    return arr[:, new_order][new_order, :], len(z_order)


def solution(m):
    # make numpy arrays
    if len(m) == 1:
        return [1, 1]
    m_a, split = orderarray(m)
    r_m = m_a[split:, :split]
    q_m = m_a[split:, split:]
    identity_m = np.identity(len(q_m))
    f = np.linalg.inv(identity_m - q_m)
    fr = np.matmul(f, r_m)

    ans = getfractions(fr[0])

    return ans


def main():
    # Test case 1
    output = solution(
        [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]])
    if output == [0, 3, 2, 9, 14]:
        print("Pass!", output)
    else:
        print("Fail!", output)

    # Test case 2
    output = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    if output == [7, 6, 8, 21]:
        print("Pass!", output)
    else:
        print("Fail!", output)


if __name__ == "__main__":
    main()