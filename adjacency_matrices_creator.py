'''

'''

import numpy as np

class AdjacencyMatricesCreator:

  def create_adjacency_matrices(self, simplicial_complex, incidence_matrix):
    q = 0
    adjacency_matrices = dict()
    while q <= simplicial_complex.get_dimension():
      q_adj = self.create_empty_adjacency_matrix(incidence_matrix, q)
      i = 0
      i_prime = 0
      while i <= len(incidence_matrix) - 1:
        if incidence_matrix[i].count(1) - 1 >= q:
          j = i + 1
          q_adj[i_prime][i_prime] = 1
          j_prime = i_prime + 1
          while j < len(incidence_matrix):
            if incidence_matrix[j].count(1) - 1 >= q:
              if self.are_q_adjacent(incidence_matrix[i], incidence_matrix[j], q):
                q_adj[i_prime][j_prime] = 1
                q_adj[j_prime][i_prime] = 1
              j_prime += 1
            j += 1
          i_prime += 1
        i += 1
      adjacency_matrices[q] = q_adj
      q += 1
    return adjacency_matrices

  def create_empty_adjacency_matrix(self, incidence_matrix, q):
    size = 0
    i = 0
    while i < len(incidence_matrix):
      if incidence_matrix[i].count(1) - 1 >= q:
        size += 1
      i += 1
    return np.zeros(shape=[size, size], dtype=np.int8).tolist()

  def are_q_adjacent(self, simplex_1, simplex_2, q):
    if simplex_1.count(1) >= q and simplex_2.count(1) >= q:
      ones = 0
      i = 0
      while i < len(simplex_1):
        if simplex_1[i] == simplex_2[i] and simplex_1[i] == 1:
          ones += 1
        i += 1
      if ones - 1 == q:
        return True
    return False
