import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, LabelSet
from bokeh.palettes import Spectral8

from graph import *

WIDTH = 640
HEIGHT = 480  # TODO: Currently graph renders square, scale to numbers here.
CIRCLE_SIZE = 30

graph_data = Graph()
graph_data.randomize(5, 4, 115, 0.6)
graph_data.connected_components()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)


plot = figure(title='Graph Layout Demonstration', x_range=(0, WIDTH), y_range=(0, HEIGHT),
              tools='', plot_width=WIDTH, plot_height=HEIGHT, toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=CIRCLE_SIZE, fill_color='color')


# This is drawing the edges for start to end

def get_edge_indexes(graph):
    start_indexes = []
    end_indexes = []

    for start_index, vertex in enumerate(graph_data.vertexes):
        for edge in vertex.edges:
            start_indexes.append(start_index)
            end_indexes.append(graph_data.vertexes.index(edge.destination))

    return dict(start=start_indexes, end=end_indexes)


graph.edge_renderer.data_source.data = get_edge_indexes(graph)

x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]
# def get_positions():
#     return [v.pos for v in graph_data.vertexes]


def get_values():
    return [v.value for v in graph_data.vertexes]


def setup_labels(graph):
    label_source = ColumnDataSource(data=dict(
        # x=[pos['x'] for pos in get_positions()],
        # y=[pos['y'] for pos in get_positions()],
        x=x,
        y=y,
        values=get_values()))

    labels = LabelSet(x='x', y='y', text='values', level='overlay', text_align='center',
                      text_baseline='middle', source=label_source, render_mode='canvas')

    return labels


graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(setup_labels(graph))

output_file('graph.html')
show(plot)
