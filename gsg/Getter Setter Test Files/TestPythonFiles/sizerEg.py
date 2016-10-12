#-------------------------------------------------------------------------------
# Name:        Sizers Example
# Purpose:
#
# Author:      Soribo
#
# Created:     10/09/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import wx


class SizerExample( wx.Frame ):


    def __init__( self, _parent, _id, _size ):
        """ """

        # call super constructor
        wx.Frame.__init__( self, _parent, _id, "Sizer Example", pos = (-1,-1),
                                size = _size )

        # init variables
        self.main_panel = wx.Panel( self, wx.ID_ANY )
        self.main_sizer = wx.BoxSizer( wx.VERTICAL )
        panel_1         = wx.Panel( self.main_panel, wx.ID_ANY )
        panel_2         = wx.Panel( self.main_panel, wx.ID_ANY )

        # set component attributes
        self.main_panel.SetBackgroundColour( (200,200,30) )
        panel_1.SetBackgroundColour( (0,0,30) )
        panel_2.SetBackgroundColour( (100,100,100) )

        # add components to sizer
        self.main_sizer.Add( panel_1, 1, wx.EXPAND | wx.ALL, 20 )  # Params( component, proportion - 0 = noresize, 2 = double resize of 1, flags, offset )
        self.main_sizer.Add( panel_2, 1, wx.EXPAND | wx.ALL, 20 )

        #set sizer
        self.main_panel.SetSizer( self.main_sizer )
        self.Centre()
        self.Show( True )



def main():

    app   = wx.App( True )

    frame = SizerExample( None, -1, wx.Size(500,600) )

    app.MainLoop()



if __name__ == '__main__':
    main()

