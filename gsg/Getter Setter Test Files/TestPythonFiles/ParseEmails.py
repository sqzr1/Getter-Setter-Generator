

## Constants ##
solved_problems = []


class SolvedProblem:
    """ """

    
    def __init__( self, problem_tags ):
        """ Default Constructor: """

        self.problem_tags = problem_tags


    def get_relation( tag_list ):
        """ Post: """

        hit_rate = 0
        
        for tag in tag_list:

            #if not self.problem_tags.index( tag ) == None:
            if not self.problem_tags.index( tag ) == -1:

                hit_rate += 1


        return hit_rate



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




b = "  A B C D A D E F G H B"

a = parse_email_contents( b, ignore_common_words = True )
c = get_frequent_terms( a, 9 )


print c
