from classifier import Classifier
from q_analysis.simplicial_complex_creator import SimplicialComplexCreator
from model.simplex import Simplex


if __name__ == '__main__':

  DATASE_NAME = 'car_evaluation_one_hot_encoded'
  DATASET_PATH = 'resources/{}.xlsx'.format(DATASE_NAME)
  OUTPUT_FILE = 'output/output_{}.txt'.format(DATASE_NAME)

  classifier = Classifier(DATASET_PATH)

  SPLITS = 4
  SHUFFLE = False
  
  train_simplices, test_simplices = next(classifier.execute_k_fold(SPLITS, SHUFFLE))
  simplicial_complex_creator = SimplicialComplexCreator()
  simplicial_complexes = simplicial_complex_creator.create_simplicial_complex(train_simplices)

  # Iteration through all test simplices
  for s in test_simplices:

    category = s.pop(0) # The expected category of the simplex
    id = s.pop() # The id of the simplex in the dataframe
    attributes = s[:] # The list of one's and zero's of the simplex in the dataframe

    simplex = Simplex(id, category, attributes) # Simplex creation
    print()
    print('===============================================')
    print('Simplex:', simplex.id)

    # Iteration through all the simplicial complexes in the train set
    for k in simplicial_complexes:
      classifier.execute_q_analysis(k, simplex)

    simplex.set_real_category()

    # Write the output into the txt file
    with open(OUTPUT_FILE, 'a') as f:
      f.write('===============================================\n')
      f.write('Simplex: {} \n'.format(simplex.id))
      f.write('Expected category: {} \n'.format(simplex.expected_category))
      f.write('Real category: {}\n'.format(simplex.real_category))
      f.write('===============================================')
      f.write('\n\n')
    
    print()
    print('Expected category:', simplex.expected_category)
    print('Real category:', simplex.real_category)
    print('===============================================')
    print()
