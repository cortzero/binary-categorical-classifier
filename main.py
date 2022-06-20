from classifier_main_module import execute_k_fold

if __name__ == '__main__':
  
  DATASET_PATH = 'resources/lymphography_one_hot_encoded.xlsx'

  for train, test in execute_k_fold(DATASET_PATH, 4, True):
    print('Train set:\n', train)
    print()
    print('Testing set:\n', test)
    print('\n---------------------------------------------\n')
