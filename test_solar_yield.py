import unittest

from solar_yield import annual_energy, capacity_factor


class SolarYieldTests(unittest.TestCase):
    def test_reference_array(self):
        self.assertAlmostEqual(annual_energy(10, 0.20, 1800, 0.8), 2880)

    def test_degradation(self):
        self.assertAlmostEqual(annual_energy(10, 0.20, 1800, 0.8, 1), 2865.6)

    def test_capacity_factor(self):
        self.assertAlmostEqual(capacity_factor(1752, 1), 0.2)


if __name__ == "__main__":
    unittest.main()
