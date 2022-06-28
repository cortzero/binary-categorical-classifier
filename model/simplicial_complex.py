'''
Module that contains a class representation for a simplicial complex whose name is one category from the dataset

Classes
-------
SimplicialComplex
'''

class SimplicialComplex:

  '''
  Class representation of a simplicial complex
  '''

  '''
  __init__ method that builds a SimplicialComplex object

  Parameters
  ----------
  name : str
      One of the categories from the dataset.
  incidence_matrix : List
      A matrix representation of the simplicial complex.
  '''
  def __init__(self, name, incidence_matrix):
    self.__name = name
    self.__incidence_matrix = incidence_matrix
    self.__dimension = 0

  '''
  Calculates the dimension of the simplicial complex by counting the ones in each row and then, finding the maximun amount of
  ones among the rows.
  In this case, the input dataset is set in a way that each simplex has the same dimension, so the maximun is not necessary but
  this method is implemented for the general case.
  '''
  def calculate_dimension(self):
    d = []
    for s in self.__incidence_matrix:
      d.append(s.count(1))
    self.__dimension = max(d) - 1

  '''
  Returns the dimension of the simplicial complex, which is the dimension of the simplex with the most number of ones.

  Returns
  -------
  dimension : int
    The dimension of the simplicial complex
  '''
  def get_dimension(self):
    return self.__dimension

  def get_name(self):
    return self.__name

  def get_incidence_matrix(self):
    return self.__incidence_matrix