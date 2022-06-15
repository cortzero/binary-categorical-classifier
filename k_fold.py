'''
Module that exports a function that performs the k-fold algorithm to split the dataset in trian and test subsets.

Functions
--------
execute_k_fold : Generator
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold

def execute_k_fold(dataset_path, splits, has_to_shuffle):
  '''
  This function performs the k-fold technique for data analysis on the given categorical and binary dataset

  Parameters
  ----------
  dataset_path : str
      The path for the dataset
  splits : int
      The number of subsets into which the dataset will be divided
  has_to_shuffle : bool
      Tells whether the k-fold algorithm has to shuffle after every iteration or not

  Yields:
  -------
  train_matrix : list
      A list containing the simplices used to form the simplicial complexes for
      every category for one iteration
  test_matrix : list
      A list containing the simplices used to test q-analysis algorithm
  '''
  dataset = pd.read_excel(dataset_path)
  kfold = KFold(n_splits=splits, shuffle=has_to_shuffle, random_state=1)
  for train, test in kfold.split(dataset):
    train_matrix = []
    for x in train:
      train_matrix.append(dataset.iloc[x].tolist())
    test_matrix = []
    for x in test:
      test_matrix.append(dataset.iloc[x].tolist())
    yield train_matrix, test_matrix
