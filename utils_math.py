from fractions import Fraction


def greatest_common_divisor(num1: int, num2: int) -> int:
    while num2:
        num1, num2 = num2, num1 % num2

    return num1

def lowest_common_multiple(num1: int, num2: int) -> int:
    return (num1 * num2) // greatest_common_divisor(num1, num2)


def normalize_ratio_three(a: float, b: float, c: float) -> (int, int, int):
    f1, f2 = Fraction(a / c), Fraction(b / c)
    c = lowest_common_multiple(f1.denominator, f2.denominator)
    a, b = f1.numerator * (c // f1.denominator), f2.numerator * (c // f2.denominator)

    return a, b, c