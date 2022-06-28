'''
This module implements a class that will be responsible for creating each simplicial complex given a training set of binary data.

Classes
-------
SimplicialComplexCreator
'''

from model.simplicial_complex import SimplicialComplex

class SimplicialComplexCreator:

  '''
  The class that will create the simplicial complexes for each category in the dataset.
  '''

  '''
  This method creates a SimplicialComplex object for each category in the training matrix.

  Parameters
  ----------
  training_matrix : List
      The set of simplices used for training.

  Return
  ------
  simplicial_complexes : List
      A list that contains all the simplicial complexes created per category.
  '''
  def create_simplicial_complex(self, training_matrix=[]):
    simplicial_complexes = []
    categories = self.get_categories(training_matrix)
    for category in categories:
      k = [] # Incidence matrix
      i = 0
      while i < len(training_matrix):
        if training_matrix[i][0] == category:
          k.append(training_matrix[i][1:])
        i += 1
      complex_k = SimplicialComplex(category, k)
      complex_k.calculate_dimension()
      simplicial_complexes.append(complex_k)
    return simplicial_complexes

  '''
  Creates a list with all the categories in the training matrix.

  Parameters
  ----------
  training_matrix : List
      The set of simplices used for training.

  Return
  ------
  category_list : List
      A list that contains the categories from the dataset.
  '''
  def get_categories(self, training_matrix=[]):
    categories_list = []
    i = 0
    while i < len(training_matrix):
      if len(categories_list) == 0:
        categories_list.append(training_matrix[i][0])
      elif training_matrix[i][0] not in categories_list:
        categories_list.append(training_matrix[i][0])
      i += 1
    return categories_list