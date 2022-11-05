import pandas as pd
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from scipy.spatial.distance import hamming


class Classifier:

  def __init__(self, data, k_neighbours):
    self.dataset = pd.DataFrame(data)
    self.knn = KNeighborsClassifier(n_neighbors=k_neighbours, metric=hamming)

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
        test_matrix.append(simplex_list)
      yield train_matrix, test_matrix

  def predict_simplex(self, test_simplex):
    test_simplex_2d = [test_simplex]
    return self.knn.predict(test_simplex_2d)

  def fit(self, X_train, y_train):
    self.knn.fit(X_train, y_train)

  def get_score(self, X_test, y_test):
    return self.knn.score(X_test, y_test)