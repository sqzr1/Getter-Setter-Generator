#-------------------------------------------------------------------------------
# Application: Getter Setter Creator -
#              This application automatically generates Getter & Setter
#              functions for a classes member variables.
#
#              Methodology:
#                   - parse source code
#                   - identify wrappers (class, interface, struct...)
#                   - identify each wrappers member variables
#                   - generate setter & getter functions
#
# Name:        Getter Setter Controller
# Purpose:     This class is the Controller component of the applications
#              MVC architecture. The message processing performed within
#              this class is imitates a window proceedure function in
#              Win32.
#
# Author:      Soribo
#
# Created:     08/09/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import wx
from GetterSetterView      import *   # GetterSetterView
from GetterSetterModel     import *   # GetterSetterModel
from GetterSetterGlobal    import *



class Controller:

    ## Class Variables: ##

    # self.app_window
    # self.app_model


    ## Class Functions: ##

    def __init__( self ):
        """ Default Constructor: Define Model & View compenents of the
            MVC architecture """

        App = wx.App(redirect=True)  # Error messages go to popup window

        self.app_window = GetterSetterView ( None, self, wx.Point(10,10), wx.Size(700,400), wx.HORIZONTAL )
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

                self.app_window.show_error_dialog( "Input file is not defined. Please drag & drop a file into the input area, copy & paste some code into the input area or click the Browse button" )


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
        """ Post: Used to call regression & integration tests when performing
                  application maintenance & updates """

        pass




## Main Thread ##

def main():
    """ """

    controller = Controller()


if __name__ == "__main__":

    main()

