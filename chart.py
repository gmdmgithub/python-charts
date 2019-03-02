from bokeh.plotting import figure, output_file, show


def bokeh_print():
    x = [1, 2, 3, 4, 5, 6]
    y = [4, 5, 8, 4, 3, 6]

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    fig = figure(title="some line example",
                 x_axis_label='x axis', y_axis_label='y axis')

    # add a line renderer with legend and line thickness
    fig.line(x, y, legend="Trend line", line_width=2)

    # show the results
    show(fig)


def data_plot():
    """"plots data from csv file"""

    # Read in csv
    data_frame = pandas.read_csv('sample.csv')

    car = data_frame['Car']
    horse_power = data_frame['Horsepower']
    output_file('index.html')

    # create a new plot with a title and axis labels
    fig = figure(
        y_range=car,
        plot_width=800,
        plot_height=600,
        title="Cars with top horsepower",
        x_axis_label='horpower'
        tools="")

    #ranger graph
    # https://bokeh.pydata.org/en/latest/docs/reference/models/glyphs/hbar.html
    fig.hbar(
        y=car,

    )


if __name__ == "__main__":
    bokeh_print()
