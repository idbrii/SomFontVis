#! /usr/bin/env python

import som

class SelfOrgMapGlue():
    def __init__(self, nOutputs):
        nInputs = _getNInputs()
        self.som = som.SelfOrgMap(nInputs, nOutputs)

    def _getNInputs(self):
        return 500

    def getCategory(self, filename):
        letter = imagedata.Letter(filename)
        result = self.som.process( letter )

        return _findSmallest(result)

    def _findSmallest(self, result):
        """ self._findSmallest( list ) -> int
            finds the smallest element in `result` and returns its index
        """
        # map result into list of result,index pairs
        result = map(None, result, range(len(result)))
        # find smallest result
        result = min(result)

        # return index from pair
        return result[1]
