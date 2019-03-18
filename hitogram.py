from bokeh.plotting import figure, output_file
from bokeh.io import show, save
import pandas
import numpy as np

# Import the ColumnDataSource class, HoverTool for tooltips - https://bokeh.pydata.org/en/latest/docs/reference/models/sources.html
from bokeh.models import ColumnDataSource, HoverTool


def show_histogram(use_colum_data_source):
    # Read the data from a csv into a dataframe
    flights = pandas.read_csv('./flight.csv', index_col=0)
    output_file("flights.html",  title="First more complicated bokeh example")

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

    # Add a column showing the extent of each interval
    delays['f_interval'] = ['%d to %d minutes' %
                            (left, right) for left, right in zip(delays['left'], delays['right'])]
    print(delays)

    # Create the blank plot
    p = figure(plot_height=600, plot_width=600,
            
               title='Histogram of Arrival Delays for NY in 2013',
               x_axis_label='Delay [min]',
               y_axis_label='Number of Flights')

    if use_colum_data_source:
        # Convert dataframe to column data source
        src = ColumnDataSource(delays)
        print(src.data.keys())
        # Add a quad glyph with source this time
        p.quad(source=src,
               bottom=0,
               top='arr_delay',
               left='left', right='right',
               hover_fill_alpha=1.0,
               fill_alpha=0.75, hover_fill_color='navy',
               fill_color='red', line_color='black',
               legend='Delay statistics', muted_alpha=0.1)

        p.legend.click_policy="mute"

        # Hover tool referring to our own data field using @ and
        # a position on the graph using $
        hover = HoverTool(tooltips=[('Delay of flights ', '@f_interval'),  # ('Delay of flights ', '@left'),
                                    ('Dalay No', '@arr_delay'),
                                    ('(x,y)', '($x{0}, $y{0,0.0})')]) #formatting added
        hover.show_arrow = False

        # Add the hover tool to the graph
        p.add_tools(hover)

    else:  # ordinary approach
         # Add a quad glyph
        p.quad(bottom=0, top=delays['arr_delay'],
               left=delays['left'], right=delays['right'],
               fill_color='red', line_color='black')

    # style before print
    p = style(p)

    # Show/Save the plot
    # show(p)
    save(p)


# Styling for a plot - in seperate function
def style(p):
    # Title
    p.title.align = 'center'
    p.title.text_font_size = '20pt'
    p.title.text_font = 'serif'

    # Axis titles
    p.xaxis.axis_label_text_font_size = '14pt'
    p.xaxis.axis_label_text_font_style = 'bold'
    p.yaxis.axis_label_text_font_size = '14pt'
    p.yaxis.axis_label_text_font_style = 'bold'

    # Tick labels
    p.xaxis.major_label_text_font_size = '12pt'
    p.yaxis.major_label_text_font_size = '12pt'

    return p


if __name__ == "__main__":
    show_histogram(True)
