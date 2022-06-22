from classifier_main_module import execute_k_fold
from simplicial_complex_creator import SimplicialComplexCreator
from adjacency_matrices_creator import AdjacencyMatricesCreator
import pandas as pd
import numpy as np

if __name__ == '__main__':
  DATASET_PATH = 'resources/lymphography_one_hot_encoded.xlsx'
  dataset = pd.read_excel(DATASET_PATH)
  print(dataset)
  splits = 4
  shuffle = False
  i = 0
  for train, test in execute_k_fold(DATASET_PATH, splits, shuffle):
    simplicial_complex_creator = SimplicialComplexCreator()
    simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train)
    adjacency_matrices_creator = AdjacencyMatricesCreator()
    print('=======================================')
    for k in simplicial_complexes:
      print('Complex:', k.get_name())
      adj_matrices_k = adjacency_matrices_creator.create_adjacency_matrices(k, k.get_incidence_matrix())
      for key, value in adj_matrices_k.items():
        print('q-adjacency:', key)
        print(np.array(value))
        print('-----------------')

