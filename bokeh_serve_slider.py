# Reference
# https://stackoverflow.com/questions/49800444/bokeh-and-how-to-make-it-into-a-gui
# usage
# bokeh serve --show bokeh_serve_slider.py
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

# Set up data
x = np.linspace(0, 4*np.pi, 200)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(title="my sine wave")
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# Set up widgets
freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)


# Set up callbacks
def update_data(attrname, old, new):

    # Get the current slider values and set new data
    k = freq.value
    x = np.linspace(0, 4*np.pi, 200)
    y = np.sin(k*x)
    source.data = dict(x=x, y=y)

freq.on_change('value', update_data)

# Set up layouts and add to document
curdoc().add_root(column(freq, plot))
curdoc().title = "Sliders"
