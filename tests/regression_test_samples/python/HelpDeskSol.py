"""

Help Desk Solution Suggester:


IDEA: !!  Have a global dict that contains all problem tags as keys
          & as the values have a pointer to each HelpDeskIssue OR
          ID of each HelpDeskIssue that has that problem tag.

          When I search for related issues I use .has_key() on the
          global dict for each tag inside the target_issue. The
          HelpDeskIssue that has the most hits(same tags) will be the
          suggested solution.

"""


### Globals ###

solution_list = []
problem_dict  = {}



### Classes ###

class HelpDeskSolution:


    def __init__( self, _solution_text ):
        """ """

        self.sol_text = _solution_text

        

class HelpDeskIssue:


    ### Class Static Variables ###
    
    hdissue_instance_count = 0

    
    def __init__( self, _name, _issue_data, _related_solutions ):
        """ """

        HelpDeskIssue.hdissue_instance_count += 1

        self.id                = HelpDeskIssue.hdissue_instance_count
        self.name              = _name
        self.content           = _issue_data
        self.problem_tags      = self.extract_problem_tags( _issue_data )
        self.related_solutions = _related_solutions
        self.hash_value        = self.get_hash_value()

        register_problem_tags( problem_dict, self.problem_tags, self.id )



    def extract_problem_tags( self, email_content ):
        """ """

        word_list = email_content.split() # NEED to split/remove chars ')', ',' etc.
        word_freq = {}
        
        for word in word_list:

            word = word.lower()
            
            if word_freq.has_key( word ):

                word_freq[word] += 1

            else:

                word_freq[word] = 1


        # delete common words from dictionary
        word_freq = self.remove_unrelated_words( word_freq )


        return word_freq


    def remove_unrelated_words( self, word_dict ):
        """ """

        unrel_wrd = [ 'the', 'at', 'a', 'is', 'there', 'that',
                      'and', 'to', 'of', 'or', 'their', 'in',
                      'for', 'with', 'it', 'can', 'many', 'be',
                      'this', 'such' ]


        for word in unrel_wrd:

            if word_dict.has_key( word ):

                del word_dict[word]


        return word_dict



    def get_hash_value( self ):
        """ """

        self.hash_value = 0
        tag_hash        = 0
        
        for tag in self.problem_tags:

            for char in tag:

                tag_hash += ord(char) * 5


            self.hash_value += tag_hash
            tag_hash         = 0


        return self.hash_value



    def to_string( self ):
        """ """

        return "name:     %s\ncontent:  %s\nsolution: %s\n" % ( self.name,
                                                              self.content,
                                                              self.related_solutions )



### Suggest Solution Functions ###

def register_problem_tags( global_tags, subject_tags, subject_id ):
    """ """

    for tag in subject_tags.keys():

        if global_tags.has_key( tag ):

            global_tags[tag].append( subject_id )

        else:

            global_tags[tag] = [ subject_id ]


    return global_tags


def get_related_issues( target_issue, issue_list, n_degree ):
    """ """

    rel_issues   = []
    tar_hash_val = target_issue.get_hash_value()

    for issue in issue_list:

        if abs(tar_hash_val - issue.get_hash_value()) <= n_degree:

            rel_issues.append( issue )


    return rel_issues


def suggest_related_issues( target_issue, issue_list, hit_quota ):
    """ """

    rel_issues        = []
    smallest_tag_dict = None
    largest_tag_dict  = None
    hit_rate          = 0

    for issue in issue_list:

        if len( target_issue.problem_tags ) <= len( issue.problem_tags ):

            smallest_tag_dict = target_issue.problem_tags
            largest_tag_dict  = issue.problem_tags

        else:
            smallest_tag_dict = issue.problem_tags
            largest_tag_dict  = target_issue.problem_tags

        for key in smallest_tag_dict.keys():

            if largest_tag_dict.has_key( key ):

                hit_rate += 1

        if hit_rate >= hit_quota:
            
            rel_issues.append( issue )

        hit_rate = 0


    return rel_issues


def store_related_issues( issue_dict, id_list ):
    """ """

    for issue_id in id_list:

        issue_id = str( issue_id )
        
        if issue_dict.has_key( issue_id ):

            issue_dict[issue_id] += 1

        else:
            
            issue_dict[issue_id]  = 1


    return issue_dict


def vet_issues( related_issues, hit_quota ):
    """ """

    if len( related_issues ) <= 0:

        return {}

    for key,value in related_issues.items():

        if value < hit_quota:

            del related_issues[key]


    return related_issues


def issues_by_id( id_list, issue_list ):
    """ """

    li = []
    
    for id in id_list:

        for issue in issue_list:

            if issue.id == int(id):

                li.append( issue )


    return li


def suggest_related_issues_ex( target_issue, issue_list, global_tags, hit_quota ):
    """ """

    related_issues = {}

    for tag in target_issue.problem_tags.keys():

        if global_tags.has_key( tag ):

            related_issues = store_related_issues( related_issues,
                                                  global_tags[tag] )

    if related_issues.has_key( str(target_issue.id) ):

        del related_issues[str(target_issue.id)]

        
    related_issues = vet_issues( related_issues, hit_quota )


    return issues_by_id( related_issues.keys(), issue_list )
            
    
def parse_line( file_stream ):
    """ """

    content = []
    
    while content == []:

        line = file_stream.readline()

        if line:
            content = line.split()

    return line
        

def parse_solution( file_stream ):
    """ """

    try:

        # .strip( ',()"'''[]?.;\' ) to remove unwanted characters
        sol_name      = parse_line( file_stream ).strip( "name:" ).strip()
        sol_content   = parse_line( file_stream ).strip( "content:" ).strip()
        sol_solutions = parse_line( file_stream ).strip( "solution:" ).strip()
        
        return HelpDeskIssue( sol_name, sol_content, sol_solutions )

    except Exception, error:

        print ".iss file is incorrectly formatted: " + str(error)
        return None


def import_issue_database( db_name ):
    """ """

    issue_list = []
    
    if not db_name.endswith("iss"):

        return issue_list


    try:

        file_stream   = open( db_name, 'r' )
        hd_issue_num  = int ( file_stream.readline().split()[0] )

        for x in range( hd_issue_num ):
            
            hd_issue = parse_solution( file_stream )

            if not hd_issue == None:

                issue_list.append( hd_issue )

        file_stream.close()


    except IOError, error:

        print 'Error opening file\n' + str(error)

    except UnicodeDecodeError, error:

        print 'Cannot open non ascii files\n' + str(error)

    except Exception, error:

        print "Other exception occured\n" + str(error)


    return issue_list


def store_database_issue( db_name, issue ):
    """ """
    
    if not db_name.endswith("iss"):

        return False

    
    try:

        # TODO - Need to change the header line of database file:
        # increase issue count (in header)
        
        file_stream = open( db_name, 'a' )

        file_stream.write( "\n" )
        file_stream.write( issue.to_string() )
        file_stream.write( "\n" )

        file_stream.close()

        return True

    
    except Exception, error:

        print "Other exception occured\n" + str(error) 

        

### Debugging Functions ###

def build_test_issues():
    """ """

    test_issues = []

    names     = ( 'Logoff', 'Insufficient Memory', 'Firewall Breach',
                'Missing Config File' )
    content   = ( """ A help desk is an information and assistance resource that
                      troubleshoots problems with computers or similar products.
                      Corporations often provide help desk support to their customers
                      via a toll-free number, website and/or e-mail. There are also
                      in-house help desks geared toward providing the same kind of
                      help for employees only. Some schools offer classes in which
                      they perform similar tasks as a help desk. In the Information
                      Technology Infrastructure Library, within companies adhering
                      to ISO/IEC 20000 or seeking to implement IT Service Management """,
                  """ A typical help desk has several functions. It provides the users a
                      single point of contact, to receive help on various computer issues.
                      The help desk typically manages its requests via help desk software,
                      such as an issue tracking system, that allows them to track user requests
                      with a unique number. This can also be called a "Local Bug Tracker" or LBT.
                      There are many software applications to support the help desk function. Some
                      are targeting enterprise level help desk (rather large) and some are targeting
                      departmental needs. """,
                  """ The deskside team (sometimes known as "desktop support") is responsible for the
                      desktops, laptops, and peripherals, such as PDAs. The help desk will assign the
                      desktop team the second level deskside issues that the first level was not able
                      to solve. They set up and configure computers for new users and are typically
                      responsible for any physical work relating to the computers such as repairing
                      software or hardware issues and moving workstations to another location. """,
                  """ The network team is responsible for the network software, hardware and infrastructure
                      such as servers, switches, backup systems and firewalls. They are responsible for the
                      network services such as email, file, and security. The help desk will assign the network
                      team issues that are in their field of responsibility """ )
    solutions = ( HelpDeskSolution( "Logoff Sol" ),
                  HelpDeskSolution( "Insufficient Memory Sol" ),
                  HelpDeskSolution( "Firewall Breach Sol" ),
                  HelpDeskSolution( "Missing Config File Sol" ) )


    for i in range( len(names) ):
        
        test_issues.append( HelpDeskIssue( names[i],
                                           content[i],
                                           solutions[i] ) )


    return test_issues



def get_rand_issue():
    """ """

    return HelpDeskIssue( "Test Problem",
                          """ Middleton [1] at Robert Gordon University found
                              through his research that many organizations had begun
                              to recognize that the real value of their help desk(s)
                              derives not solely from their reactive response to users'
                              issues but from the help desk's unique position where it
                              communicates daily with numerous customers or employees.
                              This gives the help desk the ability to monitor the user
                              environment for issues from technical problems to user
                              preferences and satisfaction. Such information gathered
                              at the help desk can be valuable for use in planning and
                              preparation for other units in information technology. """,
                          None )


def get_rand_issue_ex():
    """ """

    issue = HelpDeskIssue( "Test Problem", "", None )

    issue.problem_tags = { 'Issue': 9, 'viral': 9, 'shutdown': 9, 'restart': 9,
                           'recurring': 9, 'windows': 9, 'executable': 9,
                           'symptom': 9, 'process': 9, 'attempt': 9, 'missing': 9,
                           'help': 9, 'information': 9, 'customers': 9, 'problems': 9,
                           'desk': 9 } # issues for logoff

    return issue



def debug_rel_issues( tar_issue, rel_issues ):
    """ """

    for issue in rel_issues:

        print "**Start:"
        
        for key in issue.problem_tags.keys():

            if tar_issue.problem_tags.has_key(key):

                print "Target Issue:    " + key + ": " + str( issue.problem_tags[key] )
                print "Suggested Issue: " + key + ": " + str( tar_issue.problem_tags[key] )

        print "**End \n"



    
def debug_issues( rel_issues ):
    """ """

    template = "Issue Name: %s;  Issue hash: %s "
    
    for issue in rel_issues:

        print template % ( issue.name, str(issue.get_hash_value()) )




### Main Implementation ###
    
def main():
    """ """

    solution_list = import_issue_database( "HelpDeskDatabase.iss" )  # build_test_issues()
    issue         = get_rand_issue_ex()


    rel_issues = suggest_related_issues_ex( issue, solution_list, problem_dict, 5 )

    if len(rel_issues) > 0:

        print "We suggest the following help desk issues are related to your issue:"
        for iss in rel_issues:

            print iss.name


    # store_database_issue( "HelpDeskDatabase.iss", issue )
    

    print "\n\nDebugging: "
    debug_issues( [ issue ] )
    debug_issues( solution_list )

    print "\nWords that occur in both issues: "
    debug_rel_issues( issue, rel_issues )


    raw_input()

    

if __name__ == "__main__":

    main()


