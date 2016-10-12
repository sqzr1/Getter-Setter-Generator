#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


try:
    import wx
except ImportError:
    print "Please install wxPython: 'apt-get install python-wxgtk2.8', 'easy_install wxPython' or 'pip install wxPython'"


import wx
from view                   import *   
from model                  import *   
from getter_setter_global   import *



class Controller:

    ## Class Variables: ##

    # self.app_window
    # self.app_model


    ## Class Functions: ##

    def __init__( self ):
        """ Default Constructor: Define Model & View compenents of the
            MVC architecture """

        App = wx.App(redirect=False)  # Error messages do not go to popup dialog

        self.locale     = wx.Locale(wx.LANGUAGE_ENGLISH)
        self.app_window = GetterSetterView ( None, self, wx.Point(10,10), wx.Size(600,600), wx.VERTICAL )
        self.app_model  = GetterSetterModel( self.app_window )


        self.debug()


        self.app_window.Show()
        App.MainLoop()


    def window_proc( self, msg, w_param ):
        """ Post:  """

        if msg == GS_GENERATE_CODE:

            self.app_model.generate_code()

        elif msg == GS_FIND_VARIABLES:

            # Check input defined
            if self.app_model.is_input_defined():

                self.app_model.find_variables( w_param )

            else:

                self.app_window.show_error_dialog( """Input file is not defined. Please drag & drop a file into the input area, copy & paste some code into the input area or click the Browse button""" )


        elif msg == GS_UPDATE_VARIABLE:

            w_param_type = str( type( w_param) )

            # Check if w_param is an array(tuple/list) >= 2
            if  w_param_type == "<type 'tuple'>"  or  w_param_type == "<type 'list'>":

                if len( w_param ) >= 2:

                    self.app_model.set_variable_generation_type( w_param )


        elif msg == GS_FILE_DROP:

            pass

        elif msg == GS_INPUT_CHANGE:

            self.app_model.set_input_data( w_param )
            self.app_window.toggle_generate_bt( False )

        elif msg == GS_OUTPUT_CHANGE:

            self.app_model.set_output_data( w_param )

        elif msg == GS_LANGUAGE_CHANGE:

            self.app_model.set_language( w_param )

        elif msg == GS_CLOSE:

            self.app_window.Destroy() # destroy view window


    def debug( self ):
        """ Post: Used for regression and integration tests"""

        pass




## Main Thread ##

def main():
    """ """

    controller = Controller()


if __name__ == "__main__":

    main()

