import unittest
from main import quadratic_roots


class TestQuadraticRoots(unittest.TestCase):

    def test_two_real_roots(self):
        self.assertEqual(quadratic_roots(1, -3, 2), (2.0, 1.0))

    def test_one_real_root(self):
        self.assertEqual(quadratic_roots(1, 2, 1), (-1.0))

    def test_two_complex_roots(self):
        roots = quadratic_roots(1, 0, 1)
        self.assertTrue(all(isinstance(root, complex) for root in roots))
        self.assertEqual(roots[0], complex(0, 1))
        self.assertEqual(roots[1], complex(0, -1))

    def test_zero_coefficient_a(self):
        with self.assertRaises(ValueError) as context:
            quadratic_roots(0, 1, 1)
        self.assertEqual(str(context.exception), "Коэффициент a не должен быть равен 0 для квадратного уравнения")

    def test_non_numeric_coefficients(self):
        with self.assertRaises(ValueError) as context:
            quadratic_roots(1, 'b', 3)
        self.assertEqual(str(context.exception), "Коэффиценты должны быть числами")

    def test_negative_discriminant(self):
        roots = quadratic_roots(1, 1, 1)
        self.assertTrue(all(isinstance(root, complex) for root in roots))
        self.assertAlmostEqual(roots[0].real, -0.5)
        self.assertAlmostEqual(roots[1].real, -0.5)

    def test_large_coefficients(self):
        roots = quadratic_roots(1000000, 5000000, 1000000)
        self.assertTrue(all(isinstance(root, complex) for root in roots))

if __name__ == '__main__':
    unittest.main()

