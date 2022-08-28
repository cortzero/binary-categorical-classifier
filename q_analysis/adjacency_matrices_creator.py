'''
This module provides a class that will help to create the adjacency matrices for each dimension of a simplicial complex.
'''

import numpy as np

class AdjacencyMatricesCreator:

  def create_adjacency_matrices(self, simplicial_complex, incidence_matrix):
    adjacency_matrices = dict()

    for q in range(simplicial_complex.get_dimension() + 1):
      q_adj = self.create_empty_adjacency_matrix(incidence_matrix, q)
      i_adj = 0
      for i in range(len(incidence_matrix)):
        if incidence_matrix[i].count(1) - 1 >= q:
          q_adj[i_adj][i_adj] = 1
          j_adj = i_adj + 1
          for j in range(i + 1, len(incidence_matrix)):
            if incidence_matrix[j].count(1) - 1 >= q:
              if self.are_q_adjacent(incidence_matrix[i], incidence_matrix[j], q):
                q_adj[i_adj][j_adj] = 1
                q_adj[j_adj][i_adj] = 1
              j_adj += 1
          i_adj += 1
      adjacency_matrices[q] = q_adj
    return adjacency_matrices

  def create_empty_adjacency_matrix(self, incidence_matrix, q):
    size = 0
    for i in range(len(incidence_matrix)):
      if incidence_matrix[i].count(1) - 1 >= q:
        size += 1
    return np.zeros(shape=[size, size], dtype=np.int8).tolist()

  def are_q_adjacent(self, simplex_1, simplex_2, q):
    ones = 0
    for i in range(len(simplex_1)):
      if simplex_1[i] == 1 and simplex_1[i] == simplex_2[i]:
        ones += 1
    if ones - 1 == q:
      return True
    return False
