'''
Module that represents the classifier and executes the k-fold and the q-analysis algorithm.
'''
from q_analysis.adjacency_matrices_creator import AdjacencyMatricesCreator
from q_analysis.distance_matrices_creator import DistanceMatricesCreator
from q_analysis.centrality_calculator import calculate_centrality
import pandas as pd
from sklearn.model_selection import KFold
import time


decimals = 5


class Classifier:

  def __init__(self, data):
    self.dataset = pd.DataFrame(data)

  def execute_k_fold(self, splits, has_to_shuffle):
    '''
    This function performs the k-fold technique for data analysis on the given categorical and binary dataset
    '''
    kfold = KFold(n_splits=splits, shuffle=has_to_shuffle)
    for train, test in kfold.split(self.dataset):
      train_matrix = []
      for x in train:
        train_matrix.append(self.dataset.iloc[x].tolist())
      test_matrix = []
      for x in test:
        simplex_list = self.dataset.iloc[x].tolist()
        simplex_list.append(x) # append example id from the dataset
        test_matrix.append(simplex_list)
      yield train_matrix, test_matrix

  def execute_q_analysis(self, simplicial_complex, test_simplex):
    '''
    Executes the q-analysis algorithm given the simplicial complex for one category and the simplex for which 
    the centrality will be computed.
    '''
    adjacency_matrices_creator = AdjacencyMatricesCreator() # Adjacency matrices
    distance_matrices_creator = DistanceMatricesCreator() # Distance matrices
    k_complex = simplicial_complex.get_name() # Category of the simplicial complex

    incidence_matrix = simplicial_complex.get_incidence_matrix()
    simplices_amount = len(incidence_matrix)

    incidence_matrix.append(test_simplex.attributes)
    simplicial_complex.calculate_dimension()

    adj_matrices_k = adjacency_matrices_creator.create_q_adjacency_matrices(simplicial_complex, incidence_matrix)
    distances = distance_matrices_creator.create_distance_matrices(adj_matrices_k, len(incidence_matrix) - 1)

    # Loop through distance matrices
    centrality = 0
    for q_distance in distances.values():
      #test_simplex_distance_list = distance_matrix_q[-1] # Retrieve the test simplex which is the last one in the distance matrix
      normalized_centrality = calculate_centrality(q_distance.values()) / simplices_amount
      centrality += normalized_centrality

    print()

    # Round the centrality measure to two decimals
    # centrality = round(centrality, 2)
    # Adds the pair simplicial complex name and centrality value
    test_simplex.add_centrality_measure(k_complex, centrality)
