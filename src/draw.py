import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, LabelSet
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

# debug_pallette = Spectral8
# debug_pallette.append('#FF0000')
# debug_pallette.append('#0000FF')

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=20, fill_color='color')


# This is drawing the edges for start to end
graph.edge_renderer.data_source.data = dict(
    start=node_indices,  # this is why all the edges start from the first vertex
    end=node_indices[1:])


# def get_edge_indexes(graph):
#     start_indices = []
#     end_indices = []

#     for start, vertex in enumerate(graph_data.vertexes):
#         for ed in vertex.edges:
#             start_indices.append(start)
#             end_indices.append(graph_data.vertexes.index(ed.destination))

#     return dict(start=start_indices, end=end_indices)


# graph.edge_renderer.data_source.data = get_edge_indexes(graph)


def get_positions():
    return [v.pos for v in graph_data.vertexes]


def get_values():
    return [v.value for v in graph_data.vertexes]


def setup_labels(graph):
    labelSource = ColumnDataSource(data=dict(
        x=[pos['x'] for pos in get_positions()],
        y=[pos['y'] for pos in get_positions()],
        values=get_values()))

    labels = LabelSet(x='x', y='y', text='values', level='glyph', text_align='center',
                      text_baseline='middle', source=labelSource, render_mode='canvas')

    return labels


x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)
plot.add_layout(setup_labels(graph))

output_file('graph.html')
show(plot)
