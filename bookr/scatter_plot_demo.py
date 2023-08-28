from plotly.offline import plot
import plotly.graph_objs as graphs


def generate_scatter_plot(x_axis, y_axis):
    """Generate a scatter plot for the provided x and y-axis values."""
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=x_axis, y=y_axis)
    figure.add_trace(scatter)
    return plot(figure, output_type='div')


def generate_html(plot_html):
    """Generate an HTML page for the provided plot."""
    html_content = f"<html><head><title>Plot Demo</tilte></head><body>{plot_html}</body></html>"
    .format(plot_html)