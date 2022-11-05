from flask import Flask, request
from flask_cors import CORS
from sklearn.metrics import confusion_matrix, classification_report, cohen_kappa_score
from classifier import Classifier
from dataframe_utils import get_categories
from response import Response
from response_json_encoder import ResponseEncoder
import json
import time


#Set up Flask
app = Flask(__name__)

#Set up Flask to bypass CORS
cors = CORS(app)

#Create the receiver API POST endpoint:
@app.route("/send", methods=["POST"])
def post_dataframe():
  dataframe = request.get_json()
  SPLITS = 4
  SHUFFLE = False
  i = 0

  y_real = []
  y_pred = []

  k_neighbors = 9
  classifier = Classifier(dataframe, k_neighbors)
  categories = get_categories(classifier.dataset.values.tolist())

  # ==================== START TIME ====================
  st = time.time()
  # ==================== START TIME ====================
  for X_train, X_test in classifier.execute_k_fold(SPLITS, SHUFFLE):
    y_train = [x[0] for x in X_train]
    y_test = [x[0] for x in X_test]
    X_train = [x[1:] for x in X_train]
    X_test = [x[1:] for x in X_test]

    y_real.extend(y_test)

    classifier.fit(X_train, y_train)
    print(f'Score: {classifier.get_score(X_test, y_test)}')
    for test_simplex in X_test:
      predicted_category = classifier.predict_simplex(test_simplex)
      y_pred.append(predicted_category)
      print('Simplex:', i)
    print('---------------------------------------------------\n\n')
    i += 1
  # ==================== END TIME ====================
  et = time.time()
  elapsed_time = et - st
  # ==================== END TIME ====================

  print('Elapsed time:', round(elapsed_time, 5), 'seconds')

  print(categories)
  response = Response()
  response.categories = categories
  response.confusion_matrix = confusion_matrix(y_real, y_pred, labels=categories).tolist()
  response.classification_report = classification_report(y_real, y_pred, output_dict=True)
  response.cohen_kappa = cohen_kappa_score(y_real, y_pred)
  return json.dumps(response, cls=ResponseEncoder)