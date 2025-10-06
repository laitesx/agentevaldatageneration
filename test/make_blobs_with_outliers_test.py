import unittest
import math

from src.make_blobs_with_outliers import make_2d_blobs_with_outliers


class TestMakeBlobsWithOutliers(unittest.TestCase):
    def test_make_2d_blobs_with_outliers(self):
        x, y, cluster_centers = make_2d_blobs_with_outliers(
            n_samples=500,
            n_outliers=100,
            n_clusters=5,
            center_box=(-5, 5)
        )

        self.assertEqual(len(x), 600, "Wrong number of points generated.")
        self.assertEqual(len(y), 600, "Wrong number of point classes generated.")
        self.assertEqual(min(y), 0, "Class less than 0 found.")
        self.assertEqual(max(y), 4, "Class greater than 5 found.")
        self.assertEqual(len(cluster_centers), 5, "Wrong number of clusters generated.")

        self.assertIn(0, y, "Class 0 not found.")
        self.assertIn(1, y, "Class 1 not found.")
        self.assertIn(2, y, "Class 2 not found.")
        self.assertIn(3, y, "Class 3 not found.")
        self.assertIn(4, y, "Class 4 not found.")

        for i in range(0, len(x)):
            self.assertEqual(len(x[i]), 2)

            if x[i][0] < -18 or x[i][0] > 18 or x[i][1] < -18 or x[i][1] > 18:
                self.fail("Out of bounds value found in point " + str(x[i]))

            point_class = y[i]
            self.assertLess(math.dist(x[i], cluster_centers[point_class]), 12, "For class " + str(point_class) + " point " + str(x[i]) + " is " + str(math.dist(x[i], cluster_centers[point_class])) + " away from center " + str(cluster_centers[point_class]))
