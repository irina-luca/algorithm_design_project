### Code related to Hypersphere ###
class Hypersphere(object):
    def __init__(self, center, threshold):
        self.center = center
        self.threshold = threshold

    def __str__(self):
        return str(self.center) + ", " + str(self.threshold)

class HypersphereModel(object):
    def __init__(self, min, max, hyperspheres):
        self.min = min
        self.max = max
        self.hyperspheres = hyperspheres