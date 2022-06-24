class Simplex:
  def __init__(self, id, expected_category, attributes = []):
    self.id = id
    self.attributes = attributes
    self.centrality_measures = []
    self.expected_category = expected_category
    self.real_category = ''

  def add_centrality_measure(self, complex_name, centrality):
    self.centrality_measures.append((complex_name, centrality))

  def set_real_category(self):
    max_centrality = max(self.centrality_measures, key=get_centrality_from_tuple)
    self.real_category = max_centrality[0]

def get_centrality_from_tuple(measure):
  return measure[1]
