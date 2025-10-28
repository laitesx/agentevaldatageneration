import unittest
import math

try:
    from src.divided_land_dataset import make_2d_divided_land_dataset
except ImportError:
    from ..src.divided_land_dataset import make_2d_divided_land_dataset


class TestDividedLandDataset(unittest.TestCase):
    def test_make_2d_divided_land_dataset(self):
        x, y, cluster_centers = make_2d_divided_land_dataset(
            n_mid_line_samples=100,
            n_mid_line_outliers=10,
            n_samples=500,
            n_outliers=50,
            n_clusters=3,
            center_box=(-5, 5)
        )

        self.assertEqual(len(x), 660, "Wrong number of points generated.")
        self.assertEqual(len(y), 660, "Wrong number of point classes generated.")
        self.assertEqual(min(y), 0, "Class less than 0 found.")
        self.assertEqual(max(y), 3, "Class greater than 3 found.")

        self.assertIn(0, y, "Class 0 not found.")
        self.assertIn(1, y, "Class 1 not found.")
        self.assertIn(2, y, "Class 2 not found.")
        self.assertIn(3, y, "Class 3 not found.")

    def test_make_2d_divided_land_dataset_no_outliers(self):
        x, y, cluster_centers = make_2d_divided_land_dataset(
            n_mid_line_samples=100,
            n_mid_line_outliers=0,
            n_samples=500,
            n_outliers=0,
            n_clusters=3,
            center_box=(-5, 5)
        )

        self.assertEqual(len(x), 600, "Wrong number of points generated.")
        self.assertEqual(len(y), 600, "Wrong number of point classes generated.")
        self.assertEqual(min(y), 0, "Class less than 0 found.")
        self.assertEqual(max(y), 3, "Class greater than 3 found.")

        self.assertIn(0, y, "Class 0 not found.")
        self.assertIn(1, y, "Class 1 not found.")
        self.assertIn(2, y, "Class 2 not found.")
        self.assertIn(3, y, "Class 3 not found.")

        for i in range(500):
            self.assertEqual(len(x[i]), 2)

            if x[i][0] < -9 or x[i][0] > 9 or x[i][1] < -9 or x[i][1] > 9:
                self.fail("Out of bounds value found in point " + str(x[i]))

            point_class = y[i]
            self.assertLess(math.dist(x[i], cluster_centers[point_class]), 6, "For class " + str(point_class) + " point " + str(x[i]) + " is " + str(math.dist(x[i], cluster_centers[point_class])) + " away from center " + str(cluster_centers[point_class]))

        for i in range(100):
            self.assertEqual(len(x[i + 500]), 2)

            if x[i][0] < -9 or x[i][0] > 9 or x[i][1] < -9 or x[i][1] > 9:
                self.fail("Out of bounds value found in point " + str(x[i]))

            self.assertEqual(x[i + 500][0], x[i + 500][1])
