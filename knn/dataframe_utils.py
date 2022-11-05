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
def get_categories(training_matrix=[]):
  categories_list = []
  i = 0
  while i < len(training_matrix):
    if len(categories_list) == 0:
      categories_list.append(training_matrix[i][0])
    elif training_matrix[i][0] not in categories_list:
      categories_list.append(training_matrix[i][0])
    i += 1
  return categories_list