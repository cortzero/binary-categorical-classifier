import math
import copy

class DistanceMatricesCreator:

  def create_distance_matrices(self, adj_matrices):
    dist_matrices = dict()
    for q, adj_matrix in adj_matrices.items():
      q_dist_matrix = self.Floyd_Warshall(adj_matrix)
      dist_matrices[q] = q_dist_matrix
    return dist_matrices

  def set_up_initial_matrix(self, adj_matrix):
    dist_matrix = copy.deepcopy(adj_matrix)
    INF = math.inf
    for i in range(len(dist_matrix)):
      for j in range(len(dist_matrix)):
        if i != j:
          if adj_matrix[i][j] == 0:
            dist_matrix[i][j] = INF
        else:
          dist_matrix[i][j] = 0
    return dist_matrix

  def Floyd_Warshall(self, adj_matrix):
    dist_matrix = self.set_up_initial_matrix(adj_matrix)
    for k in range(len(adj_matrix)):
      for i in range(len(adj_matrix)):
        if i != k:
          for j in range(i, len(adj_matrix)):
            if j != k:
              if dist_matrix[i][j] > (dist_matrix[i][k] + dist_matrix[k][j]):
                dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                dist_matrix[j][i] = dist_matrix[i][k] + dist_matrix[k][j]
    return dist_matrix