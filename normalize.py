#! /usr/bin/env python

""" Normalize the colour and size of the images.
    We need them all to be the same size and to be in shades of grey.
"""

import sys
from PIL import Image
from imagedata import *

def usage():
    print "Usage:\n\t", sys.argv[0], "font-name [font-name [...]]"
    print "For example:\t", sys.argv[0], "TimesNewRoman Arial LucidaConsole"
    exit()

letters_list = map( chr, range(ord('A'),ord('G')) ) # characters [A-G) --> A..F
# Grab fonts from command line
try:
    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        usage()

    font_list = sys.argv[1:]
except:
    print "Error:\n\t","You need to provide the names of fonts as an argument."
    usage()


def inflate(box1, box2):
    """ Return a box that contains both box1 and box2 """
    box = []
    for i in range(0,2):
        box.append( min(box1[i], box2[i]) )
    for i in range(2,4):
        box.append( max(box1[i], box2[i]) )
    return box


# Get all of the letters
letters = []
for f in font_list:
    fonts = {}
    for a in letters_list:
        fonts[a] = Letter.Create(f, a)
        letters.append( fonts[a] )

# Determine the maximum size image
maxBox = [0,0,0,0]
for let in letters:
    im = let.im     # grab the image
    maxBox = inflate(im.getbbox(), maxBox)

# Perform the resizing and greyscaling
print 'Before'
for let in letters:
    print let.filename,let.im.getbbox()

for let in letters:
    let.im = let.im.resize( maxBox[2:4], Image.ANTIALIAS )
    let.im = let.im.convert("L")
    let.save()

print '\nAfter'
for let in letters:
    print let.filename,let.im.getbbox()

