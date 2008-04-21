#! /usr/bin/env python
import random

def ScaledGen(alpha, scale):
    """
    An example generator for alpha.

    >>> sGen = ScaledGen(1.0, 0.5)
    >>> sGen.next()
    1.0
    >>> sGen.next()
    0.5
    >>> sGen.next()
    0.25
    """
    while True:
        yield alpha
        alpha *= scale

class Weight():
    def __init__(self, dim):
        self.dim = dim
        self.data = [0] * self.dim
    def __str__(self):
        return str(self.data[:8])

    def randomize(self):
        MAX = 255
        i = random.randint(0,MAX)
        for w in range(len(self.data)):
            self.data[w] = i
            i += 1
            i %= MAX

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

    def _makeCloser(self, alpha, data):
        """ Make the weight closer in value to the input, according to the alpha
        """
        assert len(self.data) == len(data), "Inputs should have same size as weights (%i,%i)" % (len(self.data), len(data))

        # iterate over list
        for i in range(len(self.data)):
            # Find the difference from what we wanted, scale by alpha,
            # and apply to weight
            self.data[i] += alpha*(data[i] - self.data[i])

class SelfOrgMap():
    def __init__(self, nInputs, nOutputs, alphaGen=ScaledGen(1.0,0.5)):
        """
        nInputs -> number of inputs to the map
        nOutputs -> number of categories/clusters

        >>> s = SelfOrgMap(10, 5, ScaledGen(0.5,0.5))
        >>> [len(a.data) for a in s.weights]
        [10, 10, 10, 10, 10, 10]
        """
        # create nOutputs weights
        self.weights = [Weight(nInputs) for a in range(nOutputs+1)]
        self._initializeWeights()
        self.setAlphaGenerator(alphaGen)

    def __str__(self):
        s = ''
        for w in self.weights:
            s += str(w) + "\n"
        return s

    def _initializeWeights(self):
        random.seed(1) # use constant seed for repeatable results
        for w in self.weights:
            w.randomize()

    def setAlphaGenerator(self, alphaGen):
        self.alphaGen = alphaGen

    def process(self, letter):
        """ self.process( Letter ) -> list
        Using the input letter, determine the outputs of the SOM.
        len(output) == nOutputs == len(self.weights)

        >>> import imagedata
        >>> letter = imagedata.Letter.Create('TimesNewRoman', 'B')
        >>> s = SelfOrgMap( letter.getWidth()*letter.getHeight(), 5, ScaledGen(0.5,0.5))
        >>> r = s.process( letter )
        >>> # TODO: do something with r
        """
        # convert to list
        data = list(letter.getData())
        # create list of total distance for each weight
        return [w.calcDistance(data) for w in self.weights]

    def train(self, letters, nEpochs):
        """
        Train the SOM for nEpochs.
        Learning rate decays with time: a(0) = 0.8, a(t) = 0.7*a(t-1)
        Only modify one cluster (no neighbourhood).
        """
        for t in range(nEpochs):
            self._trainSingleEpoch(letters, self.alphaGen.next())

    def _trainSingleEpoch(self, letters, alpha):
        if alpha == 0.0:
            print "Warning: Requested more epochs, but learning parameter is now zero. (t=%i)"%t

        self.clustersUsed = {}
        random.shuffle(letters) #in-place shuffle -> epoch's different from last
        for letter in letters:
            self._trainOnLetter(letter, alpha)
        print '=== Used (key,cluster):'\
            ,[(k,self.clustersUsed[k]) for k in self.clustersUsed.keys()]\
            ,'==='

    def _scaleAlpha(self, alpha):
        alpha *= 0.7    # scale alpha
        return alpha

    # DEBUG: testing cheat to force good training
    counter = -1    # initialize self.counter
    def _getCheatSmallest(self):
        self.counter += 1
        self.counter %= len(self.weights)
        return self.counter
    # END DEBUG

    def _trainOnLetter(self, letter, alpha):
        """
        Train for the given letter.
        Determine the closest weight to the input `letter` and make that weight
        closer to the input using the given `alpha`.
        """
        # get result
        result = self.process(letter)
        smallest = self._findSmallest(result)
        try:
            self.clustersUsed[smallest] += 1
        except:
            self.clustersUsed[smallest] = 1

        # DEBUG: testing cheat to force good training
        #smallest = self._getCheatSmallest()
        #print 'letter %s had smallest: %i' %(letter.getName(),smallest)

        # modify smallest weight
        data = list(letter.getData())
        self.weights[smallest]._makeCloser(alpha, data)

    def _findSmallest(self, result):
        """ self._findSmallest( list ) -> int
        Finds the smallest element in `result` and returns its index

        >>> s = SelfOrgMap(0,0, ScaledGen(0.5,0.5))
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
