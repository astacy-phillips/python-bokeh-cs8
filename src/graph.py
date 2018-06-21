import random


class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value='default', **pos):  # TODO: test default arguments
        self.edges = []
        self.value = value
        self.pos = pos
        self.color = 'white'


class Graph:
    def __init__(self):
        self.vertexes = []


    def bfs(self, start):
        random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0)  # TODO: Look into collections.dequeue

        return found

    def connected_components(self):
        need_reset = []
        for vertex in self.vertexes:
            if vertex.color is 'white' or vertex.color not in need_reset:
                self.bfs(vertex)
                need_reset.append(vertex)
                


    def randomize(self, width, height, px_box, probability=0.6):
        def connect_verts(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        count = 0

        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex()
                count += 1
                v.value = 'v' + str(count)
                row.append(v)

            grid.append(row)
        
        for y in range(height):
            for x in range(width):
                # Connect down
                if y < height - 1:
                    if random.random() < probability:
                        connect_verts(grid[y][x], grid[y+1][x])
                # Connect right
                if x < width - 1:
                    if random.random() < probability:
                        connect_verts(grid[y][x], grid[y][x+1])

        box_buffer = 0.8
        box_inner = px_box * box_buffer
        box_inner_offset = (px_box - box_inner) / 2

        for y in range(height):
            for x in range(width):
                grid[y][x].pos = dict(
                    x=x * px_box + box_inner_offset + random.random() * box_inner,
                    y=y * px_box + box_inner_offset + random.random() * box_inner
                )

        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])
