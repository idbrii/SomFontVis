#! /usr/bin/env python

# run code
import gui
import som

import wx
app = wx.PySimpleApp(0)
wx.InitAllImageHandlers()

somFontVis = gui.SomFontFrame(None, -1, "")
app.SetTopWindow(somFontVis)
somFontVis.Show()
app.MainLoop()
