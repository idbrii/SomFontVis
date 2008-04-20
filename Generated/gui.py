#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.5 on Thu Apr 10 17:34:22 2008 from /home/dbriscoe/code/som/gladeGui

import wx

class FontFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FontFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.letterImage = wx.StaticBitmap(self, -1, wx.Bitmap("data/TimesNewRoman_B.png", wx.BITMAP_TYPE_ANY))
        self.output = wx.RadioBox(self, -1, "Output: Character", choices=["A", "B", "C", "D", "E", "F"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.selectImageButton = wx.Button(self, -1, "newImageButton")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.OnModifyOutput, self.output)
        self.Bind(wx.EVT_BUTTON, self.OnSelectImage, self.selectImageButton)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FontFrame.__set_properties
        self.SetTitle("SomFontVis")
        self.output.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FontFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_5.Add((100, 20), 0, 0, 0)
        sizer_5.Add(self.letterImage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_2.Add(self.output, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add((20, 20), 0, 0, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.selectImageButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def OnModifyOutput(self, event): # wxGlade: FontFrame.<event_handler>
        print "Event handler `OnModifyOutput' not implemented!"
        event.Skip()

    def OnSelectImage(self, event): # wxGlade: FontFrame.<event_handler>
        print "Event handler `OnSelectImage' not implemented!"
        event.Skip()

# end of class FontFrame




if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    somFontVis = SomFontFrame(None, -1, "")
    app.SetTopWindow(somFontVis)
    somFontVis.Show()
    app.MainLoop()
