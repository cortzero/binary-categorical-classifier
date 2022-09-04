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



    # ==================== START TIME INCIDENCE MATRIX ====================
    st_incidence = time.time()
    # ==================== START TIME INCIDENCE MATRIX ====================

    incidence_matrix = simplicial_complex.get_incidence_matrix()
    simplices_amount = len(incidence_matrix)

    # ==================== END TIME INCIDENCE MATRIX ====================
    et_incidence = time.time()
    elapse_time_incidence = et_incidence - st_incidence
    print('Incidence matrix creation time:', round(elapse_time_incidence, decimals), 'seconds')
    # ==================== END TIME INCIDENCE MATRIX ====================



    incidence_matrix.append(test_simplex.attributes)
    simplicial_complex.calculate_dimension()



    # ==================== START TIME ADJACENCY MATRIX ====================
    st_adjacency = time.time()
    # ==================== START TIME ADJACENCY MATRIX ====================

    adj_matrices_k = adjacency_matrices_creator.create_q_adjacency_matrices(simplicial_complex.get_dimension(), incidence_matrix)

    # ==================== END TIME ADJACENCY MATRIX ====================
    et_adjacency = time.time()
    elapse_time_adjacency = et_adjacency - st_adjacency
    print('Adjacency matrix creation time:', round(elapse_time_adjacency, decimals), ' seconds')
    # ==================== END TIME ADJACENCY MATRIX ====================



    # ==================== START TIME DISTANCE MATRIX ====================
    st_distance = time.time()
    # ==================== START TIME DISTANCE MATRIX ====================

    dist_matrices_k = distance_matrices_creator.create_distance_matrices(adj_matrices_k)

    # ==================== END TIME DISTANCE MATRIX ====================
    et_distance = time.time()
    elapse_time_distance = et_distance - st_distance
    print('Distance matrix creation time:', round(elapse_time_distance, decimals), ' seconds')
    # ==================== END TIME DISTANCE MATRIX ====================



    # ==================== START TIME CENTRALITY CALCULATION ====================
    st_centrality = time.time()
    # ==================== START TIME CENTRALITY CALCULATION ====================

    # Loop through distance matrices
    centrality = 0
    for distance_matrix_q in dist_matrices_k.values():
      test_simplex_distance_list = distance_matrix_q[-1] # Retrieve the test simplex which is the last one in the distance matrix
      normalized_centrality = calculate_centrality(test_simplex_distance_list) / simplices_amount
      centrality += normalized_centrality
    
    # ==================== END TIME CENTRALITY CALCULATION ====================
    et_centrality = time.time()
    elapse_time_centrality = et_centrality - st_centrality
    print('Centrality calculation time:', round(elapse_time_centrality, decimals), ' seconds')
    # ==================== END TIME CENTRALITY CALCULATION ====================


    print()


    # Round the centrality measure to two decimals
    #centrality = round(centrality, 2)
    # Adds the pair simplicial complex name and centrality value
    test_simplex.add_centrality_measure(k_complex, centrality)
