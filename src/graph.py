class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value, **pos):  # TODO: test default arguments
        self.edges = []
        self.value = value
        self.pos = pos
        self.color = 'white'


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=40, y=40)
        debug_vertex_2 = Vertex('t2', x=100, y=100)
        debug_vertex_3 = Vertex('t3', x=300, y=400)
        debug_vertex_4 = Vertex('t3', x=400, y=100)
        print(debug_vertex_1.pos['x'])

        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_2)
        debug_vertex_3.edges.append(debug_edge_2)

        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])
