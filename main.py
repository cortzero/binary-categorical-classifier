from classifier_main_module import Classifier
from simplicial_complex_creator import SimplicialComplexCreator
from simplex import Simplex
import pandas as pd
import numpy as np

if __name__ == '__main__':
  DATASET_PATH = 'resources/lymphography_one_hot_encoded.xlsx'
  dataset = pd.read_excel(DATASET_PATH)
  #print(dataset)
  classifier = Classifier(DATASET_PATH)
  splits = 4
  shuffle = False
  i = 0
  train_simplices, test_simplices = next(classifier.execute_k_fold(splits, shuffle))
  simplicial_complex_creator = SimplicialComplexCreator()
  simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train_simplices)

  # Simplex creation
  for s in test_simplices:
    category = s.pop(0)
    id = s.pop()
    attributes = s[:]
    simplex = Simplex(id, category, attributes)
    print()
    print('===============================================')
    print('Simplex:', simplex.id)
    for k in simplicial_complexes:
      classifier.execute_q_analysis(k, simplex)
    simplex.set_real_category()
    print()
    print('Expected category:', simplex.expected_category)
    print('Real category:', simplex.real_category)
    print('===============================================')
    print()
