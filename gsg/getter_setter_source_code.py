#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


from    math                    import  floor
from    getter_setter_global    import  BOTH
import  getter_setter_variable  as      Variable



class SourceCode:

    ## Class Functions: ##

    def __init__( self, _source_code ):
        """ Constructor: Initialise member variables"""

        self.code                 = _source_code
        self.comment_tag          = '//'
        self.comment_blk_strt_tag = '/*'
        self.comment_blk_end_tag  = '*/'
        self.end_dec              = '};'
        self.end_chars            = ('}', '??', '~~')
        self.wrapper_tags         = ("class" ,)
        self.quotation_type_tags  = ('"', "'")
        self.wrapper_list         = []
        self.variable_list        = []
        self.format_chars         = ( (',',  ', '),  ('(',  '( '), (')',  ' )'),
                                      (':',  ' : '), ('=',  '= ') )
        self.data_type_tags       = ( 'bool',  'char',    'int', 'long',
                                      'short', 'string', 'float',
                                      'UINT',  'POINT' )


    def find_variables( self ):
        """ Post: Format source code, collect wrappers then return all
                  variables found in each wrapper """

        ## Format code
        ## Identify end of classes
        ## Parse for wrappers
        ## Parse for variables
        ## Return variable list

        self.wrapper_list  = []
        self.variable_list = []


        source_code        = self.format_code( self.code )

        if source_code == None  or not  self.is_code_valid( source_code ):
            return -1


        self.wrapper_list  = self.extract_wrappers( source_code, [], 0 )[0]


        self.variable_list = self.extract_variables( self.wrapper_list )

        return self.variable_list


    def format_code( self, source_code ):
        """ Post: Format source code to create some kind of consistancy
                  (especially when dealing with different coding styles/
                  semantics) & get the code ready to be parsed """

        source_code = self.remove_superficial_code( source_code )

        for char_set in self.format_chars:

            source_code = source_code.replace( char_set[0], char_set[1] )


        # Mark the end of each classes declaration
        source_code = self.catalog_end_of_class( source_code, self.wrapper_tags )


        return source_code


    def remove_superficial_code( self, source_code ):
        """ Post: Identify & remove all code that is unrelated to a
                  wrapper(class)'s definition from source_code &
                  return source_code

                  This function is rather exceptional because its code is
                  broad & stable enough to identify & remove comments & strings
                  regardless of the programming language the file contents
                  are composed of.  """


        start_index          = 0
        end_index            = 0
        comma_num            = source_code.count( ',' )
        equals_num           = source_code.count( '=' )
        open_bracket_num     = source_code.count( '(' )
        comment_num          = source_code.count( self.comment_tag )
        comment_blk_strt_num = source_code.count( self.comment_blk_strt_tag )
        comment_blk_end_num  = source_code.count( self.comment_blk_end_tag  )


        # Delete all comment blocks from code
        if comment_blk_strt_num  ==  comment_blk_end_num:

            for comment_block in range( comment_blk_strt_num ):


                start_index = source_code.find( self.comment_blk_strt_tag, start_index     )
                end_index   = source_code.find( self.comment_blk_end_tag,  start_index + 1 )

                if end_index == -1:

                    break

                source_code = source_code[0 : start_index] + "\n ; \n" + source_code[end_index + len(self.comment_blk_strt_tag) : len(source_code)]


        # Delete all comments from code
        start_index = 0
        end_index   = 0

        for comment in range( source_code.count( self.comment_tag ) ):


            start_index = source_code.find( self.comment_tag, start_index )
            end_index   = source_code.find( "\n", start_index )

            if end_index == -1:

                break

            source_code = source_code[0 : start_index] + "\n ; \n" + source_code[end_index : len(source_code)]


        # Delete all strings from code
        start_index = 0
        end_index   = 0

        for quotation_mark in self.quotation_type_tags:

            string_num = int( floor( source_code.count(quotation_mark) / 2 ) )
            start_index = 0
            end_index   = 0

            for string in range( string_num ):

                start_index = source_code.find( quotation_mark, start_index )
                end_index   = source_code.find( quotation_mark, start_index + 1 )

                if end_index != -1:

                    source_code = source_code[0 : start_index] + " ;STRING REMOVED; " + source_code[end_index + 1 : len(source_code)]


        # Delete all whitespace before an special chars
        delim_chars = ( '(', '=', ',' )

        for delim in delim_chars:

            start_index = 0
            end_index   = 0

            for delim_occurence in range( source_code.count( delim ) ):

                start_index = source_code.find( delim, start_index )
                x           = start_index - 1

                try:
                    while source_code[ x ]  ==  ' '  or  source_code[ x ]  ==  '\t'  or  source_code[ x ]  ==  '\r':

                        # del source_code[ x ]
                        # OR
                        source_code  = source_code[ 0 : x ] + source_code[ x + 1 : len(source_code) ]
                        x  -= 1


                except IndexError:

                    print "Index error thrown"
                    pass

                start_index = x + 2

        return source_code


    def catalog_end_of_class( self, code_str, wrapper_tags ):
        """ Post: Identify & mark the end of each wrapper """

        end_len      = len( self.end_chars[0] )
        sel_class    = -1

        while True:

            sel_class  = self.get_nxt_wrapper_index( code_str, sel_class+1, wrapper_tags )
            nxt_end    = code_str.find( self.end_chars[0], sel_class+1 )
            open_count = 0
            end_count  = 0

            if sel_class >= 9999999:

                break

            while True:

                open_count = code_str.count( '{', sel_class, nxt_end+end_len )
                end_count  = 0

                for char in self.end_chars:

                    c = code_str.count( char, sel_class, nxt_end+end_len )
                    if c > 0:
                        end_count += c


                # if nxt_end's position is at the end of a classes declaration
                if end_count == open_count:

                    code_str  = code_str[0 : nxt_end] + '\n~~\n' + code_str[nxt_end+end_len : len(code_str)]
                    break

                else:

                    nxt_end = code_str.find( self.end_chars[0], nxt_end + end_len, len(code_str) )
                    if nxt_end < 0:
                        print "File incorrectly formatted"
                        return None


        return code_str


    def is_code_valid( self, source_code ):
        """ Post: Abstract(Virtual) function that is overloaded in
                  sub-classes to return true if code follows the
                  correct programming standards else false """

        return True


    def extract_wrappers( self, code_str, wrapper_list, begin_index ):
        """ Pre:  code_str must be formatted to remove comments & strings
            Post: Recursively identify & store all wrappers found in
                  code_str """

        end_dec      = self.end_dec
        wrapper_tags = self.wrapper_tags

        while ( True ):

            strt_wrap = self.get_nxt_wrapper_index( code_str, begin_index, wrapper_tags )
            end_wrap  = code_str.find( end_dec, strt_wrap+1 )
            nxt_wrap  = self.get_nxt_wrapper_index( code_str, strt_wrap+1, wrapper_tags )


            # if there are no more wrappers in code_str
            if strt_wrap >= 9999999:

                break

            # if we have a nested wrapper (a wrapper inside another wrapper)
            elif nxt_wrap <= end_wrap:

                data         = self.extract_wrappers( code_str, wrapper_list, nxt_wrap )
                wrapper_list = data[0]
                code_str     = data[1]

            elif end_wrap > -1:

                try:
                    wrapper_type = self.format_var( code_str[strt_wrap : len(code_str)].split( " ", 1 )[0] )
                    wrapper_name = self.format_var( code_str[strt_wrap : len(code_str)].split( " ", 2 )[1] )
                    wrapper_dec  = code_str[strt_wrap : end_wrap+2]

                    wrapper_list.append( (wrapper_type, wrapper_name, wrapper_dec) )

                except IndexError:
                    pass

                code_str      = code_str[0 : strt_wrap] + code_str[end_wrap+2 : len(code_str)]

            """else: #if end_wrap <= -1:
                print "Code is incorrectly formatted"
                # NEED to throw an exception to break all recursive iterations
                raw_input()
                return (None, None)"""


        return (wrapper_list, code_str)


    def get_nxt_wrapper_index( self, source_code, begin_index, wrapper_tags ):
        """ Post: Find & return the index position of the next class within
                  source_code """

        nxt_wrappers = []

        for wrapper_name in wrapper_tags:

            nxt_wrap_index = begin_index-1

            while True:

                nxt_wrap_index = source_code.find( wrapper_name, nxt_wrap_index+1 )

                if nxt_wrap_index <= -1:

                    nxt_wrappers.append( 9999999 )
                    break

                elif self.is_wrapper( source_code, nxt_wrap_index, wrapper_name ):

                    nxt_wrappers.append( nxt_wrap_index )
                    break

        return min( nxt_wrappers )


    def is_wrapper( self, source_code, wrapper_pos, wrapper_name ):
        """ Post: Abstract(Virtual) function that is overloaded in
                  sub-classes to return true if we have identified the
                  beginning of wrapper """

        return True


    def extract_variables( self, wrapper_list ):
        """ Post: Identify & return all member variables for each wrapper
                  in wrapper_list """

        var_list  = []
        var_types = self.data_type_tags

        for wrapper in wrapper_list:

            wrapper_name = wrapper[1]
            wrapper_dec  = "; " + self.remove_implementation( wrapper[2] ) + " ;"

            for data_type in var_types:

                while wrapper_dec.count( data_type ) > 0:

                    var_pos = wrapper_dec.find( data_type )
                    var_dec = self.get_var_declaration( wrapper_dec, var_pos )

                    if var_dec == None:
                        break

                    # if not a function
                    if var_dec.count('(') <= 0:

                        var_data  = self.get_var_data( var_dec )

                        for var in var_data:

                            var_list.append( self.create_variable(var[0], var[1],
                                                                  0, wrapper_name,
                                                                  BOTH) )


                    wrapper_dec = wrapper_dec.replace( var_dec.replace(';',''), '' )


        return var_list


    def remove_implementation( self, wrapper_dec ):
        """ Post: Abstract(Virtual) function that is overloaded in
                  sub-classes to remove the implementation of a classes
                  member function """

        return wrapper_dec


    def find_first_char( self, s, chars, begin, end, limit_type ):
        """ Post: Return the index of the 1st occurence of any character from
                  chars in s. Using limit_type we can define whether we want
                  to start searching from the left or right
            Example: Search "abc,ghij;" for the 1st occurence of (',', ';', ':')
                     will return 3 (the index position of ',') """

        """found = [ n for n in [ s.rfind(c, begin, end) for c in chars ] if not n==-1 ]

        if len(found) == 0:
            return -1

        if limit_type >= 0:
            return max(found)

        return min(found)"""

        if limit_type >= 0:
            found = [ n for n in [ s.rfind(c, begin, end) for c in chars ] if not n==-1 ]
        else:
            found = [ n for n in [ s.find(c, begin, end) for c in chars ]  if not n==-1 ]

        if len(found) == 0:
            return -1

        if limit_type >= 0:
            return max(found)

        return min(found)


    def get_var_declaration( self, var_dec, var_pos ):
        """ Post: Return a line of text that contains a variables declaration """

        try:

            dec_strt = self.find_first_char( var_dec, ':;{??', 0, var_pos, 1 )
            dec_end  = self.find_first_char( var_dec, '=;{', var_pos, len(var_dec), -1 )

            return var_dec[dec_strt : dec_end+1]

        except ValueError:

            print "<get_var_declaration>Error: ValueError"

        except Exception:

             print "<get_var_declaration>Error: Unknown Exception"

        return None


    def format_var( self, var_str ):
        """ Post: Remove all non alpha numerical characters from the string
                  var_str """

        var_str = str( var_str )
        return var_str.translate( None, "\t\r\n\v:;,{}(+-/=~?" ).strip()


    def get_var_data( self, var_str ):
        """ Post: Take a string containing a variables declaration &
                  identify and return the variables name & data type """

        var_list   = []
        var_data  = var_str.expandtabs().split(",")
        var_type  = var_data[0].rsplit(" ", 1)[0]
        var_names = var_data[1 : len(var_data)]
        var_names.append( var_data[0].rsplit(" ", 1)[-1] )
        is_array   = var_type.find('[]') != -1

        for name in var_names:

            # if variable is an array & the MAIN data type is not an array
            if name.find(']') != -1:

                if not is_array:
                    type = self.format_var(var_type) + "[]"

                name = name.split("[")[0]

            else:
                type = self.format_var(var_type)

            if type != ""  and  self.format_var(name) != "":
                var_list.append( [self.format_var(name), type] )

        return var_list


    def create_variable( self, var_name, var_type, var_value, wrapper_name, gen_type ):
        """ Post: Create & return a GetterSetterVariable object """

        return Variable.Variable( var_name, var_type, var_value, wrapper_name, gen_type )


    def generate_variable_code( self, language ):
        """ Post: Get all variables to generate their getter/setter function
                  code & return it as one string """

        variable_code = ""

        for var in self.variable_list:

            variable_code += var.get_code( language )

        return variable_code




class CPlusCode( SourceCode ):

    ## Class Variables: ##

    # self.code                  ~ Inherited
    # self.wrapper_list          ~ Inherited
    # self.variable_list         ~ Inherited
    # self.end_dec               ~ Inherited   ~ Overridden
    # self.end_chars             ~ Inherited   ~ Overridden
    # self.wrapper_tags          ~ Inherited   ~ Overridden
    # self.format_chars          ~ Inherited   ~ Overridden
    # self.data_type_tags        ~ Inherited
    # self.comment_tag           ~ Inherited
    # self.comment_blk_strt_tag  ~ Inherited
    # self.comment_blk_end_tag   ~ Inherited
    # self.quotation_type_tags   ~ Inherited


    ## Class Functions: ##

    def __init__( self, _source_code ):
        """ Constructor: Initialise member variables """

        SourceCode.__init__( self, _source_code )

        self.format_chars   = tuple( self.format_chars + (('~',  '!'), ('{',  ' { \n'), ('}', ' }'), ('.',  '. '), ('*', '* '), (' :  : ', '@@')) )  # ('};', '??\n'),
        self.end_dec        = '~~'
        self.end_chars      = ('}', '~~')  # '??',
        self.wrapper_tags   = tuple( self.wrapper_tags + ('struct', ) )
        self.data_type_tags = ( self.data_type_tags + ('vector', 'queue', 'stack') )


    def create_variable( self, var_name, var_type, var_value, wrapper_name, gen_type ):
        """ Post: Override super function to create & return a
                  CPlusVariable object """

        return Variable.CPlusVariable( var_name, var_type, var_value, wrapper_name, gen_type )


    def is_wrapper( self, source_code, wrapper_pos, wrapper_name ):
        """ Post: Returns true if we have come across the beginning of a
                  wrapper at the position wrapper_pos in the string source
                  code """

        try:

            end_pos = source_code.find( '{', wrapper_pos+1 )
            wrapper = source_code[wrapper_pos : end_pos+1].split()

            if wrapper[0] == wrapper_name  and  wrapper[-1] == "{":

                if len(wrapper) == 3:

                    return True

                elif len(wrapper) > 3  and  wrapper[2] == ":":

                    return True

        except Exception, e:

            pass

        return False


    def is_code_valid( self, source_code ):
        """ Post: Returns true if code follows the correct programming
                  standards else false """

        if source_code.count('{') != (source_code.count('}') + source_code.count('~~')):
            return False
        if source_code.count('(') != source_code.count(')'):
            return False

        return True


    def remove_implementation( self, wrapper_dec ):
        """ Post: Remove each functions implementation within a specific
                  classes declaration """

        nxt_strt_brac = -1
        nxt_end_brac  = -1

        while True:

            nxt_end_brac  = wrapper_dec.find( ')', nxt_end_brac+1 )
            nxt_strt_brac = wrapper_dec.rfind( '(', 0, nxt_end_brac+1 )
            nxt_char      = self.find_first_char( wrapper_dec, ";{abcdefghijklmnopqrstuvwxyz", nxt_end_brac+1, len(wrapper_dec), -1 )

            if nxt_end_brac == -1:

                return wrapper_dec

            # if we have found a function that has implementation
            elif wrapper_dec[nxt_char] == '{':

                nxt_strt_paren = nxt_char
                nxt_end_paren  = nxt_char

                while True:

                    nxt_strt_paren = wrapper_dec.find( '{', nxt_strt_paren+1 )
                    nxt_end_paren  = wrapper_dec.find( '}', nxt_end_paren+1  )

                    if nxt_end_paren == -1:
                        break

                    if nxt_strt_paren == -1:

                        nxt_strt_paren = 9999999


                    if nxt_end_paren < nxt_strt_paren:
                        wrapper_dec = wrapper_dec[0 : nxt_end_brac+1] + ";" + wrapper_dec[nxt_end_paren+1 : len(wrapper_dec)]
                        break

            wrapper_dec = wrapper_dec[0 : nxt_strt_brac+1] + wrapper_dec[nxt_end_brac : len(wrapper_dec)]




class JavaCode( SourceCode ):

    ## Class Variables: ##

    # self.code                  ~ Inherited
    # self.wrapper_list          ~ Inherited
    # self.variable_list         ~ Inherited
    # self.end_dec               ~ Inherited   ~ Overridden
    # self.end_chars             ~ Inherited   ~ Overridden
    # self.wrapper_tags          ~ Inherited   ~ Overridden
    # self.format_chars          ~ Inherited   ~ Overridden
    # self.data_type_tags        ~ Inherited   ~ Overridden
    # self.comment_tag           ~ Inherited
    # self.comment_blk_strt_tag  ~ Inherited
    # self.comment_blk_end_tag   ~ Inherited
    # self.quotation_type_tags   ~ Inherited


    ## Class Functions: ##

    def __init__( self, _source_code ):
        """ Constructor: Initialise member variables """

        SourceCode.__init__( self, _source_code )

        self.format_chars    = tuple( self.format_chars + (('{',  ' {\n'), ('.',  '. '), (')', ');')) )
        self.end_dec         = '~~'
        self.end_chars       = ('}', '~~')
        self.wrapper_tags    = tuple( self.wrapper_tags + ('interface', ) )
        self.data_type_tags  = ( 'private', 'public', 'protected' )


    def create_variable( self, var_name, var_type, var_value, wrapper_name, gen_type ):
        """ Post: Override super function to create & return a
                  JavaVariable object """

        return Variable.JavaVariable( var_name, var_type, var_value, wrapper_name, gen_type )


    def is_wrapper( self, source_code, wrapper_pos, wrapper_name ):
        """ Post: Returns true if we have come across the beginning of a
                  wrapper at the position wrapper_pos in the string source
                  code """

        try:

            end_pos = source_code.find( '{', wrapper_pos+1 )
            wrapper = source_code[wrapper_pos : end_pos+1].split()

            if wrapper[0] == wrapper_name  and  wrapper[-1] == "{":

                if len(wrapper) == 3  or  wrapper[2] == "implements"  or  wrapper[2] == "extends":

                    return True

        except Exception, e:

            pass

        return False


    def is_code_valid( self, source_code ):
        """ Post: Returns true if code follows the correct programming
                  standards else false """

        if source_code.count('{') != (source_code.count('}') + source_code.count('~~')):
            return False

        return True



class PythonCode( SourceCode ):

    ## Class Variables: ##

    # self.code                  ~ Inherited
    # self.wrapper_list          ~ Inherited
    # self.variable_list         ~ Inherited
    # self.end_dec               ~ Inherited   ~ Overridden
    # self.end_chars             ~ Inherited
    # self.wrapper_tags          ~ Inherited
    # self.format_chars          ~ Inherited
    # self.data_type_tags        ~ Inherited   ~ Overridden
    # self.comment_tag           ~ Inherited   ~ Overridden
    # self.comment_blk_strt_tag  ~ Inherited   ~ Overridden
    # self.comment_blk_end_tag   ~ Inherited   ~ Overridden
    # self.quotation_type_tags   ~ Inherited


    ## Class Functions: ##

    def __init__( self, _source_code ):
        """ Constructor: Initialise member variables """

        SourceCode.__init__( self, _source_code )

        self.format_chars         = tuple( self.format_chars + (('+',  ' + '), ('-',  ' - '), ('*', ' * '), ('/', ' / '), ('%', ' % '),
                                                                ('"'+"'"+'"', ';'), ("'"+'"'+"'", ';')) )
        self.comment_tag          = '#'
        self.comment_blk_strt_tag = '"""'
        self.comment_blk_end_tag  = '"""'
        self.end_dec              = '~~'
        self.data_type_tags       = ( 'self.', )


    def is_wrapper( self, source_code, wrapper_pos, wrapper_name ):
        """ Post: Returns true if we have come across the beginning of a
                  wrapper at the position wrapper_pos in the string source
                  code """

        try:

            end_pos = source_code.find( ':', wrapper_pos+1 )
            wrapper = source_code[wrapper_pos : end_pos+1].split()

            if wrapper[0] == wrapper_name  and  wrapper[-1] == ":":

                if len(wrapper) == 3  or  (wrapper[1].endswith('(')  and  wrapper[-2].endswith(')')):

                    return True

        except Exception, e:

            pass

        return False


    def format_code( self, source_code ):
        """ Post: Format source code to create some kind of consistancy
                  (especially when dealing with different coding styles/
                  semantics) & get the code ready to be parsed """

        for char_set in self.format_chars:

            source_code = source_code.replace( char_set[0], char_set[1] )

        source_code = self.remove_superficial_code( source_code )


        # Mark the end of each classes declaration
        source_code = self.catalog_end_of_class( source_code, self.wrapper_tags )


        return source_code


    def catalog_end_of_class( self, code_str, wrapper_types ):
        """ Post: Identify & mark the 'end of class declaration' for
                  each python class in python code """

        sel_class   = -1
        end_dec_str = "\n%s\n" % self.end_dec
        end_index   = 0
        wrapper_num   = 0


        for wrapper_type in wrapper_types:

            c = code_str.count( wrapper_type )

            if c > 0:
                wrapper_num += c


        for x in range( wrapper_num ):

            sel_class     = self.get_nxt_wrapper_index( code_str, sel_class+1, wrapper_types )
            class_strt    = code_str.rfind( '\n', 0, sel_class )
            target_indent = self.get_indentation( self.get_nxt_line(code_str, class_strt)[0] )
            end_index     = self.get_nxt_line(code_str, class_strt)[1]


            # Search for & mark the end of a classes declaration
            while (True):

                nxt_line_data = self.get_nxt_line( code_str, end_index )
                nxt_line      = nxt_line_data[0]
                end_index     = nxt_line_data[1]

                # if we are at the end of the string
                if ( end_index >= len(code_str) ):

                    code_str += end_dec_str
                    break

                elif ( self.is_blank_line( nxt_line ) == False  and  self.get_indentation(nxt_line) <= target_indent ):

                    prev_index = code_str.rfind('\n', 0, end_index-2)
                    code_str   = code_str[0 : prev_index+1] + end_dec_str + code_str[prev_index+1 : len(code_str)]
                    break


        return code_str


    def get_nxt_line( self, code_str, begin_index ):
        """ Post: Identify the next 2 endline characters & return the
                  text in between these 2 characters """

        endln_pos = [ begin_index - 1, -1, -1 ]

        for i in range( len(endln_pos)-1 ):

            endln_pos[i+1] = code_str.find( '\n', endln_pos[i] + 1 )

            if endln_pos[i+1] == -1:

                return ( code_str[ endln_pos[i] : len(code_str) ], len(code_str) )


        return ( code_str[ endln_pos[1] : endln_pos[2] ], endln_pos[2] )


    def is_blank_line( self, line_str ):
        """ Post: Returns true if line_str is a blank line (can contain
                  " ", "\r", "\t" or "\v" chars. """

        delimiters = ( '\n', '\r', '\t', '\v', '#', ' ' )

        for delim in delimiters:

            line_str = line_str.replace( delim, '' )

        line_str = line_str.expandtabs(4)

        return ( len( line_str ) <= 0 )


    def get_indentation( self, code_ln ):
        """ Post: Return the number of whitespace characters at the start
                  of code_ln string """

        after_indent = code_ln.lstrip()
        indent_str   = code_ln[ 0 : len(code_ln)-len(after_indent) ].expandtabs(4).replace('\n','')

        return len(indent_str)


    def format_var( self, var_str ):
        """ Post: Remove all non alpha numerical characters from the string
                  var_str """

        var_str = str( var_str )
        return var_str.translate( None, "\t\r\n\v:;,{}[](+-*/=~?" ).strip()


    def extract_variables( self, wrapper_list ):
        """ Post: Identify & return all member variables for each wrapper
                  in wrapper_list """

        var_list  = []

        for wrapper in wrapper_list:

            sel_var      = -1
            cur_vars     = []
            wrapper_name = wrapper[1]
            wrapper_dec  = wrapper[2]

            for x in range( wrapper_dec.count("self.") ):

                sel_var  = wrapper_dec.find( "self.", sel_var+1 )
                end_var  = self.find_first_char( wrapper_dec, " .=", sel_var+5, len(wrapper_dec), -1 )

                try:
                    var_name = wrapper_dec[sel_var+5 : end_var]

                    if var_name.find( '(' ) == -1:
                        var_name = self.format_var( var_name.split("[")[0] )

                        if not var_name in cur_vars:
                            cur_vars.append( var_name )

                except Exception, e:
                    pass


            for var in cur_vars:

                var_list.append( Variable.PythonVariable( var, "Undefined",
                                                          0, wrapper_name,
                                                          BOTH )  )

        return var_list




