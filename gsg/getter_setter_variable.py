#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


from getter_setter_global import BOTH, GETTER, SETTER, CPLUSPLUS, JAVA, PYTHON



class Variable:

    ## Static Class Variables: ##

    getter_template = """
psuedo code:
function: %(var_type)s Get%(var_name)s()
{
    // Post: Getter function generated by Getter Setter Application

    return ( %(var_name)s );
}

"""

    setter_template = """
psuedo code:
function: %(var_type)s  Set%(var_name)s( %(var_type)s newValue )
{
    // Post: Setter function generated by Getter Setter Application

    %(var_type)s oldValue = %(var_name)s
    %(var_name)s = newValue;

    return ( oldValue );
}

"""


    ## Class Functions: ##

    def __init__( self, _name, _data_type, _var_value, _wrapper_name, _function_type ):
        """ Constructor: Initialise class member variables """

        self.var_name      = _name
        self.data_type     = _data_type
        self.var_value     = _var_value
        self.wrapper_name  = _wrapper_name
        self.function_type = _function_type


    def set_name( self, _name ):
        """ Post: Change a variables name/identifier """

        data_type    = str( type(_name) )

        if data_type == "<type 'string'>":   # OR "str"

            self.var_name = _name
            return True

        else:
            return False


    def set_data_type( self, _data_type ):
        """ Post: Change a variables data type """

        self.data_type = _data_type


    def set_function_type( self, _function_type ):
        """ Post: Change a variables code generation type """

        self.function_type = _function_type


    def get_code( self, language ):
        """ Post: Return this variables getter/setter function/code in a
                  specific programming language """

        if language == CPLUSPLUS:
            return self.generate_code( CPlusVariable.getter_template, CPlusVariable.setter_template )

        elif language == JAVA:
            return self.generate_code( JavaVariable.getter_template, JavaVariable.setter_template )

        elif language == PYTHON:
            return self.generate_code( PythonVariable.getter_template, PythonVariable.setter_template )

        else:
            return self.generate_code( Variable.getter_template, Variable.setter_template )



    def generate_code( self, _getter_template, _setter_template ):
        """ Post: Generate getter/setter functions for this variable """

        var_attribs  = { 'var_name'    : self.var_name,
                         'var_type'    : self.data_type,
                         'wrapper_name': self.wrapper_name }


        if self.function_type == GETTER:

            return _getter_template % var_attribs

        elif self.function_type == SETTER:

            return _setter_template % var_attribs

        else: # self.function_type == BOTH

            return ( _getter_template % var_attribs + _setter_template % var_attribs )



class CPlusVariable( Variable ):

    ## Class Variables: ##

    # self.var_name
    # self.data_type
    # self.var_value
    # self.wrapper_name
    # self.function_type


    ## Static Class Variables: ##

    getter_template = """

%(var_type)s  %(wrapper_name)s :: Get%(var_name)s()
{
    // Post: Getter function generated by Getter Setter Application

    return ( %(var_name)s );
}

"""

    setter_template = """

%(var_type)s  %(wrapper_name)s :: Set%(var_name)s( %(var_type)s newValue )
{
    // Post: Setter function generated by Getter Setter Application

    %(var_type)s oldValue = %(var_name)s
    %(var_name)s = newValue;

    return ( oldValue );
}

"""


    ## Class Functions: ##

    def __init__( self, _name, _data_type, _var_value, _wrapper_name, _function_type ):
        """ Constructor: Call super constructor """

        Variable.__init__( self, _name, _data_type.replace('@@', '::'), _var_value, _wrapper_name, _function_type )



class JavaVariable( Variable ):

    ## Class Variables: ##

    # self.var_name
    # self.data_type
    # self.var_value
    # self.wrapper_name
    # self.function_type


    ## Static Class Variables: ##

    getter_template = """

/**
 *   Post: Getter function generated by Getter Setter Application
 *
 *   @return the value of %(var_name)s
 */
public %(var_type)s Get%(var_name)s()
{
    return ( %(var_name)s );
}

"""

    setter_template = """

/**
 *   Post: Setter function generated by Getter Setter Application
 *
 *   @param  newValue  the new value %(var_name)s will be set to
 *
 *   @return the previous value of %(var_name)s
 *
 */
public %(var_type)s  Set%(var_name)s( %(var_type)s newValue )
{
    %(var_type)s oldValue = %(var_name)s
    %(var_name)s = newValue;

    return ( oldValue );
}

"""


    ## Class Functions: ##

    def __init__( self, _name, _data_type, _var_value, _wrapper_name, _function_type ):
        """ Constructor: Call super constructor """

        Variable.__init__( self, _name, _data_type, _var_value, _wrapper_name, _function_type )



class PythonVariable( Variable ):

    ## Class Variables: ##

    # self.var_name
    # self.data_type
    # self.var_value
    # self.wrapper_name
    # self.function_type


    ## Static Class Variables: ##

    getter_template = """

def get_%(var_name)s( self ):
    # Post: Getter function generated by Getter Setter Application

    return ( self.%(var_name)s )

"""

    setter_template = """

def set_%(var_name)s( self, new_value ):
    # Post: Setter function generated by Getter Setter Application

    old_value = self.%(var_name)s
    self.%(var_name)s = new_value;

    return ( old_value )

"""


    ## Class Functions: ##

    def __init__( self, _name, _data_type, _var_value, _wrapper_name, _function_type ):
        """ Constructor: Call super constructor """

        Variable.__init__( self, _name, _data_type, _var_value, _wrapper_name, _function_type )



