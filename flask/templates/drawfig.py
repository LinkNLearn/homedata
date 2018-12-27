
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins
plt.ioff() # turn matplotlib interactive mode off

# Data input, global variables x and y
y=[3,1,4,1,5]
x=range(len(y)) # 0 to length of y for x-axis

def draw_fig():
    """
    Returns html equivalent of matplotlib figure
    Parameters
    ----------  (None)
    Returns
    ----------  d3 representation of figure
    """
    fig = plt.figure() # create fig object
    fid = plt.plot(x,y) # create plot within that fig

    # Using documentation from here https://mpld3.github.io/modules/API.html#mpld3.save_html
    # We save the figure as 'savedplot.html', saving the plot rendered as an html document
    return mpld3.save_html(fig, 'savedplot2.html')

draw_fig()
