import math
import copy
from queue import Queue

class DistanceMatricesCreator:

  def create_graph(self, adj_matrix):
    n_simplices = range(len(adj_matrix))
    graph = { s: [] for s in n_simplices }
    for i in n_simplices:
      simplex = adj_matrix[i]
      for j in range(i, len(simplex)):
        if i != j and adj_matrix[i][j] == 1:
          graph[i].append(j)
          graph[j].append(i)
    return graph

  def calculate_distance(self, input_graph, source):
    Q = Queue()
    distance_dict = { s: math.inf for s in input_graph.keys() }
    visited_simplices = list()
    Q.put(source)
    visited_simplices.append(source)
    while not Q.empty():
      simplex = Q.get()
      if simplex == source:
        distance_dict[simplex] = 0
      for u in input_graph[simplex]:
        if u not in visited_simplices:
          if distance_dict[u] > distance_dict[simplex] + 1:
            distance_dict[u] = distance_dict[simplex] + 1
          Q.put(u)
          visited_simplices.append(u)
    return distance_dict

  def create_distance_matrices(self, adj_matrices, source):
    distances = dict()
    for q, adj_matrix in adj_matrices.items():
      q_graph = self.create_graph(adj_matrix)
      distances[q] = self.calculate_distance(q_graph, source)
    return distances
