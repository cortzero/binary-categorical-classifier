from classifier import Classifier
from q_analysis.simplicial_complex_creator import SimplicialComplexCreator
from model.dataframe_tools import get_categories
from model.simplex import Simplex
from model.response import Response
from model.response_json_encoder import ResponseEncoder
from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.metrics import confusion_matrix, classification_report, cohen_kappa_score
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

  classifier = Classifier(dataframe)
  simplices_classification = []

  SPLITS = 4
  SHUFFLE = False

  i = 0

  y_real = []
  y_pred = []
  categories = get_categories(classifier.dataset.values.tolist())
  
  # ==================== START TIME ====================
  st = time.time()
  # ==================== START TIME ====================

  for train_simplices, test_simplices in classifier.execute_k_fold(SPLITS, SHUFFLE):
    simplicial_complex_creator = SimplicialComplexCreator()
    simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train_simplices)

    print('Iteration', i, '\n')

    # Iteration through all test simplices
    for s in test_simplices:
      category = s.pop(0) # The expected category of the simplex
      id = s.pop() # The id of the simplex in the dataframe
      attributes = s[:] # The list of one's and zero's of the simplex in the dataframe

      simplex = Simplex(id, category, attributes) # Simplex creation

      # Iteration through all the simplicial complexes in the train set
      for k in simplicial_complexes:
        classifier.execute_q_analysis(k, simplex)
      simplex.set_predicted_category()
      y_real.append(simplex.real_category)
      y_pred.append(simplex.predicted_category)
      simplex_json = json.dumps(simplex, default=simplex.serialize)
      simplices_classification.append(simplex_json)
      
      print('Simplex:', id)
      print('Real category:', simplex.real_category)
      print('Predicted category:', simplex.predicted_category, '\n')
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

if __name__ == '__main__':
  app.run(debug=True)
