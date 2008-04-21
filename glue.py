#! /usr/bin/env python

import som
import imagedata

class SelfOrgMapGlue():
    def __init__(self, nOutputs):
        self.letters = imagedata.createLetters()
        nInputs = self._getNInputs(self.letters[0])
        self.som = som.SelfOrgMap(nInputs, nOutputs)

    def _getNInputs(self, letter):
        return letter.getWidth()*letter.getHeight()

    def getCategory(self, filename):
        letter = imagedata.Letter(filename)
        result = self.som.process( letter )

        return self.som._findSmallest(result)

    def train(self, nEpochs):
        self.som.train(self.letters, nEpochs)


def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
