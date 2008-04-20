#! /usr/bin/env python

import som

class SelfOrgMapGlue():
    def __init__(self, nOutputs):
        nInputs = self._getNInputs()
        self.som = som.SelfOrgMap(nInputs, nOutputs)

    def _getNInputs(self):
        return 500

    def getCategory(self, filename):
        letter = imagedata.Letter(filename)
        result = self.som.process( letter )

        return self.som._findSmallest(result)



def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
