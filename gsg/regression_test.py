#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


import os
from   getter_setter_source_code import *



class SourceFile:

    def __init__( self, _path, _type ):
        """ Constructor """

        self.path      = _path
        self.type      = _type
        self.wrap_list = []
        self.var_list  = []
        self.src_code  = None

        self.create_object()


    def read_file( self ):
        """ Post: Read a file """

        return open( self.path, 'r' ).read()


    def log_wrappers( self ):
        """ Post: Record all wrappers found in a file """

        for var in self.var_list:

            if not var.wrapper_name in self.wrap_list:

                self.wrap_list.append( var.wrapper_name )


    def create_object( self ):
        """ Post: Create SourceCode object according to the file type (what
                  programming language the file is written in) """

        content = self.read_file()

        if self.type == "JAVA"  or  self.type == ".java":

            self.src_code = JavaCode( content )

        elif self.type == "PYTHON"  or  self.type == ".py":

            self.src_code = PythonCode( content )

        else:

            self.src_code = CPlusCode( content )


        self.var_list  = self.src_code.find_variables()

        if self.var_list == -1:
            self.var_list = []
            raw_input( "Intentionally caught a test file that has illegal code. \nPress enter to continue" )

        self.log_wrappers()


    def to_string( self ):
        """ Post: Return a string that explains all features of this source
                  file including its absolute path, wrapper names & wrapper
                  variables """

        var_template = "%s,%s,%s,%s,%d\n"
        res          = "%s\n" % self.path

        for wrap in self.wrap_list:

            res += wrap + ","

        if len(self.wrap_list) > 0:
            res = res[0 : len(res)-1]

        res += "\n"

        for var in self.var_list:

            res += var_template % (var.var_name, var.data_type, var.var_value,
                                   var.wrapper_name, var.function_type)


        return res + "\n"



class MockSourceFile:

    def __init__( self, _path, _wrap_list, _var_list, _type ):
        """ Constructor """

        self.path      = _path
        self.wrap_list = _wrap_list
        self.var_list  = _var_list
        self.type      = _type
        self.src_code  = None

        if len(self.wrap_list) > 0  and  self.wrap_list[0] == '':
            self.wrap_list = []

        if len(self.var_list) > 0  and  self.var_list[0] == '':
            self.var_list = []

        # Convert to same data type as a real SourceFile object
        if len(self.var_list) > 0:
            for var in self.var_list:

                var[-3] = int(var[-3])
                var[-1] = int(var[-1])


    def compare( self, src_code ):
        """ Post: Compare wrappers & variables of a real SourceFile object
                  against this object & return the 'comparision result' as
                  a string """

        var_list  = []
        template  = "Test of %s: " % self.path

        for var in src_code.src_code.variable_list:

            var_list.append( [var.var_name, var.data_type, var.var_value,
                              var.wrapper_name, var.function_type] )

        sol_list = []
        test_list = []
        
        for a in (self.var_list):
            sol_list.append( a[0] )

        for a in (var_list):
            test_list.append( a[0] )

        for a in (sol_list):

            if not a in test_list:
                print a


        if self.path.split('\\')[-1] != src_code.path.split('\\')[-1]:

            return template + "Not the same files\n"

        if self.wrap_list != src_code.wrap_list:

            return template + "Wrappers dont match\n"

        if self.var_list != var_list:

            return template + "Variables dont match\n"

        return template + "success\n"



def get_files_in_dir( directory, file_ext ):
    """ Post: Open a directory & return all files that have the same
              extension as file_ext """

    # dir_files = filter( lambda x: x.endswith(file_ext), os.listdir(directory))
    # OR
    # html_files = [x for x in os.listdir(directory) if x.endswith(file_ext)]

    dir_files = []

    for f in os.listdir(directory):

        if f.endswith(file_ext):
            dir_files.append( directory + "\\" + f )

    return dir_files


def create_log_file( file_name ):
    """ Post: Create a file in the current directory """

    f = open( file_name, 'w' )
    f.close()


def parse_solution_file_ex( file_name ):
    """ Post: Parse a file containing the results of previous tests & create a
              MockSourceFile object to represent that test. Returns a dictionary
              (of MockSourceFile objects) which contains all the test solutions """

    test_sols = {}

    content   = open(file_name, 'r').read().split('\n')

    if content == None:
        print "Failed to open testsols.rtf"
        return test_sols

    while len(content) > 0:
        
        try:
            path      = content[0]
            wrap_list = content[1].split(',')
            var_list  = []
            type      = "." + path.rsplit('.')[-1]
            del content[0:2]

            while content[0] != "":

                var_list.append( content[0].split(',') )
                del content[0]

            test_sols[str(path).split('\\')[-1]] = MockSourceFile( path, wrap_list, var_list, type )
            del content[0]

        except Exception, e:
            print "Error: " + str(e)
            break

    return test_sols


def write_to_solution_file( file_name, src_file ):
    """ Post: Write a solution(path, wrapper list & variable list) to
              TestSolutions.rtf file """

    f = open( file_name, 'a' )

    if not f:
        print "Failed to open solutions file"
        return None

    f.write( src_file.to_string() )

    f.close()


def write_to_log_file( file_name, string ):
    """ Post: Write the results of a regression test(a comparison of a current
              test with the correct solution) to the Test Log file -
              GetterSetterLog.rtf """

    f = open( file_name, 'a' )

    if not f:
        print "Failed to open file log"
        return None

    f.write( string )

    f.close()


def test_find_variables( test_dir, log_name, test_sol_name, test_sols ):
    """ Post: For all files in test_dir, read file, create SourceFile object,
              find variables, compare variable result to the correct solution
              & finally write the results of the comparison/test to the test
              log file """

    if not os.path.isdir( test_dir[0] ):

        print test_dir[0] + " is not a directory"
        return None


    paths = get_files_in_dir( test_dir[0], test_dir[1] )

    for code_file in paths:

        src_file = SourceFile( code_file, test_dir[1] )

        if test_sols.has_key( src_file.path.split('\\')[-1] ):

            result = test_sols[code_file.split('\\')[-1]].compare( src_file )
            write_to_log_file( log_name, result )
            print result
            
            if result.split()[-1] != "success":
                raw_input()


        else:

            print "\nRESULT: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            print src_file.to_string()
            os.startfile( src_file.path )
            dec = raw_input( "Is this data correct? " )

            if dec.lower() == 'y':
                write_to_solution_file( test_sol_name, src_file )



