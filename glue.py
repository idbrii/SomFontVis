#! /usr/bin/env python

import som
import imagedata

class SelfOrgMapGlue():
    def __init__(self, nOutputs, alpha, scale):
        self.letters = imagedata.createLetters()
        nInputs = self._getNInputs(self.letters[0])
        self.alpha = alpha
        self.scale = scale
        self.som = som.SelfOrgMap(nInputs, nOutputs)
        self._updateAlphaGenerator()

    def _getNInputs(self, letter):
        return letter.getWidth()*letter.getHeight()

    def getCategory(self, filename):
        letter = imagedata.Letter(filename)
        result = self.som.process( letter )

        return self.som._findSmallest(result)

    def train(self, nEpochs):
        self.som.train(self.letters, nEpochs)

    def setInitialAlpha(self, alpha):
        self.alpha = alpha
        self._updateAlphaGenerator()

    def setScale(self, scale):
        self.scale = scale
        self._updateAlphaGenerator()

    def _updateAlphaGenerator(self):
        self.som.setAlphaGenerator( som.ScaledGen(self.alpha, self.scale) )


def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
