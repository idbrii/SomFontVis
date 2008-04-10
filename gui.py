#! /usr/bin/env python

import wx
from Generated import gui

#            wx.BeginBusyCursor()            
#            wx.EndBusyCursor()

class SomFontFrame(gui.FontFrame):
    def __init__(self, *args, **kwds):
        gui.FontFrame.__init__(self, *args, **kwds)
        self.selectedOutput = 0
        self.letterFilename = "/home/dbriscoe/code/som/data/TimesNewRoman_B.png"
        # TODO: Set up SOM

    def _selectOutput(self, i):
        self.selectedOutput = i
        self.output.SetSelection(i)

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
        self.letterImage.Destroy()
        self.letterImage = wx.StaticBitmap(self, -1, wx.Bitmap(inFilename, wx.BITMAP_TYPE_ANY))
        self.Layout()





if __name__ == "__main__":
    import wx
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    somFontVis = SomFontFrame(None, -1, "")
    app.SetTopWindow(somFontVis)
    somFontVis.Show()
    app.MainLoop()
