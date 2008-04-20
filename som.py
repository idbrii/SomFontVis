#! /usr/bin/env python
import random

class Weight():
    def __init__(self, dim):
        self.dim = dim
        self.data = [0] * self.dim
    def __str__(self):
        return str(self.data)

    def randomize(self):
        for w in range(len(self.data)):
            self.data[w] = random.randint(0,10)

    def calcDistance(self, data):
        assert len(self.data) == len(data), "Inputs should have same size as weights (%i,%i)" % (len(self.data), len(data))

        print "Data:",len(self.data), len(data)
        distance = 0
        for w,i in self.data,data:
            print distance
            distance += _calcDistance(w,i)
        return distance

class SelfOrgMap():
    def __init__(self, nInputs, nOutputs):
        """
        nInputs -> number of inputs to the map
        nOutputs -> number of categories/clusters

        >>> s = SelfOrgMap(10, 5)
        >>> print s.inputs
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> [len(a.data) for a in s.weights]
        [10, 10, 10, 10, 10]
        """
        self.inputs = [0]*nInputs
        self.weights = [Weight(nInputs) for a in range(nOutputs)]
        self._randomize()

    def _randomize(self):
        random.seed()
        for w in self.weights:
            w.randomize()

    def process(self, letter):
        """
        >>> import imagedata
        >>> letter = imagedata.Letter('TimesNewRoman', 'B')
        >>> s = SelfOrgMap( letter.getWidth()*letter.getHeight(), 5)
        >>> s.process( letter )
        """
        data = list(letter.getData())
        result = [w.calcDistance(data) for w in self.weights]
        print result
        result = min(result)
        print result



def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
