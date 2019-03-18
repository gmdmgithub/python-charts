
from bokeh.plotting import figure, output_file
from bokeh.io import show, save
import pandas
import numpy as np

def show_histogram():
    # Read the data from a csv into a dataframe
    flights = pandas.read_csv('./flight.csv', index_col=0)
    output_file("flights.html")

    # Summary stats for the column of interest
    print(flights['arr_delay'].describe())

    """Bins will be five minutes in width, so the number of bins 
    is (length of interval / 5). Limit delays to [-60, +120] minutes using the range."""
    arr_hist, edges = np.histogram(flights['arr_delay'],
                                   bins=int(180/5),
                                   range=[-60, 120])
    # Put the information in a dataframe
    delays = pandas.DataFrame({'arr_delay': arr_hist,
                           'left': edges[:-1],
                           'right': edges[1:]})

    print(delays)

    # Create the blank plot
    p = figure(plot_height=600, plot_width=600,
               title='Histogram of Arrival Delays',
               x_axis_label='Delay (min)]',
               y_axis_label='Number of Flights')

    # # Add a quad glyph
    p.quad(bottom=0, top=delays['arr_delay'],
           left=delays['left'], right=delays['right'],
           fill_color='red', line_color='black')

    # # Save the plot
    save(p)


if __name__ == "__main__":
    show_histogram()
