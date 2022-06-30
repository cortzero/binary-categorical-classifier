from classifier import Classifier
from q_analysis.simplicial_complex_creator import SimplicialComplexCreator
from model.simplex import Simplex
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

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

  SPLITS = 2
  SHUFFLE = False
  
  for train_simplices, test_simplices in classifier.execute_k_fold(SPLITS, SHUFFLE):
    simplicial_complex_creator = SimplicialComplexCreator()
    simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train_simplices)

    # Iteration through all test simplices
    for s in test_simplices:
      category = s.pop(0) # The expected category of the simplex
      id = s.pop() # The id of the simplex in the dataframe
      attributes = s[:] # The list of one's and zero's of the simplex in the dataframe

      simplex = Simplex(id, category, attributes) # Simplex creation

      # Iteration through all the simplicial complexes in the train set
      for k in simplicial_complexes:
        classifier.execute_q_analysis(k, simplex)

      simplex.set_real_category()
      simplex_json = json.dumps(simplex, default=simplex.serialize)
      simplices_classification.append(simplex_json)

  response = jsonify(simplices_classification)
  return response

if __name__ == '__main__':
  app.run(debug=True)
