from bokeh.plotting import figure, output_file, show

def bokeh_print():
    x = [1,2,3,4,5,6]
    y = [4,5,7,8,9,10]

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    fig = figure(title="some line example", x_axis_label='x', y_axis_label='y')

    # add a line renderer with legend and line thickness
    fig.line(x, y, legend="Line", line_width=2)

    # show the results
    show(fig)

if __name__ == "__main__":
    bokeh_print()