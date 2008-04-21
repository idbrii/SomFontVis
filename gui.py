#! /usr/bin/env python

import wx
from Generated import gui
import glue

#            wx.BeginBusyCursor()            
#            wx.EndBusyCursor()

class SomFontFrame(gui.FontFrame):
    def __init__(self, *args, **kwds):
        gui.FontFrame.__init__(self, *args, **kwds)
        self.selectedOutput = 0
        self.letterFilename = "data/TimesNewRoman_B.png"
        self._changeImage(self.letterFilename)
        self.som = glue.SelfOrgMapGlue(5)

        # fix output
        self._updateOutput()

    def _selectOutput(self, i):
        self.selectedOutput = i
        self.output.SetSelection(i)

    def _updateOutput(self):
        out = self.som.getCategory( self.letterFilename )
        self._selectOutput( out )

    def OnModifyOutput(self, event): # wxGlade: FontFrame.<event_handler>
        """ Override, but don't call super---it has garbage implementation
        Don't let the user modify the radio buttons. They are for output.
        """
        self._selectOutput(self.selectedOutput)
        event.Skip()


    def OnSelectImage(self, event): # wxGlade: FontFrame.<event_handler>
        """ Override, but don't call super---it has garbage implementation"""
        # don't care about event
        event.Skip()

        # get new filename
        self.letterFilename = self._openFile(self.letterFilename)

        self._changeImage(self.letterFilename)

        self._updateOutput()

    def OnTrain(self, event): # wxGlade: FontFrame.<event_handler>
        wx.BeginBusyCursor()            

        self.som.train( self.nEpochs.GetValue() )
        # fix output
        self._updateOutput()

        wx.EndBusyCursor()



    def _openFile(self, previousName):
        """Open an image file and return the filename"""
        
        #filters = 'Image files (*.gif;*.png;*.jpg)|*.gif;*.png;*.jpg'
        #fileDlg = wx.FileDialog(..., wildcard=filters, style=wx.OPEN)
        
        # create open dialog. use previous file as start location.
        fileDlg = wx.FileDialog(self, message="Select an Image...", defaultDir="", defaultFile=previousName, style=wx.OPEN)
        
        # grab our previous name in case we fail
        filename = previousName
        if fileDlg.ShowModal() == wx.ID_OK:
            filename = fileDlg.GetPath()
                        
        # clean up dialog
        fileDlg.Destroy()

        return filename


    def _changeImage(self, inFilename):
        """Change the current letter image"""
        self.letterImage.SetBitmap(wx.Bitmap(inFilename, wx.BITMAP_TYPE_ANY))



def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
