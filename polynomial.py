from __future__ import annotations

import copy
from typing import List, Union


class Polynomial:

    def __init__(self, coefficients: List[Union[int, float]]):
        self.coefficients = coefficients
        self.len = len(self.coefficients)

    def __str__(self):
        """Converts a Polynomial into a string"""
        order = self.len - 1
        represent = []
        for coe in self.coefficients:
            if coe == 0:
                continue
            represent.append("- " if coe < 0 else "+ ")
            represent.append(str(format(coe, '.3f')))
            represent.append(" ")
            if order > 0:
                represent.append("z")

            if order > 1:
                represent.append(f"**{order}")

            represent.append(" ")
            order -= 1

        return "".join(represent)[2:-2]

    def __repr__(self):
        return str(self)

    def __call__(self, value: Union[int, float]) -> Union[int, float]:
        return self.val(value)

    def __add__(self, other: Polynomial) -> Polynomial:
        return self.add(other)

    def __sub__(self, other: Polynomial) -> Polynomial:
        return self.sub(other)

    def __mul__(self, other: Union[int, float, Polynomial]) -> Polynomial:
        return self.mul(other)

    def get_coefficient(self, i: int) -> Union[int, float]:
        """Return the coefficient of the x^i term of polynomial"""
        return self.coefficients[self.len - i - 1]

    def val(self, value: Union[int, float]) -> float:
        """Returns the numerical result of evaluating the polynomial when x equals value"""
        res = 0
        i = self.len - 1
        while i >= 0:
            res += self.coefficients[i] * value ** (self.len - i - 1)
            i -= 1

        return float(res)

    def add(self, other: Polynomial) -> Polynomial:
        """Returns a new Polynomial representing the sum of Polynomials self and other"""

        large_coefficients = copy.deepcopy(other.coefficients)
        small_coefficients = copy.deepcopy(self.coefficients)

        if self.len > len(other.coefficients):
            large_coefficients = copy.deepcopy(self.coefficients)
            small_coefficients = copy.deepcopy(other.coefficients)


        i, j = len(large_coefficients) - 1, len(small_coefficients) - 1
        while j >= 0:
            large_coefficients[i] += small_coefficients[j]
            i -= 1
            j -= 1

        return Polynomial(large_coefficients)

    def sub(self, other: Polynomial) -> Polynomial:
        """Returns a new Polynomial representing the subtract of Polynomials self and other"""

        minuend = copy.deepcopy(self.coefficients)
        subtrahend = [-coefficient for coefficient in other.coefficients]

        large_coefficients = subtrahend
        small_coefficients = minuend

        if self.len > len(other.coefficients):
            large_coefficients = minuend
            small_coefficients = subtrahend

        i, j = len(large_coefficients) - 1, len(small_coefficients) - 1
        while j >= 0:
            large_coefficients[i] += small_coefficients[j]
            i -= 1
            j -= 1

        return Polynomial(large_coefficients)

    def mul(self, other: Union[int, float, Polynomial]) -> Polynomial:
        """returns a new Polynomial representing the product of Polynomials self and other"""
        if isinstance(other, (int, float)):
            return Polynomial(self._mul_constant(self.coefficients, other))

        multiplicand = copy.deepcopy(self.coefficients)
        multiplier = copy.deepcopy(other.coefficients)

        if self.len < len(other.coefficients):
            multiplicand, multiplier = multiplier, multiplicand

        product = Polynomial([0 for _ in range(len(multiplicand))])
        i = len(multiplier) - 1
        while i >= 0:
            temp_coefficients = self._mul_constant(multiplicand, multiplier[i]) + \
                                [0 for _ in range(len(multiplier) - i - 1)]
            product = product.add(Polynomial(temp_coefficients))
            i -= 1

        return product

    @staticmethod
    def _mul_constant(poly: List[Union[int, float]], const: Union[int, float]) \
            -> List[Union[int, float]]:
        return [coefficient * const for coefficient in poly]

if __name__ == '__main__':
    p1 = Polynomial([1, 2, 3])
    p2 = Polynomial([100, 200])
    print(p1)
    print(p1.add(p2))
    print(p1 + p2)
    print(p1(1))
    print(p1(-1))
    print((p1 + p2)(10))
    print(p1.mul(p1))
    print(p1 * p1)
    print(p1 * p2 + p1)

