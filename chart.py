from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas

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

    # car = data_frame['Car']
    # horse_power = data_frame['Horsepower']

    # Create ColumnDataSource from data frame
    source = ColumnDataSource(data_frame)

    output_file('index.html')
    # Car list
    car_list = source.data['Car'].tolist()

    # create a new plot with a title and axis labels
    fig = figure(
    #    y_range=car, # using 
        y_range=car_list,
        plot_width=700,
        plot_height=400,
        title="Cars with top horsepower",
        x_axis_label='Horsepower',
        y_axis_label='Cars',
        tools="pan,box_select,zoom_in,zoom_out,save,reset",
        toolbar_location=None)

    #ranger graph
    # https://bokeh.pydata.org/en/latest/docs/reference/models/glyphs/hbar.html
    fig.hbar(
        # y=car,
        # right=horse_power,
        y='Car',
        right='Horsepower',
        left=0,
        height=0.5,
        #color="#ff1200",
        fill_color=factor_cmap(
            'Car',
            palette=Blues8,
            factors=car_list
        ),
        fill_alpha=0.8,
        source=source,
        legend='Car'

    )
    fig.toolbar_location = 'above'

    # Add Legend
    fig.legend.orientation = 'vertical'
    fig.legend.location = 'top_right'
    # print(fig.legend.__dir__())
    fig.legend.label_text_font_size = '10px'

    # Add Tooltips
    hover = HoverTool()
    hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>HP: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width="200" /></div>
    </div>
    """
    fig.add_tools(hover)

     # show the results
    # show(fig) #like f5
    save(fig)

    # Use compoenten from bokeh.embed to prepare script and div
    ## IMPORTANT - use it then in respond!!
    script, div = components(fig)
    # print(div)
    # print(script)
    f= open("fig.div","w")
    f.write(div)
    f.write(script)
    f.close()

if __name__ == "__main__":
    # bokeh_print()
    data_plot()
