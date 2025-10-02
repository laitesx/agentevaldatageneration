import numpy
import matplotlib.pyplot as pyplot


def make_2d_blobs_and_moons(
        n_samples=250,
        n_clusters=2,
        n_moons=2,
        *,
        center_box=(-10, 10)
):

    shape_count = n_clusters + n_moons

    samples_per_shape = n_samples // shape_count
    leftover_samples = n_samples - (samples_per_shape * shape_count)

    shape_samples = numpy.full(shape_count, samples_per_shape)

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

    for i in range(0, n_moons):
        moon_shape = numpy.random.randint(0, 2)

        moon_x = None
        moon_y = None

        if moon_shape == 0:
            moon_x = numpy.cos(numpy.linspace(0, numpy.pi, shape_samples[i + n_clusters]))
            moon_y = numpy.sin(numpy.linspace(0, numpy.pi, shape_samples[i + n_clusters]))
        else:
            moon_x = 1 - numpy.cos(numpy.linspace(0, numpy.pi, shape_samples[i + n_clusters]))
            moon_y = 1 - numpy.sin(numpy.linspace(0, numpy.pi, shape_samples[i + n_clusters]))

        moon_loc = numpy.random.uniform(center_box[0], center_box[1], size=2)

        for j in range(0, shape_samples[i + n_clusters]):
            x.append(numpy.random.normal(loc=(moon_x[j] + moon_loc[0], moon_y[j] + moon_loc[1]), scale=0.1, size=2))
            y.append(i + n_clusters)

    return x, y


def main():
    x, y = make_2d_blobs_and_moons(
        n_samples=500,
        n_clusters=4
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
