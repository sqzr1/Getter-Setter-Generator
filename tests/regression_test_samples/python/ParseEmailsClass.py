"""



"""


## Constants ##

UD_ALL    = 50001
HASH_MULT = 50002
HASH_DIV  = 50003


class Tag:

    ## Class Variables: ##

    # self.name
    # self.code


    ## Class Functions: ##

    def __init__( self, _name, _code ):
        """ Default Constructor: """

        self.name = _name
        self.code = _code



class Solution:

    ## Class Variables: ##

    # self.name
    # self.tag_dict
    # self.hash_code
    # self.hash_equation


    ## Class Functions: ##

    def __init__( self, _name, _related_tag_dict ):
        """ Default Constructor: """

        self.name          = _name
        self.tag_dict      = _related_tag_dict
        self.hash_code     = -1
        self.hash_equation = HASH_MULT

        
        self.update_hash_code( UD_ALL )



    def perform_hash( self, new_value ):
        """ Post: """

        if self.hash_equation == HASH_MULT:

            self.hash_code     = self.hash_code * new_value
            self.hash_equation = HASH_DIV
            
        else:  # hash_equation == HASH_DIV

            self.hash_code     = int(self.hash_code / new_value)
            self.hash_equation = HASH_MULT

        return self.hash_code


            
    def update_hash_code( self, update_type ):
        """ Post: """

        if update_type == UD_ALL:

            self.hash_code = self.tag_dict.values()[0].code
            
            for tag in self.tag_dict.values():

                self.perform_hash( tag.code )
                """
                print "Tag name: " + tag.name
                print "Tag code: " + str(tag.code)
                print "Hash code: " + str(self.hash_code)
                """

        else:

            tag_list      = self.tag_dict.values()
            tag_list_size = len( tag_list )
            tag_index     = tag_list_size - update_type - 1
            
            while ( tag_index < tag_list_size ):

                self.perform_hash( tag_list[ tag_index ].code )
                tag_index += 1



        # return self.hash_code  # May not be necessary


                

        

      

