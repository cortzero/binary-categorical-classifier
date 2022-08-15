'''
Module that represents the classifier and executes the k-fold and the q-analysis algorithm.

Classes
--------
Classifier
'''
from q_analysis.adjacency_matrices_creator import AdjacencyMatricesCreator
from q_analysis.distance_matrices_creator import DistanceMatricesCreator
from q_analysis.centrality_calculator import calculate_centrality
import pandas as pd
from sklearn.model_selection import KFold

class Classifier:

  def __init__(self, data):
    self.dataset = pd.DataFrame(data)

  def execute_k_fold(self, splits, has_to_shuffle):
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

    Parameters
    ----------
    simplicial_complex : SimplicialComplex
        A SimplicialComplex object representing the examples that belong to one category.
    test_simplex : Simplex
        A Simplex object that will be the simplex for which we are going to compute the centrality regarding the simplicial
        complex.
    '''

    adjacency_matrices_creator = AdjacencyMatricesCreator() # Adjacency matrices
    distance_matrices_creator = DistanceMatricesCreator() # Distance matrices
    k_complex = simplicial_complex.get_name() # Category of the simplicial complex

    incidence_matrix = simplicial_complex.get_incidence_matrix()
    incidence_matrix.append(test_simplex.attributes)
    simplicial_complex.calculate_dimension()
    adj_matrices_k = adjacency_matrices_creator.create_adjacency_matrices(simplicial_complex, incidence_matrix)
    dist_matrices_k = distance_matrices_creator.create_distance_matrices(adj_matrices_k)

    # Loop through distance matrices
    centrality = 0
    for distance_matrix in dist_matrices_k.values():
      test_simplex_distance_list = distance_matrix[-1] # Retrieve the test simplex which is the last one in the distance matrix
      centrality += calculate_centrality(test_simplex_distance_list) # accumulated sum for centrality for the whole complex
    
    # Round the centrality measure to two decimals
    centrality = round(centrality, 2)
    # Adds the pair simplicial complex name and centrality value
    test_simplex.add_centrality_measure(k_complex, centrality)
