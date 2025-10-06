import numpy
import matplotlib.pyplot as pyplot


def make_2d_divided_land_dataset(
        n_mid_line_samples = 100,
        n_mid_line_outliers = 10,
        n_samples=250,
        n_outliers=25,
        n_clusters=2,
        *,
        center_box=(-10, 10)
):

    samples_per_shape = n_samples // n_clusters
    leftover_samples = n_samples - (samples_per_shape * n_clusters)

    shape_samples = numpy.full(n_clusters, samples_per_shape)

    for x in range(0, leftover_samples):
        shape_samples[x] = shape_samples[x] + 1

    x = []
    y = []

    cluster_centers = []

    for i in range(0, n_clusters):
        cluster_centers.append(numpy.random.uniform(center_box[0], center_box[1], size=2))

        for j in range(0, shape_samples[i]):
            x.append(numpy.random.normal(loc=cluster_centers[i], scale=1.0, size=2))
            y.append(i)

    for i in range(0, n_outliers):
        outlier_cluster = numpy.random.randint(0, n_clusters)
        outlier_loc = numpy.random.normal(loc=cluster_centers[outlier_cluster], scale=3.0, size=2)
        x.append(outlier_loc)
        y.append(outlier_cluster)

    for i in range(0, n_mid_line_samples):
        random_point = numpy.random.uniform(center_box[0], center_box[1])
        x.append([random_point, random_point])
        y.append(n_clusters)

    for i in range(0, n_mid_line_outliers):
        random_point = numpy.random.uniform(center_box[0], center_box[1])
        x.append(numpy.random.normal(loc=[random_point, random_point], scale=1.5, size=2))
        y.append(n_clusters)

    return x, y, cluster_centers


def main():
    x, y, cluster_centers = make_2d_divided_land_dataset(
        n_mid_line_samples=250,
        n_mid_line_outliers=25,
        n_samples=450,
        n_clusters=4,
        n_outliers=50
    )

    x_coords = [a[0] for a in x]
    y_coords = [a[1] for a in x]

    color_box = { 0: 'red', 1: 'green', 2: 'blue', 3: 'orange', 4: 'purple', 5: 'black', 6: 'gray' }

    colors = []

    for i in range(0, len(x_coords)):
        colors.append(color_box[y[i]])

    pyplot.scatter(x_coords, y_coords, c=colors)
    pyplot.xlim(-15, 15)
    pyplot.ylim(-15, 15)
    pyplot.show()


if __name__ == "__main__":
    main()

