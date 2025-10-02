import numpy
import matplotlib.pyplot as pyplot


def make_2d_squares_and_blobs_with_outliers(
        n_samples = 250,
        n_outliers = 25,
        n_clusters = 2,
        n_squares = 2,
        *,
        center_box = (-10, 10)):

    shape_count = n_clusters + n_squares

    samples_per_shape = n_samples // shape_count
    leftover_samples = n_samples - (samples_per_shape * shape_count)

    shape_samples = numpy.full(shape_count, samples_per_shape)

    for x in range(0, leftover_samples):
        shape_samples[x] = shape_samples[x] + 1

    x = []
    y = []

    cluster_centers = []
    square_centers = []

    for i in range(0, n_clusters):
        cluster_centers.append(numpy.random.uniform(center_box[0], center_box[1], size=2))

        for j in range(0, shape_samples[i]):
            x.append(numpy.random.normal(loc=cluster_centers[i], scale=1.0, size=2))
            y.append(i)

    for i in range(0, n_squares):
        square_centers.append(numpy.random.uniform(center_box[0], center_box[1], size=2))

        for j in range(0, shape_samples[i + n_clusters]):
            x_point = numpy.random.uniform(square_centers[i][0], square_centers[i][1])
            y_point = numpy.random.uniform(square_centers[i][0], square_centers[i][1])

            x.append(numpy.random.normal(loc=(x_point, y_point), scale=0.1, size=2))
            y.append(i + n_clusters)

    for i in range(0, n_outliers):
        outlier_shape = numpy.random.randint(0, n_clusters + n_squares)

        if outlier_shape < n_clusters:
            outlier_loc = numpy.random.normal(loc=cluster_centers[outlier_shape], scale=3.0, size=2)
            x.append(outlier_loc)
            y.append(outlier_shape)
        else:
            outlier_loc = numpy.random.normal(loc=square_centers[outlier_shape - n_clusters], scale=3.0, size=2)
            x.append(outlier_loc)
            y.append(outlier_shape)

    return x, y


def main():
    x, y = make_2d_squares_and_blobs_with_outliers(
        n_samples=500
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

