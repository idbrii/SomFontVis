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

        #print "Data:",len(self.data), len(data)
        distance = 0
        for w,i in map(None,self.data,data):
            distance += self._calcDistance(w,i)
        return distance

    def _calcDistance(self, weight, input):
        """
        Euclidean distance
        >>> w = Weight(5)
        >>> w._calcDistance(10,10)
        0
        >>> w._calcDistance(10,5)
        25
        >>> w._calcDistance(2,10)
        64
        """
        return pow(weight-input, 2)

    def makeCloser(self, alpha, data):
        """ Make the weight closer in value to the input, according to the alpha
        """
        assert len(self.data) == len(data), "Inputs should have same size as weights (%i,%i)" % (len(self.data), len(data))

        # iterate over list
        for i in range(self.data):
            # Find the difference from what we wanted, scale by alpha,
            # and apply to weight
            self.data[i] += alpha*(data[i] - self.data[i])

class SelfOrgMap():
    def __init__(self, nInputs, nOutputs):
        """
        nInputs -> number of inputs to the map
        nOutputs -> number of categories/clusters

        >>> s = SelfOrgMap(10, 5)
        >>> [len(a.data) for a in s.weights]
        [10, 10, 10, 10, 10]
        """
        # create nOutputs weights
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
        >>> r = s.process( letter )
        >>> # TODO: do something with r
        """
        # convert to list
        data = list(letter.getData())
        # create list of total distance for each weight
        return [w.calcDistance(data) for w in self.weights]

    def train(self, nEpochs):
        """
        Train the SOM for nEpochs.
        Learning rate decays with time: a(0) = 0.8, a(t) = 0.7*a(t-1)
        Only modify one cluster (no neighbourhood).
        """

        alpha = 0.8
        letters = imagedata.createLetters()
        for t in range(nEpochs):
            for letter in letters:
                self._trainOnLetter(letter, alpha)
            alpha *= 0.7    # scale alpha
            if alpha == 0.0:
                print "Warning: Requested more epochs, but learning parameter is now zero. (t=%i)"%t

    def _trainOnLetter(self, letter, alpha):
        # get result
        result = self.process(letter)
        smallest = self._findSmallest(result)

        # modify smallest weight
        data = list(letter.getData())
        self.weights[smallest].makeCloser(alpha, data)

    def _findSmallest(self, result):
        """ self._findSmallest( list ) -> int
        Finds the smallest element in `result` and returns its index

        >>> s = SelfOrgMap(0,0)
        >>> s._findSmallest([6, 3, 9, 2])
        3
        """
        # map result into list of result,index pairs
        result = map(None, result, range(len(result)))
        # find smallest result
        result = min(result)

        # return index from pair
        return result[1]


def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
