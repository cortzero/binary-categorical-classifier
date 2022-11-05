import math

def calculate_centrality(test_simplex_distance_list):
  centrality = 0
  
  # Accumulated sum for each q dimension
  for distance in test_simplex_distance_list:
    if distance == math.inf or distance == 0:
      centrality += 0
    else:
      centrality += 1 / distance
  return centrality