#-------------------------------------------------------------------------------
# Name:        Generation Type Chooser RadioBox
# Purpose:
#
# Author:      Soribo
#
# Created:     07/10/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import wx


class GenerationTypeChooser( wx.RadioBox ):


    ## Class Variables:

    # self.parent
    # self.choices
    # self.variable_index


    ## Class Functions:

    def __init__( self, _parent, _ulc, _id, _title, _variable_index ):
        """ Default Constructor: """

        self.parent         = _parent
        self.choices        = ( 'Getter', 'Setter', 'Both' )
        self.variable_index = _variable_index


        wx.RadioBox.__init__( self, _ulc, _id, _title, choices = self.choices )

        self.SetSelection( 2 )

        # self.Bind( wx.wxEVT_COMMAND_RADIOBOX_SELECTED, self.parent.on_generation_type_change ) # OR EVT_RADIOBOX



