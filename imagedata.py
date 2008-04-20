#! /usr/bin/env python

from PIL import Image

class Letter():
    """ Represents a letter of some font. You can get the width, height,
        and all of the pixel data """
    def __init__(self, filename):
        self.filename = filename
        self.im = Image.open( self.filename )
    """ Represents a letter of some font. You can get the width, height,
        and all of the pixel data """
    def __init__(self, font, letter):
        self.filename = 'data/'+ font +'_'+ letter +'.png'
        self.im = Image.open( self.filename )

    def getData(self):
        """ Get the data for this letter """
        return self.im.getdata()

    def getWidth(self):
        """ Get the width of the data for this letter """
        return self.im.size[0]

    def getHeight(self):
        """ Get the height of the data for this letter """
        return self.im.size[1]

    def save(self):
        """ Save the image over the previous one """
        self.im.save(self.filename)


#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    images = {}
    for a in map( chr, range(ord('A'),ord('F')) ):
        images[a] = Letter('TimesNewRoman', a)

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
