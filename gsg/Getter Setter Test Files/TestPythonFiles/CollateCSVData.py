import csv
import os, fnmatch


class Order:

    def __init__( self, row_data ):
        """ """

        self.name       = row_data[0]
        self.part_num   = []
        self.part_des   = []
        self.quantity   = []
        self.value      = []
        self.part_total = []
        self.total      = 0

        self.add_data( row_data )


    def add_data( self, row_data ):
        """ """

        try:
            
            self.part_num   .append( row_data[1] )
            self.part_des   .append( row_data[2] )
            self.quantity   .append( self.convert_to_decimal( row_data[3] ) )
            self.value      .append( self.convert_to_decimal( row_data[4] ) )
            self.part_total .append( self.quantity[-1] * self.value[-1] )
            self.total     += self.part_total[-1]

        except (SyntaxError, OverflowError, NameError, TypeError):

            return

    def cal_total( self ):

        self.total = 0
        
        for part_total in self.part_total:

            self.total += part_total

        return self.total

    def display_content( self ):
        """ """
        print "\n\nOrder Name: " + self.name

        for i in range( len(self.part_num) ):

            try:
                print "Order part: " + self.part_num[i] + "      Order des: " + self.part_des[i]
                print "Part Quantity: " + str(self.quantity[i]) + "      Part Value: $" + str(self.value[i])
                print "Part Total: $" + str(self.part_total[i])
                #print ""

            except (SyntaxError, OverflowError, NameError, TypeError):

                print "A part has some values undefined"

        print "Order Total: $" + str( self.total )
        print "\n\n"


    def to_string( self ):
        """ """

        part_data = [ self.part_num, self.part_des,  self.quantity,
                      self.value,    self.part_total ]
        result    = self.name + '\n'

        for i in range( len(self.part_num) ):

            for j in range( len(part_data) ):
                
                try:
                    
                    result += str(part_data[j][i]) + ','
                    
                except (SyntaxError, OverflowError, NameError, TypeError):

                    result += 'undefined,'

            result += '\n'

        result += str(self.total) + '\n'


        return result



    def to_string_ex( self ):
        """ """

        part_data = [ self.part_num, self.part_des,  self.quantity,
                      self.value,    self.part_total ]
        result    = ""

        for i in range( len(self.part_num) ):

            result += self.name + ','

            for j in range( len(part_data) ):
                
                try:
                    
                    result += str(part_data[j][i]) + ','
                    
                except (SyntaxError, OverflowError, NameError, TypeError):

                    result += 'undefined,'

            result += str(self.total) + '\n'


        return result

        

    def convert_to_decimal( self, n ):

        try:

            if n.isdigit():

                res = int(n)

        except (ValueError):

            res = float(n)

        except (Exception):

            res = n

        return res

    

def read_csv_file( in_file ):
    """ """

    try:

        file = open( in_file, 'r' )

        text = file.readlines()

        file.close()

        return text[ 1 : len(text) ]

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

        print( "Error opening file\n" + str(error) )
        return None

    except UnicodeDecodeError, error:

        print( "Cannot open non ascii files\n" + str(error) )
        return None

    except TypeError, error:

        print( "Invalid file type: \n" + str(error) )
        return None



def write_csv_file( out_file, order_dict ):
    """ """

    try:

        if not out_file.endswith( ".csv" ):

            out_file += ".csv"

        
        file    = open( out_file, 'w' )
        content = "Order,Part Num,Part Description,Quantity,Value,Part Total,Order Total,\n"
        
        for order in order_dict.values():
            
            content += order.to_string_ex()

        file.write( content )

        file.close()


    except IOError, error:

        print( "Error creating file\n" + str(error) )
        return None

    except UnicodeDecodeError, error:

        print( "Cannot write to non ascii files\n" + str(error) )
        return None

    except TypeError, error:

        print( "Invalid file type: \n" + str(error) )
        return None

    
    
def extract_orders( content ):
    """ """

    #content    = csv.reader( open(file_name, 'rb'), dialect="excel",
    #                             delimiter=' ', quotechar='|')
    order_dict = {}
    header     = True

    for row in content:

        row = row.split( ',' )
        # print row

        if len( row ) < 4:

            pass
        
        elif order_dict.has_key( row[0] ):

            order_dict[ row[0] ].add_data( row )

        else:

            if row[0].isalnum():
                order_dict[ row[0] ] = Order( row )


    return order_dict

        

def get_orders_in_range( _min, _max, order_dict ):
    """ """

    result = {}

    for key in order_dict:

        order_price = order_dict[ key ].cal_total()

        if order_price >= _min  and  order_price <= _max:

            result[ key ] = order_dict[ key ]


    return result



def display_valid_orders( order_dict ):
    """ """

    if len( order_dict ) <= 0:

        print "\nNo orders met the range criteria\n"

        
    for order in order_dict.values():

        order.display_content()



def take_decimal_input( _str, _max ):

    valid_input = False
    
    while not valid_input:
        try:

            result      = input( _str )

            if ( result <= _max ):
                valid_input = True

        except (SyntaxError, OverflowError, NameError, TypeError):
            print "\n*** Incorrect input *** \n"

    return result


def take_alpha_input( _str ):

    valid_input = False
    
    while not valid_input:
        try:

            result      = raw_input( _str )
            valid_input = True

        except (SyntaxError, OverflowError, NameError, TypeError):
            print "\n*** Incorrect input *** \n"

    return result



def identify_csv_files():

    '''Locate all files matching supplied filename pattern in and below
       supplied root directory. pattern, root=os.curdir'''

    dirList   = os.listdir( os.curdir )
    file_list = []
    index     = 1

    print "Identifing CSV files in directory: \n"
    
    for fname in dirList:

        if fname.endswith( ".csv" ):
            
            print str(index) + ". " + fname
            file_list.append( fname )
            index += 1

    if len( file_list ) > 0:
        file_index = take_decimal_input( "Please select a file to query: ", index-1 )
        result     = file_list[ file_index-1 ]

    else:
        print "No csv files in directory. Please place a file in the directory this application is in & rerun the program"
        result = None


    return result



def main():
    """ """

    # identify all csv files in directory
    # print open("Test Data MelAzzopardi.xlsx").decode('utf-16').read().replace("\0", ">>>NUL<<<")


    in_file = identify_csv_files()

    if in_file == None:

        raw_input( "" )
        return
    
    minimum = take_decimal_input( "\nPlease enter the minimum total an order can have: ", 999999999999 )
    maximum = take_decimal_input( "Please enter the maximum total an order can have: ", 999999999999 )

    content         = read_csv_file( in_file )
    order_dict      = extract_orders( content )
    in_range_orders = get_orders_in_range( minimum, maximum, order_dict )


    display_valid_orders( in_range_orders )

    if len( in_range_orders ) <= 0:

        raw_input( "" )
        return


    save_results = (take_alpha_input( "Do you wish to save these results to a csv file? (y or n): " )).lower()
    
    if save_results[0] == 'y':

        file_name = take_alpha_input( "Please type a csv file name: " )
        write_csv_file( file_name, in_range_orders )
        print "File successfully created."


    
    raw_input( "" )
    
    



if __name__ == "__main__":

    main()


