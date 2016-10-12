# Test of parsing text to identify & create variable objects


from Variable import *


CPLUSPLUS = 20001
JAVA      = 20002


c_plus_plus_var_names = ( 'void', 'int', 'float', 'double', 'short', 'long',
                          'char', 'string', 'const', 'static', 'vector' )
java_var_names        = ( 'void', 'int', 'float', 'double', 'char', 'String',
                          'byte', 'final', 'static', 'Integer', 'Character',
                          'Vector', 'Set', 'Object', 'Collection', 'Stack',
                          'Queue', 'Map' )

def parse_text( text ):
    """ Post: """
    

    if sel_language == CPLUSPLUS:

        var_list = c_plus_plus_var_names

    else:

        var_list = java_var_names

        
    word_list = format_text( text.split() )

    for word in word_list:

        var_type = find_var_type( word, var_list )

        if var_type != None:

            var_name = 

                 


def format_text( text ):
    """ Post: Format all word to lowercase """

    for char in text:

        if char.isUpper():

            char = char.toLower()

    return text

    

def get_wrapper_count( text ):
    """ Post: Identify classes within text & split text into list """

    structure_list = text.split( 'struct' )
    class_list     = text.split( 'class' )


    for index in len(class_list)-1:

        if ( class_list[index] == 'class' ):

            class_implementation = class_list[index+1].split()
            class_implementation = format_text( class_implementation )

            class_name = class_implementation[0]

            # find var type occurence
            # get the next word after var type, ie, get variable name
            # if the next wrd/char is '=' OR var_name  ends with ';' and not = '('
            #     get the variable value

            self.variable_list.append( Variable( var_name,  var_data_type,
                                                 var_value, class_name )

            index++
        

        

        
    
