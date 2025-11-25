import pytest


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

    @staticmethod
    def is_prime_number(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


class TestCalculator:
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (2, 3, 5),
            (-2, 5, 3),
            (0, 0, 0),
            (1.5, 2.5, 4.0)
        ]
    )
    def test_add(self, a, b, expected):
        assert Calculator.add(a, b) == expected

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (10, 4, 6),
            (-1, -1, 0),
            (3.5, 1.2, 2.3)
        ]
    )
    def test_subtract(self, a, b, expected):
        result = Calculator.subtract(a, b)
        if any(isinstance(x, float) for x in (a, b, expected)):
            assert result == pytest.approx(expected)
        else:
            assert result == expected

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (7, 6, 42),
            (0, 100, 0),
            (-3, 5, -15),
            (2.5, 4, 10.0)
        ]
    )
    def test_multiply(self, a, b, expected):
        result = Calculator.multiply(a, b)
        if any(isinstance(x, float) for x in (a, b, expected)):
            assert result == pytest.approx(expected)
        else:
            assert result == expected

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (9, 3, 3),
            (7, 2, 3.5),
            (-10, 2, -5),
            (5.0, 2.0, 2.5)
        ]
    )
    def test_divide_ok(self, a, b, expected):
        result = Calculator.divide(a, b)
        assert result == pytest.approx(expected)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(10, 0)

    @pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 97, 9973])
    def test_is_prime_true(self, n):
        assert Calculator.is_prime_number(n) is True

    @pytest.mark.parametrize("n", [-10, -1, 0, 1, 4, 6, 9, 100, 10000])
    def test_is_prime_false(self, n):
        assert Calculator.is_prime_number(n) is False
