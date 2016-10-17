#-------------------------------------------------------------------------------
# Name:        Debugging Functions
# Purpose:
#
# Author:      Soribo
#
# Created:     10/12/2010
# Copyright:   (c) Soribo 2010
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


## GetterSetterView ##

def set_variable_list_elements( self, var_list ):
        """ """

        self.delete_variable_list_elements()

        generation_type_cb = wx.ComboBox( self.variable_lc, wx.ID_ANY,
                                          choices = ('Both', 'Getter', 'Setter') )

        for variable in var_list:

            g_copy = generation_type_cb.Copy

            row = wx.ListItem( variable.var_name, variable.data_type, variable.var_value,
                    variable.wrapper_name, g_copy )

            # g_copy.Select( 'Both')

            self.variable_lc.InsertItem( row )



def set_variable_list_elements( self, var_list ):
    """ Post: """

    self.delete_variable_list_elements()

    for variable in var_list:

        gen_type_rb = wx.RadioBox  ( self.variable_lc, -1, "", choices = ('Getter', 'Setter', 'Both'), style = wx.RA_SPECIFY_COLS )

        row_items = ( ULC.UltimateListItem( wx.StaticText( self.variable_lc, -1, variable.var_name     ) ),
                      ULC.UltimateListItem( wx.StaticText( self.variable_lc, -1, variable.data_type    ) ),
                      ULC.UltimateListItem( wx.StaticText( self.variable_lc, -1, variable.var_value    ) ),
                      ULC.UltimateListItem( wx.StaticText( self.variable_lc, -1, variable.wrapper_name ) ),
                      ULC.UltimateListItem( gen_type_rb                                      )  )

        gen_type_rb.Bind( wx.EVT_COMMAND_RADIOBOX_SELECTED, self.on_variable_attrib_change )

        self.variable_lc.CreateListItem( row_items[0], 0 )
        self.variable_lc.CreateListItem( row_items[1], 1 )
        self.variable_lc.CreateListItem( row_items[2], 2 )
        self.variable_lc.CreateListItem( row_items[3], 3 )
        self.variable_lc.CreateListItem( row_items[4], 4 )

        """for item in row_items:

            self.variable_lc.SetItem( item ) """


        """for variable in var_list:

            # self.variable_lc.InsertItem( ULC.UltimateListItem( wx.StaticText( self.variable_lc, -1, variable.data_type    ) ) )
            self.variable_lc.InsertStringItem( 0, variable.var_name, 0 )
            self.variable_lc.InsertStringItem( 1, variable.data_type, 0 )
            self.variable_lc.InsertStringItem( 2, variable.var_value, 0 )
            self.variable_lc.InsertStringItem( 3, variable.wrapper_name, 0 )
            self.variable_lc.InsertStringItem( 4, "NOT IMPLEMENTED", 2 ) """

            # self.variable_lc.Update()


        """ self.variable_lc.InsertItem( ULC.UltimateListItem() )
            self.variable_lc.InsertItem( ULC.UltimateListItem() )
            timer = self.variable_lc.GetItem(0, 1)
            textctrl = wx.TextCtrl(self.variable_lc, -1, "00:00:00")
            timer.SetWindow(textctrl)
            self.variable_lc.SetItem(timer) """



def on_file_drop_command( self, event ):
        """ """

        evt_type = event.GetEventType()

        # if a file has been dropped onto the input_eb
        if evt_type == wx.wxEVT_DROP_FILES:

            file_name = event.GetFiles()[0]


        self.controller.window_proc( GS_INPUT_CHANGE, file_name )




### GetterSetterGlobal ##

## Language Class ##

class Language:

    ## Class Variables: ##

    # self.wrapper_tags
    # self.strt_declaration_tag
    # self.end_declaration_tag
    # self.comment_tag
    # self.comment_blk_strt_tag
    # self.comment_blk_end_tag
    # self.quotation_type_tags
    # self.data_type_tags
    # self.variable_name_index


    ## Class Functions: ##

    def __init__( self, _wrapper, _strt_dec, _end_dec, _comment, _comment_blk_strt, _comment_blk_end, _quotation_type, _data_types, _var_name_index ):
        " Default Constructor: "

        self.wrapper_tags         = _wrapper
        self.strt_declaration_tag = _strt_dec
        self.end_declaration_tag  = _end_dec
        self.comment_tag          = _comment
        self.comment_blk_strt_tag = _comment_blk_strt
        self.comment_blk_end_tag  = _comment_blk_end
        self.quotation_type_tags  = _quotation_type
        self.data_type_tags       = _data_types
        self.variable_name_index  = _var_name_index



## Static Constant Language Objects ##
CPLUSPLUS = Language( _wrapper          = ('class', 'struct'),
                      _strt_dec         =  '{',
                      _end_dec          = ('~~'),
                      _comment          =  '//',
                      _comment_blk_strt =  '/*',
                      _comment_blk_end  =  '*/',
                      _quotation_type   = ('"', ),
                      _data_types       = ('bool', 'char', 'int', 'long',
                                           'short', 'string', 'float',
                                           'UINT', 'POINT'),
                      _var_name_index   =  0 )

JAVA      = Language( _wrapper          = ('class', ),
                      _strt_dec         =  '{',
                      _end_dec          = ('~~'),
                      _comment          =  '//',
                      _comment_blk_strt =  '/*',
                      _comment_blk_end  =  '*/',
                      _quotation_type   = ('"', "'"),
                      _data_types       = ('boolean', 'char', 'int', 'long',
                                           'double', 'String', 'float',
                                           'byte', 'Integer'),
                      _var_name_index   =  1 )

PYTHON    = Language( _wrapper          = ('class', ),
                      _strt_dec         =  ':',
                      _end_dec          = ('~~', ),
                      _comment          =  '#',
                      _comment_blk_strt =  '"""',
                      _comment_blk_end  =  '"""',
                      _quotation_type   = ('"', "'"),
                      _data_types       = ('self.', ),
                      _var_name_index   =  0 )



## GetterSetterVariable ##


# Enum Variable Data Types
INTEGER = 20000
FLOAT   = 20001
SHORT   = 20002
LONG    = 20003
DOUBLE  = 20004
CHAR    = 20005
STRING  = 20006
CUSTOM  = 20007



## GetterSetterModel ##

def reverse( self, _list ):
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


    def format_code( self, file_content ):
        """ Post: """

        # for every '{' put a space on either side of it
        # for every '}'
        #     if the next char == ';' put a space on the left
        #     & a space after the colon!
        #     else place a space on the left & right
        # for every '=' & ',' add a space before & after
        # for every ';' ONLY add a space AFTER!!!

        file_content = self.remove_superficial_code( file_content )


        # file_content = file_content.replace( '};', '~~\n' )
        # file_content = file_content.replace( ';',  ' ;\n' )
        # file_content = file_content.replace( '}',  ' }\n' )
        file_content = file_content.replace( ',',  ', '  )
        file_content = file_content.replace( '};', '??\n' )
        file_content = file_content.replace( '{',  ' {\n' )
        file_content = file_content.replace( '(',  '( '   )
        file_content = file_content.replace( ')',  ' )'   )
        file_content = file_content.replace( ':',  ' : '  )
        file_content = file_content.replace( '=',  ' = '  )
        file_content = file_content.replace( '.',  '. '   )
        file_content = file_content.replace( '~',  '!'   )


        # Mark the end of each classes declaration
        # Place a "~~" at the end of every class decaration
        if self.sel_language == PYTHON:

            file_content = self.catalog_end_of_class_ex( file_content )
            print "isPython should have finished & returned formatted code"

        else:

            if self.sel_language == JAVA:
                end_dec   = '}'
                end_chars = ('}', '~~')
            else:
                end_dec   = '??'
                end_chars = ('}', '??', '~~')

            for wrapper_type in self.sel_language.wrapper_tags:

                file_content = self.catalog_end_of_class( file_content, wrapper_type,
                                                          end_dec, end_chars )


        return file_content



    def remove_superficial_code( self, file_content ):
        """ Post: Identify & remove all code that is unrelated to a
                  wrapper(class)'s definition from file_content &
                  return file_content

                  This function is rather exceptional because its code is
                  broad & stable enough to identify & remove comments & strings
                  regardless of the programming language the file contents
                  are composed of.  """


        start_index          = 0
        end_index            = 0
        open_bracket_num     = file_content.count( '(' )
        open_arrow_num       = file_content.count( '<' )
        closed_arrow_num     = file_content.count( '>' )
        comment_num          = file_content.count( self.sel_language.comment_tag )
        comment_blk_strt_num = file_content.count( self.sel_language.comment_blk_strt_tag )
        comment_blk_end_num  = file_content.count( self.sel_language.comment_blk_end_tag  )


        if self.sel_language  ==  PYTHON:

            str_dec_len = 3

        else:
            str_dec_len = 2


        print "Comment = " + self.sel_language.comment_tag
        print "Comment strt = " + self.sel_language.comment_blk_strt_tag
        print "Comment end = " + self.sel_language.comment_blk_end_tag
        print "Comments identified: " + str(comment_num)
        print "Comment Blk start identified: " + str(comment_blk_strt_num)
        print "Comment Blk end identified: " + str(comment_blk_end_num)
        print "Num of open brackets: " + str( file_content.count( '{' ) )
        print "Num of close brackets: " + str( file_content.count( '}' ) )



        # Delete all comment blocks from code
        if comment_blk_strt_num  ==  comment_blk_end_num:

            for comment_block in range(comment_blk_strt_num):


                start_index = file_content.find( self.sel_language.comment_blk_strt_tag, start_index     )
                end_index   = file_content.find( self.sel_language.comment_blk_end_tag,  start_index + 1 )

                if end_index == -1:

                    break

                # file_content = file_content.replace( file_content[start_index : end_index], "\n COMMENT BLOCK REMOVED \n") # start_index, end_index
                # file_content = file_content[ 0:start_index ] + "\n COMMENT BLOCK REMOVED \n" + file_content[ end_index + str_dec_len:len(file_content) ]
                file_content = file_content[ 0:start_index ] + "\n ; \n" + file_content[ end_index + str_dec_len:len(file_content) ]



        # Delete all comments from code
        start_index = 0
        end_index   = 0

        for comment in range(comment_num):


            start_index = file_content.find( self.sel_language.comment_tag, start_index )
            end_index   = file_content.find( "\n", start_index )

            if end_index == -1:

                break

            # file_content = file_content.replace( file_content[start_index : end_index], "\n COMMENT LINE REMOVED \n")
            # file_content = file_content[ 0:start_index ] + "\n COMMENT LINE REMOVED \n" + file_content[ end_index:len(file_content) ]
            file_content = file_content[ 0:start_index ] + "\n ; \n" + file_content[ end_index:len(file_content) ]




        # Delete all strings from code
        start_index = 0
        end_index   = 0

        for quotation_mark in self.sel_language.quotation_type_tags:

            string_num = int( floor( file_content.count(quotation_mark) / 2 ) )
            start_index = 0
            end_index   = 0

            for string in range( string_num ):

                start_index = file_content.find( quotation_mark, start_index )
                end_index   = file_content.find( quotation_mark, start_index + 1 )

                if end_index != -1:

                    # file_content = file_content.replace( file_content[start_index : end_index], "STRING REMOVED" )
                    file_content = file_content[ 0:start_index ] + "STRING REMOVED" + file_content[ end_index + 1:len(file_content) ]



        # Delete all whitespace before an open bracket
        start_index = 0
        end_index   = 0

        for open_bracket in range(open_bracket_num):

            start_index = file_content.find( '(', start_index )
            x           = start_index - 1

            try:
                while file_content[ x ]  ==  ' '  or  file_content[ x ]  ==  '\t'  or  file_content[ x ]  ==  '\r':

                    # del file_content[ x ]
                    # OR
                    file_content  = file_content[ 0 : x ] + file_content[ x + 1 : len(file_content) ]
                    x  -= 1


            except IndexError:

                print "Index error thrown"
                pass

            start_index = x + 2



        # Delete all whitespace before a comma
        start_index = 0
        end_index   = 0

        for open_bracket in range(open_bracket_num):

            start_index = file_content.find( ',', start_index )
            x           = start_index - 1

            try:
                while file_content[ x ]  ==  ' '  or  file_content[ x ]  ==  '\t'  or  file_content[ x ]  ==  '\r':

                    # del file_content[ x ]
                    # OR
                    file_content  = file_content[ 0 : x ] + file_content[ x + 1 : len(file_content) ]
                    x  -= 1


            except IndexError:

                print "Index error thrown"
                pass

            start_index = x + 2


        return file_content



    def catalog_end_of_class_ex( self, code_str ):
        """ Post: Identify & mark the 'end of class declaration' for
                  each python class in python code """

        sel_class = -1
        end_index = 0
        class_num = code_str.count( 'class' )


        for x in range( class_num ):

            sel_class     = code_str.find ( 'class', sel_class + 1 )
            class_strt    = code_str.rfind( '\n', 0, sel_class )
            print "class_strt= " + str(class_strt)
            target_indent = self.get_indentation( self.get_nxt_line(code_str, class_strt)[0] )
            print "2"
            end_index     = self.get_nxt_line(code_str, class_strt)[1]


            while (True):
                print "3"
                nxt_line_data = self.get_nxt_line( code_str, end_index )
                nxt_line      = nxt_line_data[0]
                end_index     = nxt_line_data[1]

                if ( end_index >= len(code_str) ):

                    code_str += "\n~~\n"
                    break

                elif ( self.is_blank_line( nxt_line ) == False  and  self.get_indentation(nxt_line) <= target_indent ):

                    prev_index = code_str.rfind('\n', 0, end_index-2)
                    code_str   = code_str[0 : prev_index+1] + "\n~~\n" + code_str[prev_index+1 : len(code_str)]
                    break


        return code_str



    def catalog_end_of_class( self, code_str, wrapper_name, end_dec, end_chars ):
        """ """

        end_len   = 2
        sel_class = -1
        wrap_num  = code_str.count( wrapper_name )

        # HACK
        if self.sel_language == JAVA:

            end_len = 1


        while wrap_num > 0:

            sel_class  = code_str.find( wrapper_name, sel_class+1 )
            nxt_end    = code_str.find( end_dec,      sel_class+1 )
            open_count = 0
            end_count  = 0


            while True:

                open_count = code_str.count( '{', sel_class, nxt_end+end_len )
                end_count  = 0

                for char in end_chars:

                    c = code_str.count( char, sel_class, nxt_end+end_len )
                    if c > 0:
                        end_count += c


                if end_count == open_count:

                    # print "Found end: " + str(open_count) + ", " + str(end_count)
                    code_str  = code_str[0 : nxt_end] + '\n~~\n' + code_str[nxt_end+end_len : len(code_str)]
                    wrap_num -= 1
                    break

                else:

                    print str(open_count) + ", " + str(end_count)
                    nxt_end = code_str.find( end_dec, nxt_end + end_len, len(code_str) )
                    if nxt_end < 0:
                        print "File incorrectly formatted"
                        return code_str  # None


        return code_str



    def get_nxt_line( self, code_str, begin_index ):
        """ Post: Identify the next 2 endline characters & return the
                  text in between these 2 characters """

        endln_pos = [ begin_index - 1, -1, -1 ]

        for i in range( 2 ):

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



    def validate_code( self ):
        """ Post: """

        content               = self.format_code( self.input_contents )
        # content             = self.input_contents
        wrapper_count         = 0
        end_declaration_count = 0


        """for wrapper_type in self.sel_language.wrapper_tags:

            count = content.count( wrapper_type )

            if count >= 0:

                wrapper_count += count

        for end_dec in self.sel_language.end_declaration_tag:

            count = content.count( end_dec )
            print "End_dec = " + end_dec + ", " + str(count)

            if count >= 0:

                end_declaration_count += count

        print wrapper_count
        print end_declaration_count

        if wrapper_count <= 0:

            self.app_window.show_error_dialog( "There were no wrappers(classes) identified in input file" )
            return None

        # if there are more wrappers than end declarations then the
        # file is incorectly formatted
        elif wrapper_count != end_declaration_count:
            ##elif wrapper_count > end_declaration_count  or  wrapper_count < end_declaration_count :

            self.app_window.show_error_dialog( "File contents(Source Code) is incorrectly formatted: number of wrappers to end declarations is not equal" )
            return None"""


        # if there are more wrappers than end declarations then the
        # file is incorectly formatted
        """if class_count + struct_count > end_declaration_count:

            self.app_window.show_error_dialog( "File contents(Source Code) is incorrectly formatted: More wrappers than end declarations" )
            return None

        elif class_count == 0  and  struct_count == 0:

            self.app_window.show_error_dialog( "There were no wrapper member variables identified in input file" )
            return None"""


        """

        # Optionally extract class & struct definitions & throw away includes
        # & other junk

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


        content = content.rpartition( self.sel_language.end_declaration_tag )[0] + self.sel_language.end_declaration_tag

        """

        content = content.split()                 # Split into list of words
        content = self.reverse( content )         # Reverse list

        return content



## Start Extract Wrappers/Variables Implementation ##



    def extract_wrappers_ex( self, code_str, wrapper_list, begin_index, wrapper, end_dec ):
        """ Pre:  code_str must be formatted to remove comments & strings
            Post: Recursively identify & store all wrappers in code_str """

        wrapper_num = code_str.count( wrapper )

        ## while ( True ):
        while wrapper_num > 0:

            strt_wrap = code_str.find( wrapper, begin_index )
            end_wrap  = code_str.find( end_dec, strt_wrap+1 )
            nxt_wrap  = code_str.find( wrapper, strt_wrap+1 )

            if nxt_wrap <= -1:

                nxt_wrap = 999999


            if nxt_wrap <= end_wrap:

                data         = self.extract_wrappers_ex( code_str, wrapper_list, nxt_wrap, wrapper, end_dec )
                wrapper_list = data[0]
                code_str     = data[1]

            elif strt_wrap == -1:

                break

            elif end_wrap > -1:

                try:
                    wrapper_type = code_str[strt_wrap : len(code_str)].split( " ", 1 )[0]
                    wrapper_name = code_str[strt_wrap : len(code_str)].split( " ", 2 )[1]
                    wrapper_dec  = code_str[strt_wrap : end_wrap+2]

                    print "CREATING WRAPPER: dec=" + wrapper_dec + "!!!!!!!!!!!!!!!!!!!!"
                    # raw_input()

                    wrapper_list.append( (wrapper_type, wrapper_name, wrapper_dec) )

                except IndexError:
                    pass

                code_str      = code_str[0 : strt_wrap] + code_str[end_wrap+2 : len(code_str)]
                wrapper_num  -= 1


        return (wrapper_list, code_str)



    def get_next_wrapper( self, content_list, begin_index ):
        """ Post: """

        nxt_wrapper_index     = []
        closest_wrapper_index = 999999

        for wrapper_type in self.sel_language.wrapper_tags:

            try:
                wrapper_index = content_list.index( wrapper_type, begin_index )

                if ( wrapper_index < 0 ):

                    wrapper_index = 999999
            except Exception:
                wrapper_index = 999999

            nxt_wrapper_index.append( wrapper_index )


        # Find the closest wrapper to begin_index
        for wrapper_pos in nxt_wrapper_index:

            if wrapper_pos < closest_wrapper_index:

                closest_wrapper_index = wrapper_pos


        return closest_wrapper_index



    def get_next_character_index( self, character_list, content_list, begin_index ):
        """ Post: """

        nxt_char_index     = []
        closest_char_index = 999999

        for character in character_list:

            try:
                char_index = content_list.index( character, begin_index )

                if ( char_index < 0 ):

                    char_index = 999999
            except Exception:
                char_index = 999999

            nxt_char_index.append( char_index )


        # Find the closest character to begin_index
        for char_pos in nxt_char_index:

            if char_pos < closest_char_index:

                closest_char_index = char_pos

        # OR just use the builtin function min
        # closest_char_index = min( nxt_char_index )

        return closest_char_index



    def extract_wrappers( self, content_list ):
        """ Post: """

        wrapper_list           =  []
        wrapper_count          =  0
        wrapper_skip           =  0
        open_declaration_skip  =  1
        close_declaration_skip =  0
        sel_wrapper            = -1
        nxt_wrapper            =  0
        nxt_open_declaration   =  0
        nxt_end_declaration    =  0


        # Calculate how many wrappers exist in code
        for wrapper_type in self.sel_language.wrapper_tags:

            sel_wrapper_num = content_list.count( wrapper_type )
            print "SEL Wrapper count: " + str(sel_wrapper_num)
            print wrapper_type
            if sel_wrapper_num > 0:
                wrapper_count += sel_wrapper_num

        print "Wrapper count: " + str(wrapper_count)
        while wrapper_count > 0:

            sel_wrapper         = -1

            for x in range( wrapper_skip ):

                try:
                    sel_wrapper = self.get_next_character_index( self.sel_language.wrapper_tags, content_list, sel_wrapper + 1)
                    # sel_wrapper = self.get_next_wrapper( content_list, sel_wrapper + 1)
                    # sel_wrapper = content_list.index( self.sel_language.wrapper_tags[0], sel_wrapper + 1 )
                except Exception:
                    sel_wrapper = len( content_list )

                try:
                    nxt_wrapper = self.get_next_wrapper( content_list, sel_wrapper + 1)
                except Exception:
                    nxt_wrapper = 999999


            nxt_open_declaration  = sel_wrapper
            nxt_close_declaration = sel_wrapper


            for x in range( open_declaration_skip ):

                try:
                    nxt_open_declaration = content_list.index( self.sel_language.strt_declaration_tag, nxt_open_declaration + 1 )
                except Exception:
                    nxt_open_declaration = 999999



            for x in range( close_declaration_skip ):

                try:
                    nxt_close_declaration = self.get_next_character_index( self.sel_language.end_declaration_tag, content_list, nxt_close_declaration )
                    # nxt_close_declaration = content_list.index( self.sel_language.end_declaration_tag, nxt_close_declaration )
                except Exception:
                    nxt_close_declaration = 999999


            """if nxt_open_declaration >= nxt_wrapper  and nxt_open_declaration >= nxt_close_declaration:

                print "\n"
                print content_list[ sel_wrapper : nxt_open_declaration ]

            elif nxt_close_declaration >= nxt_wrapper  and nxt_close_declaration >= nxt_open_declaration:

                print "\n"
                print content_list[ sel_wrapper : nxt_close_declaration ]

            elif nxt_wrapper >= nxt_close_declaration  and nxt_wrapper >= nxt_open_declaration:

                print "\n"
                print content_list[ sel_wrapper : nxt_wrapper ] """


            if nxt_open_declaration < nxt_wrapper:

                print "Deleted open & close bracket"
                #for i in range(100000000):
                #    pass

                # del content_list[ nxt_open_declaration  ]
                # del content_list[ nxt_close_declaration ]
                open_declaration_skip  += 1
                close_declaration_skip += 1

            elif nxt_wrapper < nxt_open_declaration:

                print "Found a nested class"
                #for i in range(100000000):
                #    pass

                wrapper_skip += 1

            elif nxt_close_declaration < nxt_wrapper  and  nxt_close_declaration < nxt_open_declaration:

                wrapper_name        = content_list[ sel_wrapper + 1 ]
                wrapper_type        = content_list[ sel_wrapper ]
                wrapper_declaration = content_list[ sel_wrapper + 1 : nxt_close_declaration ]
                wrapper_list.append( (wrapper_type, wrapper_name, wrapper_declaration) )

                print "Found class: name = " + wrapper_name
                print "Deleting this: "
                print content_list[ sel_wrapper : nxt_close_declaration + 1 ]
                del content_list[ sel_wrapper : nxt_close_declaration + 1 ]

                if wrapper_skip > 0:

                    wrapper_skip -= 1


                open_declaration_skip   = 1
                close_declaration_skip  = 0
                wrapper_count          -= 1

            else:
                print "Didn't meet any criteria"


        return wrapper_list



    def java_extract_wrappers( self, content_list ):
        """ Post: """

        wrapper_list      = []
        class_count       = content_list.count( 'class' )
        class_skip        = 0
        sel_class         = -1
        nxt_class         = 0
        nxt_open_bracket  = 0
        nxt_close_bracket = 0


        while class_count > 0:

            sel_class         = -1

            for x in range( class_skip ):

                sel_class = content_list.index( 'class', sel_class + 1 )

                try:
                    nxt_class = content_list.index( 'class', sel_class + 1 )
                except Exception:
                    nxt_class = 99999


            try:
                nxt_open_bracket = content_list.index( '{', sel_class        )
                nxt_open_bracket = content_list.index( '{', nxt_open_bracket + 1 )
            except Exception:
                nxt_open_bracket = 99999


            try:
                nxt_close_bracket = content_list.index( '}', sel_class )
            except Exception:
                nxt_close_bracket = 99999


            if nxt_open_bracket >= nxt_class  and nxt_open_bracket >= nxt_close_bracket:

                print "\n"
                print content_list[ sel_class : nxt_open_bracket ]

            elif nxt_close_bracket >= nxt_class  and nxt_close_bracket >= nxt_open_bracket:

                print "\n"
                print content_list[ sel_class : nxt_close_bracket ]

            elif nxt_class >= nxt_close_bracket  and nxt_class >= nxt_open_bracket:

                print "\n"
                print content_list[ sel_class : nxt_class ]


            if nxt_open_bracket < nxt_class:

                print "Deleted open & close bracket"
                #for i in range(100000000):
                #    pass

                del content_list[ nxt_open_bracket  ]
                del content_list[ nxt_close_bracket ]

            elif nxt_class < nxt_open_bracket:

                print "Found a nested class"
                #for i in range(100000000):
                #    pass

                class_skip += 1

            elif nxt_close_bracket < nxt_class  and  nxt_close_bracket < nxt_open_bracket:

                wrapper_name        = content_list[ sel_class + 1 ]
                wrapper_type        = "class"
                wrapper_declaration = content_list[ sel_class + 1 : nxt_close_bracket ]
                wrapper_list.append( (wrapper_type, wrapper_name, wrapper_declaration) )

                print "Found class: name = " + wrapper_name
                print "Deleting this: "
                print content_list[ sel_class : nxt_close_bracket + 1 ]
                del content_list[ sel_class : nxt_close_bracket + 1 ]

                if class_skip > 0:

                    class_skip -= 1

                class_count -= 1

            else:
                print "Didn't meet any criteria"
                """for i in range(100000000):
                    pass"""



        return wrapper_list



    def recursive_extract_wrappers( self, content_list, abstraction_degree, wrapper_list ):
        """ """

        wrapper_count = content_list.count( self.sel_language.end_declaration_tag )

        # while ( True ):
        # while ( wrapper_count > 0 ):  # in order to use this you need to put wrapper_count -= 1 at the bottom of loop
        while ( content_list.count(self.sel_language.end_declaration_tag) > 0 ):

            last_end_declaration = -1


            for i in range( abstraction_degree ):

                try:
                    end_declaration_pos     = content_list.index( self.sel_language.end_declaration_tag, last_end_declaration + 1, len(content_list) )
                except ValueError:
                    end_declaration_pos     = -1

                try:
                    nxt_end_declaration_pos = content_list.index( self.sel_language.end_declaration_tag, end_declaration_pos  + 1, len(content_list) )
                except ValueError:
                    nxt_end_declaration_pos = -1

                last_end_declaration    = end_declaration_pos


            if end_declaration_pos < 0:

                break


            bracket_pos  = content_list.index( '{', end_declaration_pos )
            wrapper_type = content_list[ bracket_pos + 2 ]


            if bracket_pos > nxt_end_declaration_pos  and  nxt_end_declaration_pos >= 0:

                data = self.recursive_extract_wrappers( content_list,
                                                        abstraction_degree + 1,
                                                        wrapper_list )

                content_list = data[0]
                wrapper_list = data[2]


            elif wrapper_type == 'class'  or  wrapper_type == 'struct':

                wrapper_name        = content_list[ bracket_pos + 1 ]
                wrapper_declaration = self.reverse (  content_list[ end_declaration_pos : bracket_pos ] )
                wrapper_list.append( (wrapper_type, wrapper_name, wrapper_declaration) )

                del content_list[ end_declaration_pos : bracket_pos + 3 ]

            else:

                if content_list[ bracket_pos + 1 ] == '=':

                    del content_list[ end_declaration_pos : bracket_pos + 4 ]

                else:
                    del content_list[ end_declaration_pos : bracket_pos + 3 ]


        return (content_list, abstraction_degree, wrapper_list)



    def extract_variables_ex( self, wrapper_list ):
        """ Post: """

        variable_list  = []


        for wrapper in wrapper_list:

            wrapper_name        = wrapper[1]
            wrapper_declaration = wrapper[2]

            for data_type in self.sel_language.data_type_tags:

                data_type_index = -1

                while ( wrapper_declaration.count(data_type) > 0 ):

                    try:

                        data_type_index = wrapper_declaration.index( data_type, data_type_index + 1 )
                        var_type_index  = data_type_index + self.sel_language.variable_name_index

                        var_type        = wrapper_declaration[ var_type_index ]
                        var_name        = wrapper_declaration[ var_type_index + 1 ].replace( ';', '' )
                        var_value       = 0


                        # Make sure we have a variable & not a function
                        if not var_name.endswith( ')' )  and not  '(' in var_name  and  var_name.isalnum():

                            variable_list.append( Variable.Variable( var_name, var_type,
                                                                     0, wrapper_name,
                                                                     Variable.BOTH ) )


                    except IndexError:

                        # self.app_window.show_error_dialog( "Attempting to acces a character index that is greater than the strings length" )
                        pass

                    finally:

                        del wrapper_declaration[ data_type_index ]
                        var_name        = "NULL"
                        var_type_index  = 0



        print str(len(variable_list))
        return variable_list



    def extract_variables( self, wrapper_list ):
        """ Post: """

        variable_list  = []


        for wrapper in wrapper_list:

            for data_type in self.sel_language.data_type_tags:

                while ( wrapper[2].count(data_type) > 0 ):

                    try:

                        var_type_index = wrapper[2].index( data_type )
                        var_name_index = var_type_index + 1

                        var_name       = wrapper[2][ var_name_index ].replace(';','')

                        # What about arrays, I need to identify if there is an [] in var_name then change var_type to 'int[]' from 'int'

                        # Make sure we have a variable & not a function
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

        print str(len(variable_list))
        return variable_list



    def get_var_declaration( self, var_dec, var_pos ):
        """ """

        try:

            print "dec_strt= %s, dec_end= %s " % (str(var_dec.rfind( ';', 0, var_pos )), str(var_dec.find( ';', var_pos, len(var_dec) )))
            dec_strt = var_dec.rindex( ';', 0, var_pos )
            dec_end  = var_dec.index( ';', var_pos, len(var_dec) )

            return var_dec[dec_strt : dec_end+1]

        except ValueError:

            print "<get_var_declariont>Error: ValueError"

        except Exception:

             print "<get_var_declariont>Error: Unknown Exception"

        return None



    def format_var( self, var_str ):
        """ """

        delim = ( '/t', '\r', '\n', '\v', ';', '~~', ' ' )

        for char in delim:

            var_str = var_str.replace( char, '' )

        return var_str



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



    def extract_variables_exx( self, wrapper_list ):
        """ """

        var_list  = []
        var_types = self.sel_language.data_type_tags

        for wrapper in wrapper_list:

            print "\nSEARCHING %s for variables" % wrapper[1]
            if wrapper[1] == "ubCell":
                print wrapper[2]

            wrapper_name = wrapper[1]
            wrapper_dec  = "; " + wrapper[2] + " ;"

            for data_type in var_types:

                while wrapper_dec.count( data_type ) > 0:

                    var_pos = wrapper_dec.find( data_type )
                    var_dec = self.get_var_declaration( wrapper_dec, var_pos )

                    if var_dec == None:
                        print "\nBREAKING\n"
                        break

                    # if not a function
                    if var_dec.count('(') <= 0:

                        var_data  = self.get_var_data( var_dec )
                        var_names = var_data[0]
                        var_type  = var_data[1]

                        for name in var_names:

                            print "Var name= " + self.format_var( name )
                            print "Var type= " + self.format_var( var_type )
                            print "Owner class= " + self.format_var( wrapper_name )
                            var_list.append( Variable.Variable( name, var_type,
                                                                0, wrapper_name,
                                                                Variable.BOTH ) )

                    wrapper_dec = wrapper_dec.replace( var_dec.replace(';',''), '' )


        return var_list



    ## End Extract Wrappers/Variables Implementation ##





