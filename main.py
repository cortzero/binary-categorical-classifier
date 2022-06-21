from classifier_main_module import execute_k_fold
from simplicial_complex_creator import SimplicialComplexCreator
import pandas as pd

if __name__ == '__main__':
  
  DATASET_PATH = 'resources/lymphography_one_hot_encoded.xlsx'

  dataset = pd.read_excel(DATASET_PATH)

  print(dataset)

  for train, test in execute_k_fold(DATASET_PATH, 4, True):
    simplicial_complex_creator = SimplicialComplexCreator()
    simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train)
    print('--------------------------------')
    print('Number of simplicial complexes:', len(simplicial_complexes))
    print('--------------------------------')
    for s in simplicial_complexes:
      print('-Category:', s.get_name())
      print('-Dimension:', s.get_dimension())
      print('-Incidence matrix:\n', s.get_incidence_matrix())
      print()
