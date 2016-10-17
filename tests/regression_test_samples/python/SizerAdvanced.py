#-------------------------------------------------------------------------------
# Name:        Sizer Advanced Example
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


class AdvancedSizer( wx.Frame ):

    def __init__( self, _parent, _id, _size ):
        """ """

        # Call super constructor
        wx.Frame.__init__( self, _parent, _id, "Advanced Sizer Example", pos = (-1,-1),
                           size = _size )

        # Init variables
        self.main_panel = wx.Panel( self, wx.ID_ANY )
        self.main_sizer = wx.BoxSizer( wx.VERTICAL )  # Sizer to create a border
        self.comp_sizer = wx.BoxSizer( wx.VERTICAL )  # Sizer to hold all components


        # Create & add all my components here...
        self.init_panel1()
        self.init_panel2()
        self.init_panel3()
        self.init_panel4()
        self.init_panel5()

        # Set sizer
        self.main_sizer.Add( self.comp_sizer, 1, wx.LEFT | wx.EXPAND | wx.ALL, 5 )
        self.main_panel.SetSizer( self.main_sizer )
        self.Centre()
        self.Show( True )


    def init_panel1( self ):
        """ """

        panel1 = wx.Panel( self.main_panel, wx.ID_ANY )
        sizer1 = wx.GridSizer( 2, 2 )

        sizer1.Add( wx.StaticText( panel1, wx.ID_ANY, "Find:", pos = (5,5) ), 0, wx.ALIGN_CENTER_VERTICAL )
        sizer1.Add( wx.ComboBox( panel1, wx.ID_ANY, size = (120,-1) ), 1, wx.EXPAND )
        sizer1.Add( wx.StaticText( panel1, wx.ID_ANY, "Get:", pos = (5,5) ), 0, wx.ALIGN_CENTER_VERTICAL )
        sizer1.Add( wx.ComboBox( panel1, wx.ID_ANY, size = (120,-1) ), 1, wx.EXPAND )

        panel1.SetSizer( sizer1 )
        self.comp_sizer.Add( panel1, 0, wx.TOP | wx.BOTTOM | wx.EXPAND | wx.ALL, 10 )


    def init_panel2( self ):
        """ """

        panel2 = wx.Panel( self.main_panel, wx.ID_ANY )
        sizer2 = wx.BoxSizer( wx.HORIZONTAL )
        dir_box = wx.StaticBoxSizer( wx.StaticBox( panel2, wx.ID_ANY, "Direction"), wx.VERTICAL )
        scp_box = wx.StaticBoxSizer( wx.StaticBox( panel2, wx.ID_ANY, "Scope"), wx.VERTICAL )


        dir_box.Add( wx.RadioButton( panel2, wx.ID_ANY, "Forward", style = wx.RB_GROUP ) )
        dir_box.Add( wx.RadioButton( panel2, wx.ID_ANY, "Backward") )

        scp_box.Add( wx.RadioButton( panel2, wx.ID_ANY, "All", style = wx.RB_GROUP ) )
        scp_box.Add( wx.RadioButton( panel2, wx.ID_ANY, "Selected") )

        sizer2.Add( dir_box, 1, wx.RIGHT, 5 )
        sizer2.Add( scp_box, 1 )

        panel2.SetSizer( sizer2 )
        self.comp_sizer.Add( panel2, 0, wx.BOTTOM | wx.EXPAND | wx.ALL, 10 )


    def init_panel3( self ):
        """ """

        panel3 = wx.Panel( self.main_panel, wx.ID_ANY )
        sizer3 = wx.StaticBoxSizer( wx.StaticBox( panel3, wx.ID_ANY, "Options" ), wx.VERTICAL )

        check_bx_sizer = wx.GridSizer( 3, 2, 5, 5 )

        check_bx_sizer.Add( wx.CheckBox( panel3, wx.ID_ANY, "Case Sensitive" ) )
        check_bx_sizer.Add( wx.CheckBox( panel3, wx.ID_ANY, "Wrap Search" ) )
        check_bx_sizer.Add( wx.CheckBox( panel3, wx.ID_ANY, "Whole Word" ) )
        check_bx_sizer.Add( wx.CheckBox( panel3, wx.ID_ANY, "Incremental" ) )
        check_bx_sizer.Add( wx.CheckBox( panel3, wx.ID_ANY, "Regular Expressions" ) )

        sizer3.Add( check_bx_sizer, 1, wx.EXPAND )

        panel3.SetSizer( sizer3 )
        self.comp_sizer.Add( panel3, 0, wx.EXPAND | wx.BOTTOM | wx.ALL, 10 )


    def init_panel4( self ):
        """ """

        panel4 = wx.Panel( self.main_panel, wx.ID_ANY )
        sizer4 = wx.GridSizer( 2, 2, 5, 5 )

        sizer4.Add( wx.Button( panel4, wx.ID_ANY, "Find", size = (120,-1) ) )
        sizer4.Add( wx.Button( panel4, wx.ID_ANY, "Find/Replace", size = (120,-1) ) )
        sizer4.Add( wx.Button( panel4, wx.ID_ANY, "Replace", size = (120,-1) ) )
        sizer4.Add( wx.Button( panel4, wx.ID_ANY, "Replace All", size = (120,-1) ) )

        panel4.SetSizer( sizer4 )
        self.comp_sizer.Add( panel4, 0, wx.BOTTOM | wx.EXPAND | wx.ALL, 10 )


    def init_panel5( self ):
        """ """

        panel5 = wx.Panel( self.main_panel, wx.ID_ANY )
        sizer5 = wx.BoxSizer( wx.HORIZONTAL )

        sizer5.Add( (170,-1), 1, wx.RIGHT | wx.EXPAND )
        sizer5.Add( wx.Button( panel5, wx.ID_ANY, "Close", size = (80,-1) ), 1, wx.EXPAND )

        panel5.SetSizer( sizer5 )
        self.comp_sizer.Add( panel5, 0, wx.BOTTOM | wx.EXPAND | wx.ALL, 10 )





def main():

    app = wx.App( True )

    frame = AdvancedSizer( None, -1, wx.Size(300,500) )

    app.MainLoop()

if __name__ == '__main__':
    main()