import unittest
import random
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        for _ in range(50):
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            self.assertEqual(katas.add(x, y), x + y)

    def test_multiply(self):
        for _ in range(50):
            x = random.randint(-50, 50)
            y = random.randint(-50, 50)
            self.assertEqual(katas.multiply(x, y), x * y)

    def test_power(self):
        for _ in range(50):
            x = random.randint(0, 50)
            y = random.randint(0, 50)
            self.assertEqual(katas.power(x, y), x ** y)
        with self.assertRaises(ValueError):
            katas.power(5, -5)
            katas.power(5, 2.5)

    def test_factorial(self):
        factorials = (
            1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
            39916800, 479001600, 6227020800, 87178291200, 1307674368000
        )
        for i, f in enumerate(factorials):
            self.assertEqual(katas.factorial(i), f)
        with self.assertRaises(ValueError):
            katas.factorial(-7)

    def test_fibonacci(self):
        fibonacci_seq = (
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
            17711, 28657, 46368, 75025, 121393, 196418, 317811
        )
        for n, f in enumerate(fibonacci_seq):
            self.assertEqual(
                katas.fibonacci(n),
                fibonacci_seq[n],
            )
        with self.assertRaises(ValueError):
            katas.fibonacci(-22)


if __name__ == '__main__':
    unittest.main()
