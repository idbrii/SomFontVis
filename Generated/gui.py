#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.5 on Thu Apr 10 17:34:22 2008 from /home/dbriscoe/code/som/gladeGui

import wx

class FontFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FontFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "Output Visualizer")
        self.alpha_vsizer_1_staticbox = wx.StaticBox(self, -1, "Alpha")
        self.letterImage = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/data/TimesNewRoman_B.png", wx.BITMAP_TYPE_ANY))
        self.output = wx.RadioBox(self, -1, "Output: Cluster", choices=["1", "2", "3", "4", "5", "6"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.selectImageButton = wx.Button(self, -1, "Select Image...")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.nEpochs = wx.SpinCtrl(self, -1, "5", min=0, max=10000)
        self.button_train = wx.Button(self, -1, "Train")
        self.button_reset = wx.Button(self, -1, "Reset")
        self.static_line_2 = wx.StaticLine(self, -1)
        self.label_alpha_init = wx.StaticText(self, -1, "a(0) = ")
        self.tCtrl_alpha = wx.TextCtrl(self, -1, "0.8", style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_RIGHT)
        self.label_alpha_t = wx.StaticText(self, -1, "a(t) = ")
        self.tCtrl_scale = wx.TextCtrl(self, -1, "0.5", style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_RIGHT)
        self.label_alpha_tminus1 = wx.StaticText(self, -1, "*a(t-1)")
        self.static_line_1_copy = wx.StaticLine(self, -1)
        self.weightImage_0 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/weight/0.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_1 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/weight/0.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_2 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/weight/0.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_3 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/weight/0.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_4 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/weight/0.png", wx.BITMAP_TYPE_ANY))
        self.weightImage_5 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/dbriscoe/code/som/weight/0.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.OnModifyOutput, self.output)
        self.Bind(wx.EVT_BUTTON, self.OnSelectImage, self.selectImageButton)
        self.Bind(wx.EVT_BUTTON, self.OnTrain, self.button_train)
        self.Bind(wx.EVT_BUTTON, self.OnReset, self.button_reset)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FontFrame.__set_properties
        self.SetTitle("SomFontVis")
        self.output.SetToolTipString("The input image's cluster, as assigned by the SOM.")
        self.output.SetSelection(0)
        self.selectImageButton.SetToolTipString("Choose an image to input into the SOM. Must have been normalized.")
        self.nEpochs.SetToolTipString("How many times to run through the training set.")
        self.button_train.SetToolTipString("Run the SOM through x epochs of training.")
        self.button_reset.SetToolTipString("Reset the SOM to its initial (randomized) state.")
        self.tCtrl_alpha.SetToolTipString("The initial value of alpha.")
        self.tCtrl_scale.SetToolTipString("How much to scale alpha by after each epoch.")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FontFrame.__do_layout
        vsizer_root = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(3, 3, 1, 1)
        vsizer_3 = wx.BoxSizer(wx.VERTICAL)
        alpha_vsizer_1 = wx.StaticBoxSizer(self.alpha_vsizer_1_staticbox, wx.VERTICAL)
        sizer_alphafunc = wx.BoxSizer(wx.HORIZONTAL)
        sizer_alphainit = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        vsizer_3_2 = wx.BoxSizer(wx.VERTICAL)
        hsizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        vsizer_2_1 = wx.BoxSizer(wx.VERTICAL)
        vsizer_2_1.Add((100, 20), 0, wx.EXPAND, 0)
        vsizer_2_1.Add(self.letterImage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        hsizer_2.Add(vsizer_2_1, 1, wx.EXPAND, 0)
        hsizer_2.Add(self.output, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        hsizer_2.Add((20, 20), 0, 0, 0)
        vsizer_root.Add(hsizer_2, 1, wx.EXPAND, 0)
        vsizer_root.Add(self.selectImageButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        vsizer_3.Add(self.static_line_1, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 10)
        hsizer_3.Add((20, 20), 0, 0, 0)
        label_epochs = wx.StaticText(self, -1, "Number of epochs")
        vsizer_3_2.Add(label_epochs, 0, 0, 0)
        vsizer_3_2.Add(self.nEpochs, 0, 0, 0)
        hsizer_3.Add(vsizer_3_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.button_train, 0, wx.ALL, 1)
        sizer_1.Add(self.button_reset, 0, wx.ALL, 1)
        hsizer_3.Add(sizer_1, 1, wx.EXPAND, 0)
        hsizer_3.Add((20, 20), 0, 0, 0)
        vsizer_3.Add(hsizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        vsizer_3.Add(self.static_line_2, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 10)
        sizer_alphainit.Add(self.label_alpha_init, 0, 0, 0)
        sizer_alphainit.Add(self.tCtrl_alpha, 0, wx.ALIGN_RIGHT, 0)
        alpha_vsizer_1.Add(sizer_alphainit, 1, wx.EXPAND, 0)
        sizer_alphafunc.Add(self.label_alpha_t, 0, 0, 0)
        sizer_alphafunc.Add(self.tCtrl_scale, 0, wx.ALIGN_RIGHT, 0)
        sizer_alphafunc.Add(self.label_alpha_tminus1, 0, 0, 0)
        alpha_vsizer_1.Add(sizer_alphafunc, 1, wx.EXPAND, 0)
        vsizer_3.Add(alpha_vsizer_1, 1, wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND, 10)
        vsizer_root.Add(vsizer_3, 1, wx.EXPAND, 0)
        vsizer_root.Add(self.static_line_1_copy, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 10)
        grid_sizer_1.Add(self.weightImage_0, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.weightImage_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.weightImage_2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.weightImage_3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.weightImage_4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.weightImage_5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        vsizer_root.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(vsizer_root)
        vsizer_root.Fit(self)
        self.Layout()
        # end wxGlade

    def OnModifyOutput(self, event): # wxGlade: FontFrame.<event_handler>
        print "Event handler `OnModifyOutput' not implemented!"
        event.Skip()

    def OnSelectImage(self, event): # wxGlade: FontFrame.<event_handler>
        print "Event handler `OnSelectImage' not implemented!"
        event.Skip()

    def OnTrain(self, event): # wxGlade: FontFrame.<event_handler>
        print "Event handler `OnTrain' not implemented"
        event.Skip()


    def OnReset(self, event): # wxGlade: FontFrame.<event_handler>
        print "Event handler `OnReset' not implemented"
        event.Skip()

# end of class FontFrame




if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    somFontVis = SomFontFrame(None, -1, "")
    app.SetTopWindow(somFontVis)
    somFontVis.Show()
    app.MainLoop()
