
import os
from   GetterSetterSourceCode import *



def get_files_in_dir( directory, file_ext ):
    """ """

    # dir_files = filter( lambda x: x.endswith(file_ext), os.listdir(directory))
    # OR
    # html_files = [x for x in os.listdir(directory) if x.endswith(file_ext)]

    dir_files = []
    
    for f in os.listdir(directory):

        if f.endswith(file_ext):
            dir_files.append( directory + "\\" + f )

    return dir_files


def create_log_file( file_name ):
    """ """

    f = open( file_name, 'w' )
    f.close()


def create_object( file_name, source_code ):
    """ """

    if file_name.endswith( ".java" ):

        return JavaCode( source_code )

    elif file_name.endswith( ".py" ) or file_name.endswith( ".pyw" ):

        return PythonCode( source_code )

    else:

        return CPlusCode( source_code )


def write_to_log( file_name, code_file_name, var_list ):
    """ """

    var_template = """

var_name     = %s
var_type     = %s
var_value    = %d
wrapper_name = %s
gen_type     = %d


"""

    cur_wrappers = []
    output_str   = ""

    f = open( file_name, 'aw' )

    if not f:
        print "Failed to open file log"
        return None

    f.write( "Source_code_file = " + code_file_name + "\n" )
    f.write( "Wrappers found   = \n" )

    for var in var_list:

        output_str += var_template % (var.var_name, var.data_type, var.var_value,
                                      var.wrapper_name, var.function_type)

        if not var.wrapper_name in cur_wrappers:

            cur_wrappers.append( var.wrapper_name )
            f.write( cur_wrappers[-1] + "\n" )

    f.write( output_str )

    f.close()

    
def test_find_variables( test_dirs, log_name ):
    """ """

    for directory in test_dirs:

        if not os.path.isdir( directory[0] ):

            print "Is not a directory"
            return None


        paths = get_files_in_dir( directory[0], directory[1] )

        for code_file in paths:

            code     = open(code_file,'r').read()
            src_code = create_object( directory, code )
            var_list = src_code.find_variables()

            write_to_log( log_name, code_file, var_list )

            

### Main ###

if __name__ == "__main__":

    os.chdir( os.getcwd() )
    
    test_dirs = (("\\Getter Setter Test Files\\TestC++Files",    ".h"),
                 ("\\Getter Setter Test Files\\TestJavaFiles",   ".java"),
                 ("\\Getter Setter Test Files\\TestPythonFiles", ".py")   )

    create_log_file( "GetterSetterLog.rtf" )

    for di in test_dirs:

        test_find_variables( di, "GetterSetterLog.rtf" )
