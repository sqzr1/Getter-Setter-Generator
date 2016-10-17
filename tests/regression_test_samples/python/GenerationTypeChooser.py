#-------------------------------------------------------------------------------
# Name:        Generation Type Chooser ComboBox
# Purpose:     Subclass the combobox widget to be placed in an
#              UltimateListCtrl widget & allow the user to change
#              the type of function generation for a certain variable
#              to only generate Getter functions, or Setter Functions
#              or both.
#
# Author:      Soribo
#
# Created:     07/10/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import wx


class GenerationTypeChooser( wx.ComboBox ):


    ## Class Variables:

    # self.parent
    # self.choices
    # self.variable_index


    ## Class Functions:

    def __init__( self, _parent, _ulc, _id, _title, _variable_index ):
        """ Default Constructor: Initialise member variables & combobox
            selection """

        self.parent         = _parent
        self.choices        = ( 'Getter', 'Setter', 'Both' )
        self.variable_index = _variable_index


        wx.ComboBox.__init__( self, _ulc, _id, _title, choices = self.choices )

        self.SetSelection( 2 )

        self.Bind( wx.EVT_COMBOBOX, self.parent.on_generation_type_change )



