#-------------------------------------------------------------------------------
# Name:        Getter Setter SourceCode class
# Purpose:
#
# Author:      Soribo
#
# Created:     08/12/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


from    math                 import floor
from    GetterSetterGlobal   import BOTH
import  GetterSetterVariable as Variable



class SourceCode:

    ## Class Variables:

    # self.code
    # self.wrapper_list
    # self.variable_list
    # self.end_dec
    # self.end_chars
    # self.wrapper_tags
    # self.format_chars
    # self.data_type_tags
    # self.comment_tag
    # self.comment_blk_strt_tag
    # self.comment_blk_end_tag
    # self.quotation_type_tags


    ## Class Functions: ##

    def __init__( self, _source_code ):
        """ """

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
        self.format_chars         = ( (',',  ', '),  ('(',  '( '),  (')',  ' )'),
                                      (':',  ' : '), ('=',  '= ') )
        self.data_type_tags       = ( 'bool',  'char',    'int', 'long',
                                      'short', 'string', 'float',
                                      'UINT',  'POINT' )


    def find_variables( self ):
        """ """

        ## Format code
        ## Identify end of classes
        ## Parse for wrappers
        ## Parse for variables
        ## Return variable list

        self.wrapper_list  = []
        self.variable_list = []


        source_code        = self.format_code( self.code )
        print source_code

        """if not self.is_code_valid( source_code ):
            print "Source code is not valid"
            return None"""

        for wrapper_type in self.wrapper_tags:

            self.wrapper_list += self.extract_wrappers( source_code, [], 0, wrapper_type )[0]


        self.variable_list = self.extract_variables( self.wrapper_list )

        return self.variable_list


    def format_code( self, source_code ):
        """ Post: """

        # for every '{' put a space on either side of it
        # for every '}'
        #     if the next char == ';' put a space on the left
        #     & a space after the colon!
        #     else place a space on the left & right
        # for every '=' & ',' add a space before & after
        # for every ';' ONLY add a space AFTER!!!

        source_code = self.remove_superficial_code( source_code )


        for char_set in self.format_chars:

            source_code = source_code.replace( char_set[0], char_set[1] )


        # Mark the end of each classes declaration
        for wrapper_type in self.wrapper_tags:

                source_code = self.catalog_end_of_class( source_code, wrapper_type )


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
        open_arrow_num       = source_code.count( '<' )
        closed_arrow_num     = source_code.count( '>' )
        comment_num          = source_code.count( self.comment_tag )
        comment_blk_strt_num = source_code.count( self.comment_blk_strt_tag )
        comment_blk_end_num  = source_code.count( self.comment_blk_end_tag  )


        print "Comment = " + self.comment_tag
        print "Comment strt = " + self.comment_blk_strt_tag
        print "Comment end = " + self.comment_blk_end_tag
        print "Comments identified: " + str(comment_num)
        print "Comment Blk start identified: " + str(comment_blk_strt_num)
        print "Comment Blk end identified: " + str(comment_blk_end_num)
        print "Num of open brackets: " + str( source_code.count( '{' ) )
        print "Num of close brackets: " + str( source_code.count( '}' ) )



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

                    source_code = source_code[0 : start_index] + "STRING REMOVED" + source_code[end_index + 1 : len(source_code)]



        # Delete all whitespace before an open bracket
        start_index = 0
        end_index   = 0

        for open_bracket in range( source_code.count( '(' ) ):

            start_index = source_code.find( '(', start_index )
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



        # Delete all whitespace before a comma
        start_index = 0
        end_index   = 0

        for comma in range( source_code.count( ',' ) ):

            start_index = source_code.find( ',', start_index )
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



        # Delete all whitespace before an equals character
        start_index = -1
        end_index   = 0

        for comma in range( source_code.count( '=' ) ):

            start_index = source_code.find( '=', start_index+1 )
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


    def catalog_end_of_class( self, code_str, wrapper_name ):
        """ """

        end_len   = len( self.end_chars[0] )
        sel_class = -1
        wrap_num  = code_str.count( wrapper_name )


        while wrap_num > 0:

            sel_class  = code_str.find( wrapper_name,      sel_class+1 )
            nxt_end    = code_str.find( self.end_chars[0], sel_class+1 )
            open_count = 0
            end_count  = 0


            while True:

                open_count = code_str.count( '{', sel_class, nxt_end+end_len )
                end_count  = 0

                for char in self.end_chars:

                    c = code_str.count( char, sel_class, nxt_end+end_len )
                    if c > 0:
                        end_count += c


                if end_count == open_count:

                    print "Found end: " + str(open_count) + ", " + str(end_count)
                    code_str  = code_str[0 : nxt_end] + '\n~~\n' + code_str[nxt_end+end_len : len(code_str)]
                    wrap_num -= 1
                    break

                else:

                    print str(open_count) + ", " + str(end_count)
                    nxt_end = code_str.find( self.end_chars[0], nxt_end + end_len, len(code_str) )
                    if nxt_end < 0:
                        print "File incorrectly formatted"
                        return code_str  # None


        return code_str


    def is_code_valid( self, source_code ):
        """ Post: """

        wrapper_count         = 0
        end_declaration_count = source_code.count( self.end_dec )

        for wrapper in self.wrapper_tags:

            num = source_code.count( wrapper )

            if num > 0:
                wrapper_count += num


        return ( wrapper_count == end_declaration_count )


    def extract_wrappers( self, code_str, wrapper_list, begin_index, wrapper ):
        """ Pre:  code_str must be formatted to remove comments & strings
            Post: Recursively identify & store all wrappers in code_str """

        end_dec     = self.end_dec
        wrapper_num = code_str.count( wrapper )

        ## while ( True ):
        while wrapper_num > 0:

            strt_wrap = code_str.find( wrapper, begin_index )
            end_wrap  = code_str.find( end_dec, strt_wrap+1 )
            nxt_wrap  = code_str.find( wrapper, strt_wrap+1 )

            if nxt_wrap <= -1:

                nxt_wrap = 999999


            if nxt_wrap <= end_wrap:

                data         = self.extract_wrappers( code_str, wrapper_list, nxt_wrap, wrapper )
                wrapper_list = data[0]
                code_str     = data[1]

            elif strt_wrap == -1:

                break

            elif end_wrap > -1:

                try:
                    wrapper_type = self.format_var( code_str[strt_wrap : len(code_str)].split( " ", 1 )[0] )
                    wrapper_name = self.format_var( code_str[strt_wrap : len(code_str)].split( " ", 2 )[1] )
                    wrapper_dec  = code_str[strt_wrap : end_wrap+2]

                    print "CREATING WRAPPER: dec=" + wrapper_dec + "!!!!!!!!!!!!!!!!!!!!"

                    wrapper_list.append( (wrapper_type, wrapper_name, wrapper_dec) )

                except IndexError:
                    pass

                code_str      = code_str[0 : strt_wrap] + code_str[end_wrap+2 : len(code_str)]
                wrapper_num  -= 1


        return (wrapper_list, code_str)


    def extract_variables( self, wrapper_list ):
        """ """

        var_list  = []
        var_types = self.data_type_tags

        for wrapper in wrapper_list:

            print "\nSEARCHING %s for variables" % wrapper[1]

            wrapper_name = wrapper[1]
            wrapper_dec  = "; " + wrapper[2] + " ;"

            for data_type in var_types:

                while wrapper_dec.count( data_type ) > 0:

                    var_pos = wrapper_dec.find( data_type )
                    var_dec = self.get_var_declaration( wrapper_dec, var_pos )

                    if var_dec == None:
                        # wrapper_dec = wrapper_dec.replace( data_type, '' )
                        break

                    # if not a function
                    if var_dec.count('(') <= 0:

                        var_data  = self.get_var_data( var_dec )
                        var_names = var_data[0]
                        var_type  = var_data[1]

                        for name in var_names:

                            print "Var name=    " + self.format_var( name )
                            print "Var type=    " + self.format_var( var_type )
                            print "Owner class= " + self.format_var( wrapper_name )
                            var_list.append( self.create_variable(name, var_type,
                                                                  0, wrapper_name,
                                                                  BOTH) )


                    wrapper_dec = wrapper_dec.replace( var_dec.replace(';',''), '' )


        return var_list


    def find_first_char( self, s, chars, begin, end, limit_type ):
        """ """

        if limit_type >= 0:
            found = [ n for n in [ s.rfind(c, begin, end) for c in chars ] if not n==-1 ]
        else:
            found = [ n for n in [ s.find(c, begin, end) for c in chars ] if not n==-1 ]

        if len(found) == 0:
            return -1
        else:
            if limit_type >= 0:
                return max(found)
            else:
                return min(found)


    def get_var_declaration( self, var_dec, var_pos ):
        """ """

        try:

            dec_strt = self.find_first_char( var_dec, ':{;', 0, var_pos, 1 )              # var_dec.rindex( ';', 0, var_pos )
            dec_end  = self.find_first_char( var_dec, '=;', var_pos, len(var_dec), -1 )   # var_dec.index( ';', var_pos, len(var_dec) )

            return var_dec[dec_strt : dec_end+1]

        except ValueError:

            print "<get_var_declaration>Error: ValueError"

        except Exception:

             print "<get_var_declaration>Error: Unknown Exception"

        return None


    def format_var( self, var_str ):
        """ """

        var_str = str( var_str )
        return var_str.translate( None, "\t\r\n\v;:{}=~~" ).strip()


    def get_var_data( self, var_str ):
        """ """

        com_num   = var_str.count(',')
        var_type  = ""
        var_names = []
        print "Var_str= " + var_str

        if com_num <= 0:
            # INDEX ERROR COULD OCCUR!!
            data      = var_str.rsplit( " ", 1 )
            var_type  = self.format_var( data[0] )
            var_names.append( self.format_var( data[1] ) )

        else:

            data     = var_str.split( "," )
            var_type = self.format_var( data[0].rsplit(" ", 1)[0] )
            var_names.append( self.format_var( data[0].rsplit(" ", 1)[1] ) )
            del data[0]

            for name in data:

                var_names.append( self.format_var( name ) )


        print "Var_names= " + str(var_names)
        print "Var_type= " + var_type
        return (var_names, var_type)


    def create_variable( self, var_name, var_type, var_value, wrapper_name, gen_type ):
        """ Post: """

        return Variable.Variable( var_name, var_type, var_value, wrapper_name, gen_type )


    def generate_variable_code( self ):
        """ Post: """

        variable_code = ""

        for var in self.variable_list:

            variable_code += var.get_code()

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
        """ """

        SourceCode.__init__( self, _source_code )

        self.format_chars   = tuple( self.format_chars + (('};', '??\n'), ('~',  '!'), ('{',  ' {\n'), ('.',  '. '), ('*', '* ')) )
        self.end_dec        = '~~'
        self.end_chars      = ('??', '}', '~~')
        self.wrapper_tags   = tuple( self.wrapper_tags + ('struct', ) )
        self.data_type_tags = ( self.data_type_tags + ('vector', 'queue', 'stack') )


    def create_variable( self, var_name, var_type, var_value, wrapper_name, gen_type ):
        """ Post: """

        return Variable.CPlusVariable( var_name, var_type, var_value, wrapper_name, gen_type )


    def format_code( self, source_code ):
        """ Post:  """

        # remove all "typedefs"
        for x in range( source_code.count('typedef') ):

            try:

                pos = source_code.find( 'typedef' )
                end = source_code.find( ';', pos+1 )

                source_code = source_code[0 : pos] + source_code[end : len(source_code)]

            except Exception, e:
                print "Source code is incorrectly formatted"
                return None

        return SourceCode.format_code( self, source_code )




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
        """ """

        SourceCode.__init__( self, _source_code )

        self.format_chars    = tuple( self.format_chars + (('{',  ' {\n'), ('.',  '. ')) )
        self.end_dec         = '~~'
        self.end_chars       = ('}', '~~')
        self.wrapper_tags    = tuple( self.wrapper_tags + ('interface', ) )
        self.data_type_tags  = ( 'private', 'public', 'protected' )


    def create_variable( self, var_name, var_type, var_value, wrapper_name, gen_type ):
        """ Post: """

        return Variable.JavaVariable( var_name, var_type, var_value, wrapper_name, gen_type )



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
        """ """

        SourceCode.__init__( self, _source_code )

        self.comment_tag          = '#'
        self.comment_blk_strt_tag = '"""'
        self.comment_blk_end_tag  = '"""'
        self.end_dec              = '~~'
        self.data_type_tags       = ( 'self.', )


    def catalog_end_of_class( self, code_str, wrapper_name ):
        """ Post: Identify & mark the 'end of class declaration' for
                  each python class in python code """

        sel_class   = -1
        end_dec_str = "\n%s\n" % self.end_dec
        end_index   = 0
        class_num   = code_str.count( wrapper_name )


        for x in range( class_num ):

            sel_class     = code_str.find ( wrapper_name, sel_class + 1 )
            class_strt    = code_str.rfind( '\n', 0, sel_class )
            target_indent = self.get_indentation( self.get_nxt_line(code_str, class_strt)[0] )
            end_index     = self.get_nxt_line(code_str, class_strt)[1]


            while (True):

                nxt_line_data = self.get_nxt_line( code_str, end_index )
                nxt_line      = nxt_line_data[0]
                end_index     = nxt_line_data[1]

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

        # return ( (line.replace(' ', '')).isalnum() == False )
        return ( len( line_str ) <= 0 )


    def get_indentation( self, code_ln ):
        """ Post: Return the number of whitespace characters at the start
                  of code_ln string """

        after_indent = code_ln.lstrip()
        indent_str   = code_ln[ 0 : len(code_ln)-len(after_indent) ].expandtabs(4).replace('\n','')

        return len(indent_str)


    def extract_variables( self, wrapper_list ):
        """ Post: """

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
                        var_name = self.format_var( var_name )
                        print "Looking at var: " + var_name

                        if not var_name in cur_vars:
                            cur_vars.append( var_name )

                except Exception, e:
                    pass


            print cur_vars
            for var in cur_vars:

                var_list.append( Variable.PythonVariable( var, "Undefined",
                                                          0, wrapper_name,
                                                          BOTH )  )

        return var_list




