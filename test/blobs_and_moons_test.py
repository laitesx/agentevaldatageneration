import unittest
import math

from src.blobs_and_moons import make_2d_blobs_and_moons


class TestBlobsAndMoons(unittest.TestCase):
    def test_blobs_and_moons(self):
        x, y, cluster_centers, moon_locs = make_2d_blobs_and_moons(
            n_samples=500,
            n_clusters=3,
            n_moons=3,
            center_box=(-5, 5)
        )

        self.assertEqual(len(x), 500, "Wrong number of points generated.")
        self.assertEqual(len(y), 500, "Wrong number of point classes generated.")
        self.assertEqual(min(y), 0, "Class less than 0 found.")
        self.assertEqual(max(y), 5, "Class greater than 5 found.")
        self.assertEqual(len(cluster_centers), 3, "Wrong number of clusters generated.")
        self.assertEqual(len(moon_locs), 3, "Wrong number of moon locations generated.")

        self.assertIn(0, y, "Class 0 not found.")
        self.assertIn(1, y, "Class 1 not found.")
        self.assertIn(2, y, "Class 2 not found.")
        self.assertIn(3, y, "Class 3 not found.")
        self.assertIn(4, y, "Class 4 not found.")
        self.assertIn(5, y, "Class 5 not found.")

        for i in range(0, len(x)):
            self.assertEqual(len(x[i]), 2)

            if x[i][0] < -9 or x[i][0] > 9 or x[i][1] < -9 or x[i][1] > 9:
                self.fail("Out of bounds value found in point " + str(x[i]))

            point_class = y[i]

            if point_class < 3:
                self.assertLess(math.dist(x[i], cluster_centers[point_class]), 6, "For class " + str(point_class) + " point " + str(x[i]) + " is " + str(math.dist(x[i], cluster_centers[point_class])) + " away from center " + str(cluster_centers[point_class]))
            else:
                self.assertLess(math.dist(x[i], moon_locs[point_class - 3]), 6, "For class " + str(point_class) + " point " + str(x[i]) + " is " + str(math.dist(x[i], moon_locs[point_class - 3])) + " away from center " + str(moon_locs[point_class - 3]))
