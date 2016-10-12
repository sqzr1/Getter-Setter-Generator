"""



"""

from random import randint
from ParseEmailsClass import Tag, Solution


## Global Functions ##

def heap_sort(list2):
    first = 0
    last = len(list2) - 1
    create_heap(list2, first, last)
    for i in range(last, first, -1):
        list2[i], list2[first] = list2[first], list2[i]  # swap
        establish_heap_property (list2, first, i - 1)

# create heap (used by heap_sort)
def create_heap(list2, first, last):
    i = last/2
    while i >= first:
        establish_heap_property(list2, i, last)
        i -= 1

# establish heap property (used by create_heap)
def establish_heap_property(list2, first, last):
    while 2 * first + 1 <= last:
        k = 2 * first + 1
        if k < last and list2[k].hash_code < list2[k + 1].hash_code:
            k += 1
        if list2[first].hash_code >= list2[k].hash_code:
            break
        list2[first], list2[k] = list2[k], list2[first]  # swap
        first = k



def closest(target, collection, n_times ) :
    """ Post: """

    closest_solutions = []
    
    for j in range( n_times ):

        i = 0
        closest_solutions.append( min((abs(target - i.hash_code), i.hash_code) for i in collection)[1] )
        del collection[i]
        
    return closest_solutions



def remove_common_words( inverted_index ):

    common_words = ('the', 'is', 'at')

    for word in common_words:

        try:

            # inverted_index.pop( word )
            del inverted_index[ word ]

        except KeyError:

            """ Add this exeption to debugging 'Event Log' """

    return inverted_index



def parse_email_contents( email_content, ignore_common_words ):
    """ Post: """

    inverted_index = {}
    email_content = email_content.lower()

    for word in email_content.split():

        if inverted_index.has_key( word ):

            inverted_index[ word ] += 1;

        else:

            inverted_index[ word ] = 1


    # I could have removed these words from the Str rather than adding them
    # to the inverted index THEN deleting them from the Str BUT I believe
    # it is faster to search for & remove an element from a Dictionary(Map)
    # compared to searching for a wrd in a string then removing it
    if ignore_common_words  ==  True:

        inverted_index = remove_common_words( inverted_index )
    

    return inverted_index



def get_frequent_terms( inverted_index, n_terms ):
    """ Post: """

    frequent_terms = []
    words          = inverted_index.keys()
    word_frequency = inverted_index.values()
    
    while ( n_terms > 0  and len(words) > 0 ):

        wrd_occrnc     = max(word_frequency)

        if wrd_occrnc <= 1:
            break
        
        freq_wrd_index = word_frequency.index( wrd_occrnc )

        frequent_terms.append( words[ freq_wrd_index ] )
        del words[ freq_wrd_index ]
        del word_frequency[ freq_wrd_index ]
        n_terms -= 1

    return frequent_terms



def get_key_terms( inverted_index, n_terms ):
    """ Post: Search for specific key terms that may exist/occur in
              email contents(inverted_index) """

    key_terms = ( 'dvc', 'commbox', 'combox', 'video', 'commander',
                  'lite', 'avbox', 'mkii', 'det', 'joey', 'micro',
                  'micro6', 'digital', 'signage' )

    # I want to find out which key terms if any occur in inverted index
    # I want to find out the n most frequent key terms in inverted index
    # I want to return those n most frequent key terms in a list

        
        

def get_related_problems( frequent_terms, solved_problems, min_hit_rate ):
    """ Post: """

    related_problems = []
    
    for problem in solved_problems:

        hit_rate = problem.get_relation( frequent_terms )

        if ( hit_rate >= min_hit_rate):

            related_problems.append( problem )


    return related_problems




class EmailParser:

    ## Class Variables: ##

    # self.tag_list
    # self.solution_dict

    

    ## Class Functions: ##

    def __init__( self ):
        """ Default Constructor: """

        self.init_variables()

        sol_list = self.solution_dict.values()
        heap_sort( sol_list )

        for sol in sol_list:

            print sol.hash_code


        print "Finding the number closest to 95"
        cloest = closest( 95, sol_list, 5 )

        for sol in cloest:

            print "Solution Name: " + sol.name
            print "Solution Hash: " + str(sol.hash_code)


    def init_variables( self ):
        """ Post: """

        self.tag_list      = []
        self.solution_dict = {}

        # Build some tags & solutions for debugging

        tag_name = "internet"
        sol_name = "blah"
        
        for i in range(30):

            tag_name += str( randint(65,100) )

            self.tag_list.append( Tag( tag_name, i+3 ) )


        sol_num = randint(30,100)
        
        for i in range( sol_num ):

            solution_tags = {}
            sol_tag_size  = randint(5,29)

            for i in range( sol_tag_size ):

                rand_tag = self.tag_list[ randint(0,29) ]
                solution_tags[ rand_tag.name ] = rand_tag

            sol_name += str( randint(65,100) )
            self.solution_dict[ sol_name ] = Solution( sol_name, solution_tags )


        """
        print "\n\n\nPrinting Solution Stats\n\n"
        for solution in self.solution_dict.values():

            print "Solution Name: " + solution.name
            print "Solution Dict: "
            for tag in solution.tag_dict.values():

                print tag.name + ": Code = " + str(tag.code)
            
            print "Solution Hash Code: " + str(solution.hash_code)
        """




if __name__ == "__main__":

    cla = EmailParser()

    """
    a = [ 9, 33, 44, 11, 44, 33 , 66, 88, 9, 3, 2, 6, 7, 0 ]
    heap_sort( a )

    print a
    """

        
