#! /usr/bin/env python

from PIL import Image

def getCharList():
    return map(chr, range(ord('A'),ord('G'))) # characters [A-G) --> A..F
def getFontList():
    # add more fonts here
    return 'DejaVuSans','NimbusRoman','TimesNewRoman'

class Letter():
    """ Represents a letter of some font. You can get the width, height,
        and all of the pixel data """

    @classmethod
    def Create(cls, font, letter):
        filename = 'data/'+ font +'_'+ letter +'.png'
        return cls(filename)
    def __init__(self, filename):
        self.filename = filename
        self.im = Image.open( self.filename )

    def getName(self):
        return self.filename

    def getData(self):
        """ Get the data for this letter """
        return self.im.getdata()

    def getSize(self):
        """ Get the width of the data for this letter """
        return self.im.size

    def getWidth(self):
        """ Get the width of the data for this letter """
        return self.im.size[0]

    def getHeight(self):
        """ Get the height of the data for this letter """
        return self.im.size[1]

    def save(self):
        """ Save the image over the previous one """
        self.im.save(self.filename)

    def saveWeight(self, i, weightData):
        mode = 'L' # greyscale
        size = self.im.size
        weightFilename = 'weight/'+ str(i) +'.png'

        weight = Image.new( mode, size )
        weight.putdata(weightData)
        weight.save(weightFilename)


def createLetters():
    letters = []
    for fFace in getFontList():
        for character in getCharList(): # the font chars
            try:
                letters.append( Letter.Create(fFace, character) )
            except IOError:
                print "Cannot find font face:", fFace, "character:", character
    return letters


#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    # Simple tests
    images = {}
    for a in getCharList():
        images[a] = Letter.Create('TimesNewRoman', a)

    im = images['A']
    width = im.getWidth()

    letterData = ""
    count = 0
    for a in im.getData():
        if count == width:
            letterData += "\n"
            count = 0
        count += 0
        letterData += str(a)[0]

    print letterData
    print "Length:", len(im.getData())


def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
