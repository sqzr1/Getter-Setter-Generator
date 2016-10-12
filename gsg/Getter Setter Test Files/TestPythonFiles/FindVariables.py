
import io
import Variable


def reverse( _list ):
    """ Note: For some reason the STD string function .reverse() returns
              an object of NoneType. So I have made my own function to
              maintain the type list.
        Post: Return a list with the elements arranged in the reverse order
              of _list. """

    reverse_list = []
    list_index    = len( _list ) - 1
    
    while ( list_index >= 0 ):

        reverse_list.append( _list[list_index] )
        list_index -= 1

    return reverse_list


        
def read_file( file_name ):
    """ """

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
        while ( len(file_contents) < 999999 ):

            line = file_stream.readline()

            if not (line):
                break

            else:
                file_contents += line


        file_stream.close()

        """

    except IOError, error:

        print "ERROR"
        # dlg = wx.MessageDialog( None, 'Error opening file\n' + str(error) )
        # dlg.ShowModal()

    except UnicodeDecodeError, error:

        print "ERROR"
        # dlg = wx.MessageDialog( None, 'Cannot open non ascii files\n' + str(error) )
        # dlg.ShowModal()

    return "NULL"



def format_code():
    """ Post: """

    # for every '{' put a space on either side of it
    # for every '}'
    #     if the next char == ';' put a space on the left
    #     & a space after the colon!
    #     else place a space on the left & right
    # for every '=' & ',' add a space before & after
    # for every ';' ONLY add a space AFTER!!!

    # maybe remove all comments
    pass


def validate_code( file_content, language_type ):
    """ Post: """

    # Optionally format source file 
    # content = format_code( file_content, language_type )
    content = file_content

    class_count           = content.count( 'class' )
    struct_count          = content.count( 'struct' )
    end_declaration_count = content.count( '};' )


    # if there are more wrappers than end declarations then the
    # file is incorectly formatted
    if class_count + struct_count  > end_declaration_count:

        print "File contents(Source Code) is incorrectly formatted: More wrappers than end declarations."
        return None

    elif class_count == 0  and  class_struct == 0:

        print "No wrappers found in source code."
        return None


    """

    # Optionally extract class & struct definitions from includes
    # & etc. junk
    
    # Grab the class definition part of contents & throw away rest
    first_class  = content.find( 'class' )
    first_struct = content.find( 'struct' )

    if first_class == -1:

        first_class  = 99999

    elif first_struct == -1:

        first_struct = 99999

    
    if first_class <= first_struct:

        content = "class " + content.partition( 'class' )[2]

    else:

        content = "struct " + content.partition( 'struct' )[2]


    content = content.rpartition( '};' )[0] + "};"

    """
    
    content = content.split()                 # Split into list of words
    content = reverse( content )              # Reverse list

    return content



def recursive_extract_wrappers( content_list, abstraction_degree, wrapper_list ):
    """ """

    while ( content_list.count('};') > 0 ):
        
        last_end_declaration = -1


        for i in range( abstraction_degree ):

            try: 
                end_declaration_pos     = content_list.index( '};', last_end_declaration + 1, len(content_list) )
            except ValueError:
                end_declaration_pos     = -1

            try:
                nxt_end_declaration_pos = content_list.index( '};', end_declaration_pos  + 1, len(content_list) )
            except ValueError:
                nxt_end_declaration_pos = -1

            last_end_declaration    = end_declaration_pos


        if end_declaration_pos < 0:

            break


        bracket_pos  = content_list.index( '{', end_declaration_pos )
        wrapper_type = content_list[ bracket_pos + 2 ]


        if bracket_pos > nxt_end_declaration_pos  and  nxt_end_declaration_pos >= 0:

            data = recursive_extract_wrappers( content_list,
                                               abstraction_degree + 1,
                                               wrapper_list )

            content_list = data[0]
            wrapper_list = data[2]
            

        elif wrapper_type == 'class'  or  wrapper_type == 'struct':

            wrapper_name        = content_list[ bracket_pos + 1 ]
            wrapper_declaration = reverse (  content_list[ end_declaration_pos : bracket_pos ] )
            wrapper_list.append( (wrapper_type, wrapper_name, wrapper_declaration) )

            del content_list[ end_declaration_pos : bracket_pos + 3 ]

        else:

            if content_list[ bracket_pos + 1 ] == '=':

                del content_list[ end_declaration_pos : bracket_pos + 4 ]

            else:
                del content_list[ end_declaration_pos : bracket_pos + 3 ]


    return (content_list, abstraction_degree, wrapper_list)
            


def extract_variables( wrapper_list ):
    """ Post: """

    variable_list  = []
    data_type_list = ('bool', 'char', 'int', 'long', 'short', 'string' )

    for wrapper in wrapper_list:
        
        for data_type in data_type_list:

            while ( wrapper[2].count(data_type) > 0 ):
                
                try:

                    var_type_index = wrapper[2].index( data_type )
                    var_name_index = var_type_index + 1

                    var_name       = wrapper[2][ var_name_index ].replace(';','')

                    # if not var_name.endswith( ')' ):
                    if not var_name.endswith( ')' ) and not '(' in var_name and var_name.isalnum():

                        variable_list.append( Variable.Variable( var_name,
                                                                 wrapper[2][ var_type_index ],
                                                                 0, wrapper[1],
                                                                 Variable.BOTH ) )

                    del wrapper[2][var_type_index : var_name_index]

                except IndexError:

                    print "In extract_variables(): IndexError thrown."
                    print "Will Get An Infinite Loop Here if u dont fix this!!!!"
                    del wrapper[2][var_type_index]
                    

    return variable_list



def find_variables( input_file_name ):
    """ """

    # 1. Read file & store contents
    file_content = read_file( input_file_name )


    # 2. Format contents
    # Not implemented yet

    
    # 3. Separate & store classes in 2d array 'list of list of words'
    wrapper_content = validate_code( file_content, None )


    # 4. Identify & store each wrapper declaration
    if not wrapper_content == None:

        wrapper_list    = recursive_extract_wrappers( wrapper_content, 1,
                                                      list() )[2]


        # 5. Print the wrappers we found
        for wrapper in wrapper_list:

            print "Wrapper type: " + str(wrapper[0])
            print "Wrapper name: " + str(wrapper[1])
            print "Wrapper content: " + str(wrapper[2])
            print "\n\n\n\n"

        
        # 6. Search each wrapper definition for variables & store them when found
        var_list = extract_variables( wrapper_list )


        for var in var_list:

            print "Variable: " + var.var_name
            print "Type: " + var.data_type
            print "Value: " + str(var.var_value)
            print "Wrapper Parent: " + var.wrapper_name
            print "\n\n\n"
    



# test
find_variables( "C:\Users\Soribo\Desktop/updateBox.h" )
