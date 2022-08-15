import numpy as np

class Simplex:
  def __init__(self, id, real_category, attributes = []):
    self.id = id
    self.attributes = attributes
    self.centrality_measures = []
    self.real_category = real_category
    self.predicted_category = ''

  def add_centrality_measure(self, complex_name, centrality):
    self.centrality_measures.append((complex_name, centrality))

  def set_predicted_category(self):
    max_centrality = max(self.centrality_measures, key=get_centrality_from_tuple)
    self.predicted_category = max_centrality[0]

  def serialize(self, obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, np.int64):
      serial = obj.tolist()
      return serial

    return obj.__dict__

def get_centrality_from_tuple(measure):
  return measure[1]
