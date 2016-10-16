#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


import wx


class GenerationTypeChooser( wx.ComboBox ):

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



