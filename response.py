class Response:
  def __init__(self):
    self.categories = []
    self.confusion_matrix = []
    self.classification_report = {}
    self.cohen_kappa = 0