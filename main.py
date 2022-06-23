from classifier_main_module import execute_k_fold
from simplicial_complex_creator import SimplicialComplexCreator
from adjacency_matrices_creator import AdjacencyMatricesCreator
from distance_matrices_creator import DistanceMatricesCreator
import pandas as pd
import numpy as np

if __name__ == '__main__':
  DATASET_PATH = 'resources/lymphography_one_hot_encoded.xlsx'
  dataset = pd.read_excel(DATASET_PATH)
  print(dataset)
  splits = 4
  shuffle = False
  i = 0
  train, test = next(execute_k_fold(DATASET_PATH, splits, shuffle))
  simplicial_complex_creator = SimplicialComplexCreator()
  simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train)
  adjacency_matrices_creator = AdjacencyMatricesCreator()
  distance_matrices_creator = DistanceMatricesCreator()
  print('=======================================')
  for k in simplicial_complexes:
    print('Complex:', k.get_name())
    adj_matrices_k = adjacency_matrices_creator.create_adjacency_matrices(k, k.get_incidence_matrix())
    dist_matrices_k = distance_matrices_creator.create_distance_matrices(adj_matrices_k)
    for q, adj_matrix in adj_matrices_k.items():
      print('q-adjacency:', q)
      print(np.array(adj_matrix))
      print('q-distance:', q)
      print(np.array(dist_matrices_k[q]))
      print('-----------------')
