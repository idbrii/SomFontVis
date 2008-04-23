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
        self.som = glue.SelfOrgMapGlue(5, 1.0, 0.5)

        # fix output
        self._OnChangeSomState()

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

        # grab newest values for alpha functions
        alpha = float(self.tCtrl_alpha.GetValue())
        scale = float(self.tCtrl_scale.GetValue())
        self.som.updateAlphaGenerator(alpha, scale)

        # do the training
        self.som.train( self.nEpochs.GetValue() )

        # recalculate output
        self._OnChangeSomState()

        wx.EndBusyCursor()

    def OnReset(self, event): # wxGlade: FontFrame.<event_handler>
        self.som.initializeSom()
        self._OnChangeSomState()

    def _OnChangeSomState(self):
        self._updateOutput()
        self._updateWeightImages()

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

    def _updateWeightImages(self):
        self.som.updateWeightImages()
        self.weightImage_0.SetBitmap(wx.Bitmap("weight/0.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_1.SetBitmap(wx.Bitmap("weight/1.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_2.SetBitmap(wx.Bitmap("weight/2.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_3.SetBitmap(wx.Bitmap("weight/3.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_4.SetBitmap(wx.Bitmap("weight/4.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_5.SetBitmap(wx.Bitmap("weight/5.png", wx.BITMAP_TYPE_ANY))





def _test():
    """ Run unit tests. """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    """ If script is run directly, then run unit tests """
    _test()
