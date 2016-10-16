#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


import  wx
import  getter_setter_variable          as     Variable
from    math                            import floor
from    getter_setter_source_code       import *
from    getter_setter_global            import *  


class GetterSetterModel:

    ## Class Functions: ##

    def __init__( self, _app_window ):
        """ Constructor: Store controller component """

        self.app_window = _app_window
        self.init_variables()



    def init_variables( self ):
        """ Post: Initialise class member variables """

        self.src_code        = None
        self.input_name      = "NULL"
        self.input_contents  = "NULL"
        self.output_name     = "NULL"
        self.output_contents = "NULL"
        self.variable_list   = []
        self.sel_language    = CPLUSPLUS



    def set_input_data( self, file_name ):
        """ Post: Read a selected source code file, create source code object
                  & display file contents """

        file_content = self.read_file( file_name )

        if file_content != None:


            if self.sel_language == JAVA:

                self.src_code   = JavaCode( file_content )

            elif self.sel_language == PYTHON:

                self.src_code   = PythonCode( file_content )

            else:
                self.src_code   = CPlusCode( file_content )


            self.input_name     = file_name
            self.input_contents = file_content
            self.app_window.set_input_content( (file_name, file_content) )



    def set_output_data( self, file_name ):
        """ Post: Inform the view component that the output file has changed """

        self.output_name = file_name
        self.app_window.set_output_name( file_name )

        # NOTE: Should really make this function write the text in output
        #       textfield to a file



    def is_input_defined( self ):
        """ Post: Returns true if the input source code file has been
                  specified, else false. """

        return ( (self.input_name != "NULL") )



    def set_language( self, sel_language ):
        """ Post: Change the current programming language selected """

        if sel_language == 'Java':

            self.sel_language = JAVA
            self.src_code     = JavaCode( self.input_contents )

        elif sel_language == 'Python':

            self.sel_language = PYTHON
            self.src_code     = PythonCode( self.input_contents )

        ## elif sel_language == 'C++':
        else:

            self.sel_language = CPLUSPLUS
            self.src_code     = CPlusCode( self.input_contents )



    def determine_language( self ):
        """ Post: Determine what programming language a file is written in
                  by looking at the file type of the source code file """

        input_file_type = ""

        try:

            input_file_type = self.input_name.rsplit('.')[-1]
            # OR
            # input_file      = wx.FileType( self.input_name )
            # input_file_type = input_file.GetMimeType()

        except IndexError:

            print IndexError

        except Exception:

            print Exception


        if input_file_type == "h"       or  input_file_type == 'cpp':

            self.set_language( "C++" )


        elif input_file_type == "java"  or  input_file_type == 'class':

            self.set_language( "Java" )


        elif input_file_type == "py"    or  input_file_type == 'pyw':

            self.set_language( "Python" )


        else:

            self.set_language( "C++" )



    def set_variable_generation_type( self, variable_data ):
        """ Post: Set a variables generation type (whether we generate code for a
                  Getter function or a Setter function or both) for a specific
                  variable """

        variable_index    = variable_data[0]
        variable_gen_type = variable_data[1]


        if str( type(variable_index) ) != "<type 'int'>"  or  variable_index < 0   or  variable_index >= len( self.variable_list ):

            self.app_window.show_error_dialog( "Error setting variable generation type: Variable you are altering does not exist" )
            return


        if variable_gen_type == "Getter":

            self.variable_list[ variable_index ].function_type = Variable.GETTER

        elif variable_gen_type == "Setter":

            self.variable_list[ variable_index ].function_type = Variable.SETTER

        elif variable_gen_type == "Both":

            self.variable_list[ variable_index ].function_type = Variable.BOTH

        else:

            self.app_window.show_error_dialog( "Error setting variable generation type: Invalid Generation type specified" )



    def read_file( self, file_name ):
        """ Post: Read a source code file's text contents"""

        try:

            file = open( file_name, 'r' )
            text = file.read()

            file.close()

            return text

            """
            THE BELOW CODE WILL MAKE SURE WE DONT READ A FILE THAT IS EXTRAORDINARILY LARGE

            file_stream   = open( name, 'r' )
            file_contents = ""

            # Make sure we do not read something that will require more than
            # the machines memory
            while ( not file_stream.eof()  and  len(file_contents) < 999999 ):

                line = file_stream.readline()

                if not (line):
                    break

                else:
                    file_contents += line


            file_stream.close()

            """

        except IOError, error:

            self.app_window.show_error_dialog(  "Error opening file\n" + str(error) )
            return None

        except UnicodeDecodeError, error:

            self.app_window.show_error_dialog( "Cannot open non ascii files\n" + str(error) )
            return None

        except TypeError, error:

            self.app_window.show_error_dialog( "Invalid file type: \n" + str(error) )
            return None



    def find_variables( self, code ):
        """ Post: Send message to source code object to search for wrapper
                  variables & send message to view component to display
                  them """

        self.src_code.code = code
        self.variable_list = self.src_code.find_variables()

        if self.variable_list == -1:

            self.app_window.show_error_dialog( "Source code is incorrectly formatted" )

        elif len(self.variable_list) > 0:

            self.app_window.toggle_generate_bt( True )
            self.app_window.display_variables(  self.variable_list )

        else:

            self.app_window.show_error_dialog( "There were no wrapper member variables identified in input file" )


        print "\n\nVARIABLES FOUND: "
        for v in self.variable_list:

            print v.var_name + ", " + str(v.data_type) + ", " + v.wrapper_name



    def generate_code( self ):
        """ Post: Send message to source code object to generate getter &
                  setter functions for all variables that have been
                  identified """

        self.output_contents = self.src_code.generate_variable_code( self.sel_language )

        self.app_window.set_output_content( self.output_contents )








