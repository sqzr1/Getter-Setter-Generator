#-------------------------------------------------------------------------------
# Name:        Getter Setter Model
# Purpose:
#
# Author:      Soribo
#
# Created:     08/09/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import  wx
import  GetterSetterVariable    as     Variable
from    math                    import floor
from    GetterSetterSourceCode  import *
from    GetterSetterGlobal      import *  # CPLUSPLUS, JAVA, PYTHON, c_plus_plus_getter_template, c_plus_plus_setter_template, java_getter_template, java_setter_template, python_getter_template, python_setter_template



class GetterSetterModel:

    ## Class Variables: ##

    # self.src_code
    # self.input_name
    # self.input_contents
    # self.output_name
    # self.output_contents
    # self.variable_list
    # self.sel_language
    # self.app_window


    ## Class Functions: ##

    def __init__( self, _app_window ):
        """ """

        self.app_window = _app_window
        self.init_variables()



    def init_variables( self ):
        """ """

        self.src_code        = None
        self.input_name      = "NULL"
        self.input_contents  = "NULL"
        self.output_name     = "NULL"
        self.output_contents = "NULL"
        self.variable_list   = []
        self.sel_language    = CPLUSPLUS



    def set_input_data( self, file_name ):
        """ """

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
        """ """

        self.output_name = file_name
        self.app_window.set_output_name( file_name )

        # NOTE: Should really make this function write the text in output
        #       textfield to a file



    def is_input_defined( self ):
        """ """

        return ( (self.input_name != "NULL") )



    def set_language( self, sel_language ):
        """ """

        if sel_language == 'Java':

            self.sel_language = JAVA

        elif sel_language == 'Python':

            self.sel_language = PYTHON

        ## elif sel_language == 'C++':
        else:

            self.sel_language = CPLUSPLUS



    def determine_language( self ):
        """ """

        try:

            input_file_type = self.input_name.rsplit('.')[-1]
            # OR
            # input_file      = wx.FileType( self.input_name )
            # input_file_type = input_file.GetMimeType()

        except IndexError:

            print IndexError
            return

        except Exception:

            print Exception
            return


        if input_file_type == "h"       or  input_file_type == 'cpp':

            self.sel_language = CPLUSPLUS


        elif input_file_type == "java"  or  input_file_type == 'class':

            self.sel_language = JAVA


        elif input_file_type == "py"    or  input_file_type == 'pyw':

            self.sel_language = PYTHON


        else:

            self.sel_language == CPLUSPLUS



    def set_variable_generation_type( self, variable_data ):
        """ Post: """

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
        """ Post: """

        try:

            file = open( file_name, 'r' )
            text = file.read()

            file.close()

            return text

            """
            THE BELOW CODE WILL MAKE SURE WE DONT READ A FILE THAT IS EXTRAORDINARILY LARGE(COULD USE CPU'S TOTAL MEMORY)

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
        """ """

        self.src_code.code = code
        self.variable_list = self.src_code.find_variables()

        if len(self.variable_list) > 0:

            self.app_window.toggle_generate_bt( True )
            self.app_window.display_variables(  self.variable_list )

        else:

            self.app_window.show_error_dialog( "There were no wrapper member variables identified in input file" )


        print "\n\nVARIABLES FOUND: "
        for v in self.variable_list:

            print v.var_name + ", " + str(v.data_type) + ", " + v.wrapper_name



    def generate_code( self ):
        """ """

        self.output_contents = self.src_code.generate_variable_code()

        self.app_window.set_output_content( self.output_contents )








