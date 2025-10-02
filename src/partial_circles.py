import numpy
import matplotlib.pyplot as pyplot


def make_2d_partial_circles(
        n_samples=250,
        n_circles=2,
        *,
        center_box = (-10, 10)
):

    samples_per_shape = n_samples // n_circles
    leftover_samples = n_samples - (samples_per_shape * n_circles)

    shape_samples = numpy.full(n_circles, samples_per_shape)

    for x in range(0, leftover_samples):
        shape_samples[x] = shape_samples[x] + 1

    x = []
    y = []

    for i in range(0, n_circles):
        circle_size = numpy.random.rand() * 5

        linspace = numpy.linspace(0, (1.0 + numpy.random.rand()) * numpy.pi, shape_samples[i])

        circle_x = numpy.cos(linspace) * circle_size
        circle_y = numpy.sin(linspace) * circle_size

        circle_loc = numpy.random.uniform(center_box[0], center_box[1], size=2)

        for j in range(0, shape_samples[i]):
            x.append(numpy.random.normal(loc=(circle_x[j] + circle_loc[0], circle_y[j] + circle_loc[1]), scale=0.1, size=2))
            y.append(i)

    return x, y


def main():
    x, y = make_2d_partial_circles(
        n_samples=500,
        n_circles=5,
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

