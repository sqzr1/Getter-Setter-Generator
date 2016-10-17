import sqlite3
import os


target_element = {'<body': 'body',
                  '<p'   : 'p',
                  '<div' : 'div',
                  '<a'   : 'a',
                  '<ul'  : 'ul',
                  '<ol'  : 'ol'
                  }

def import_HTML_page(HTML_filename):
    """ Pre:  file_name must be a string with NO file extension defined
        Post: Create a SQLite3 database with a table that will catalog
              all of this websites' HTML elements, ID's & classes. """

    # Create SQLite3 database
    try:
        if '.' in HTML_filename:
            HTML_filename = HTML_filename.split('.')[0]
        """ Create SQLite3 database with same name as file_name """
        if not os.path.isfile(HTML_filename+".db"):
            HTML_filename = HTML_filename+".db"
            conn = sqlite3.connect(HTML_filename)
        else:
            print "Error: "+HTML_filename+" file already exists in this directory."
            #conn = sqlite3.connect(file_name+"1.db")
            return False

        cur = conn.cursor() 
        cur.execute("CREATE TABLE variables IF NOT EXISTS (element varchar, type varchar);")
        conn.commit()
        conn.close()
        return HTML_filename
    
    except (sqlite3.OperationalError, msg):
        print "'import_HTML_page' Function Error: Failed to establish database connection."
        return False

def import_HTML_file(HTML_filename, db_filename):
    """ Pre:  db_filename string must be a SQLite3 database file name
              including path & extension.
        Post: Catalog all HTML & CSS elements in HTML file. Create an
              SQLite3 table for each HTML element. """

    HTML_file   = open(HTML_filename,'r');
    HTML_source = HTML_file.readlines()
    HTML_file.close()

    if not HTML_source==False:

        HTML_source  = format_file(HTML_source)
        catalog_elements(HTML_source)
        catalog_CSS_data(HTML_source)
        updateDatabase(db_filename)
        return True

    else:
        print "'import_HTML_page' Function Error: HTML file is empty or incorrectly formated."
        return False

def format_file(HTML_source):
    """ Post: Correctly format HTML file so we can identify HTML
              elements & CSS elements."""

    # Convert str to list
    HTML_list = list(HTML_source)
    x = 0
    state = '~'

    while x<len(HTML_list):
  
        if state == '<':
            if HTML_list[x] == ' ':
                del HTML_list[x]
                x -= 1
            else:
                state = '~'

        elif state == '=':
            if HTML_list[x] == ' ':
                del HTML_list[x]
                x -= 1
            # Check if element before '=' is a space 
            elif HTML_list[x-2] == ' ':
                del HTML_list[x-2]
                x = x-2
            else:
                state = '~'
            
        elif state == '~':
            if HTML_list[x] == '<':
                state = '<'
            elif HTML_list[x] == '=':
                state = '='

        # Change all single quotes to double quotes
        if HTML_list[x] == "'":
            HTML_list[x] = '"'

        x += 1

    # Convert list to str
    HTML_source = ''.join(HTML_list)
    print "\n '<' Spaces taken out \n\n"
    return HTML_source

def catalog_elements(HTML_source):
    """ Post: Identify all HTML elements including custom classes
              & id's and store their name & type in a list. """

    # identify & separate classes & id's
    class_list = HTML_source.split('class=')
    id_list    = HTML_source.split('id=')

    for string in class_list:
        if string[0] == '"':
            class_name = string.split('"')[1]
            create_object(class_name,"class")

    for string in id_list:
        if string[0] == '"':
            id_name = string.split('"')[1]
            create_object(class_name,"id")

    # identify HTML elements
    for target in target_element:
        if target in HTML_source:
            create_object(target_element[target],target_element[target])
    
def get_css_data(buf, element_list):
    """ Post: Identify all CSS elements including custom classes
              & id's, store their name & type in a list & extract
              element properties & values. """

    remaining_str = buf
    end = False

    while end==False:

        if '{' in remaining_str and '}' in remaining_str:

            tup = get_css_element(remaining_str)
            element_name   = tup[0]
            ele_properties = tup[1]
            remaining_str  = tup[2]
            # create new element object
            sel_element = is_present(element_name)
            if sel_element == None:
                create_object(element_name,"CSS")
                sel_element = self.object_list[-1]
            
            prop_end = False
            
            # get properties
            while prop_end==False:
                if ':' in ele_properties and ';' in ele_properties:

                    tup = get_css_element_properties(ele_properties)
                    property = tup[0]
                    value    = tup[1]
                    ele_properties = tup[2]
                    # add property & value to new_element
                    sel_element.add_attribute(property,value)
                else:
                    # add new element object to list
                    element_list.append(sel_element)
                    prop_end = True
        else:
            end = True

    for e in element_list:
        print e

def get_css_element(string):
    """ Post: Extract a CSS element name from a string """

    ### Extract element name & its properties from string
    """ Eg, extract text inside [] tags
        " <style type="text/css" >
           [ body {background-color:blue;
                   color:gray;
                   text-align:center; } ]
             h1   {color:blue;
                   float:center; }
        "
    """
    element_attributes = string.split('{',1)
    element_name       = element_attributes[0]
    rest               = element_attributes[1].split('}',1)
    element_property   = rest[0]
    del rest[0]
    remaining_str = ''.join(rest)

    ### Format CSS element
    """ Eg, element_name = " \n  body  "
            element_name = "body"
    """
    element_name = element_name.replace(' ','')
    element_name = element_name.replace('\n','')

    result = (element_name, element_property, remaining_str)
    return result

def get_css_element_properties(string):
    """ Post: Extract a CSS property & value from a string """

    ### Extract 1st occurence of property & value from string
    """ Eg, extract text inside [] tags
        " [ background-color:blue;  ]
            color:gray;
            text-align:center;
            float:center;
        "
    """
    prop_value = string.split(':',1)
    property   = prop_value[0]
    rest       = prop_value[1].split(';',1)
    value      = rest[0]
    del rest[0]
    remaining_str = ''.join(rest)

    ### Format property & value
    """ Eg, property = "  \n background-color   "
            property = "background-color"
    """
    property = property.replace(' ','')
    property = property.replace('\n','')
    value    = value.replace(' ','')
    value    = value.replace('\n','')

    result = (property, value, remaining_str)
    return result 
