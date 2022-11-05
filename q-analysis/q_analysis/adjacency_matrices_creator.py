'''
This module provides a class that will help to create the adjacency matrices for each dimension of a simplicial complex.
'''

import numpy as np

class AdjacencyMatricesCreator:

  def create_adj_matrix(self, incidence_matrix):
    np_df = np.array(incidence_matrix, dtype=np.int8)
    np_adj = np_df @ np_df.T
    return np_adj

  def create_q_adjacency_matrices(self, dim, incidence_matrix):
    adj = self.create_adj_matrix(incidence_matrix)
    adj_matrices = dict()
    for q in range(dim + 1):
      q_adj_matrix = np.where(adj == q + 1, 1, 0)
      np.fill_diagonal(q_adj_matrix, 1)
      adj_matrices[q] = q_adj_matrix.tolist()
    return adj_matrices
