

class Graph:

    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex] = []

    def add_edge(self, vertex_one, vertex_two):
        self.verticies[vertex_one] = self.vertices[vertex_one].append(vertex_two)