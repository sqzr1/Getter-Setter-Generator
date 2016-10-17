"""

  EasyCSS class is designed to allow someone who does not know CSS
  to make aestetic & visual alterations to their website. This
  class allows someone to change colours, images, text & much more.

  Author:   Sam Zielke-Ryner
  Email :   samzielkeryner@yahoo.com.au
  Location: Sydney Australia
  Authors Programming Experience: C++, Python, SQL, CSS, HTML

  This library is part of a portfolio.
  *** Do NOT use this library for personal or commericial use unless
  given verbal or written permission by author. 
  
"""

import sqlite3
import os


#--------------------------------------------------------------------#
#     Class to store HTML elements imported from HTML files &/or     #
#      SQLite3 Database.                                             #                                   
#--------------------------------------------------------------------#

class element:

    obj_name  = "" # Declare public variables
    obj_type  = ""
    css_name  = ""
    db_name   = ""
    attribute = {}

    
    def __init__(self, database_name, object_name, object_type):
        """ Default Constructor """
        
        self.obj_name  = object_name
        self.obj_type  = object_type
        self.css_name  = str(self.obj_name)+" { " # str() used here incase user incorrectly inputs a non-str value
        self.db_name   = database_name
        self.attribute = {}


    def add_attribute(self, key, value):
        """ Post: Properties(CSS)/Keys(Dict) are dynamically created.""" 

        value = str(value)
        self.attribute[key] = value

        """ Check if property already exists in element table """
        conn = sqlite3.connect(self.db_name)
        cur  = conn.cursor()
        check_exists = "SELECT value FROM "+ self.obj_name +" WHERE property = '"+ key +"';"
        cur.execute(check_exists)
        result = cur.fetchone()

        """ Update database """
        try:
            # If property already exists update its value
            if not result == None:
                change_value = "UPDATE "+ self.obj_name +" SET value = '"+ value +"' WHERE property = '"+ key +"';"
                cur.execute(change_value)
            else:
                change_value = "INSERT INTO "+ self.obj_name +" (property, value) VALUES(?,?);"
                cur.execute(change_value,[key,value])

            conn.commit()
            conn.close()

            print "Attribute added in "+self.obj_name
            return True

        except TypeError:
            print "'add_attribute' function failed. Reasons: table or column does not exist OR parameter 'new_value' has invalid value."
            return False


    def print_attributes(self):
        """ Post: Returns an objects' CSS attributes as a string
                  with each Property(color,margin,etc). """
        
        template = "%s: %s; "
        result = ""

        for property in self.attribute:
            if not self.attribute[property] == 'none':
                """ Eg, 'color: black;' """
                result += template % (property,self.attribute[property])

        css_begin = self.css_name
        formatted_code = css_begin + result + " } \n"
        return formatted_code


class body:
    def __init__(self, object_name):
        """ """
        obj_name  = object_name
        css_name  = "body { %s } \n"
        attribute = {'color': 'black', 'background-color': 'blue', 'font-family': "'Arial','Myriad','Serif';",
                     'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px', 'margin-bottom': '10px'}


class div:
    def __init__(self, object_name):
        """ """
        obj_name  = object_name
        css_name  = "div { %s } \n"
        attribute = {'color': 'black', 'background-color': 'blue', 'font-family': "'Arial','Myriad','Serif';",
                     'margin-left': '10px', 'margin-right': '10px', 'margin-top': '10px', 'margin-bottom': '10px',
                     'padding-left': 'auto', 'padding-right': 'auto', 'padding-top': 'auto', 'padding-bottom': 'auto'}



#--------------------------------------------------------------------#
#     Main Class to import HTML elements, append elements & write    #
#     to SQLite3 Database, CSS file, HTML file or Webpage.           #       
#--------------------------------------------------------------------#

class EasyCSS:

    object_list   = [] # Declare variable as public
    database_name = ""


    def __init__(self):
        """ """
        object_list  = [] # store all webpages' HTML elements in list
        bground_attrib = {'background-color': "background-color: %s ;", 'background-image': 'background-image: %s ;',
                          'background-repeat': 'background-repeat: %s ;', 'background-position': 'background-position: %s ;'}
        align_attrib = {'margin-left': 'margin-left: %s ;', 'margin-right': 'margin-right: %s ;',
                        'margin-top': 'margin-top: %s ;','margin-bottom': 'margin-bottom: %s ;',
                        'padding-left': 'padding-left: %s ;','padding-right': 'padding-right: %s ;',
                        'padding-top': 'margin-top: %s ;','padding-bottom': 'padding-bottom: %s ;',
                        'float': 'float: %s ;'}
        text_attrib = {'color': "color: %s ;", 'text-decoration': 'text-decoration: %s ;',
                       'text-align': 'text-align: %s ;', 'vertical-align': 'vertical-align: %s ;', }
        properties  = []



#--------------------------------------------------------------------#
#            Import HTML Elements from SQLite3 Database              #
#--------------------------------------------------------------------#
        
    def establish_connection(self, database):
        """ Post: Establish connection to SQLite 3 database to
                  import CSS element attributes. """
        
        try:
            # Test connection
            self.database_name = database
            conn = sqlite3.connect(database)
            conn.close()
            return True
        except (sqlite3.OperationalError, msg):
            return False


    
    def import_elements(self):
        """ Post: Import CSS elements from a SQLite 3 database. """

        function_success = False
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()

        """ Catalog all CSS elements, custom ID's & custom Classes """
        cur.execute("SELECT element, type FROM variables;")
        result = cur.fetchall()

        if len(result) > 0:

            function_success = True
            for ele in result:

                if self.is_present(ele[0]) == None:
                    self.create_dynamic_object(ele[0],ele[1])
                    print "Object from database added "+ele[0]+" "+ele[1]
            
        conn.close()
        return function_success



    def import_element_properties(self):
        """ Post: Import HTML/CSS elements properties & values from
                  SQLite 3 database. """

        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        open_table = "SELECT property,value FROM "

        for obj in self.object_list:
            cur.execute(open_table + obj.obj_name + ";")
            if not cur.fetchone() == None:
                for value in cur.fetchall():
                    obj.add_attribute(value[0],value[1])

        conn.close()


    
    def create_object(self, object_name, object_type):
        """ Post: Create HTML element object & add to database."""

        new_element = element(self.database_name,object_name,object_type)
        self.object_list.append(new_element)

        """ Create object in database """
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()
        
        add_element_row = "INSERT INTO variables(element, type) VALUES('"+ object_name +"', '"+ object_type +"');"
        add_element = "CREATE TABLE "+ object_name +" (property TEXT PRIMARY KEY, value TEXT);"
        cur.execute(add_element_row)
        conn.commit()
        cur.execute(add_element)
        conn.commit()
        conn.close()



    def create_dynamic_object(self, object_name, object_type):
        """ Post: Create an object that already exists in database."""

        new_element = element(self.database_name,object_name,object_type)
        self.object_list.append(new_element)


        
    def is_present(self, name):
        """ Post: If there is an object with the same name as name
                  string then that object is returned else we return
                  None."""
        
        for obj in self.object_list:

            if name == obj.obj_name:
                print name+"object already exists"
                return obj

        return None



#--------------------------------------------------------------------#
#       Write HTML & CSS data from Database to file or Webpage       #
#--------------------------------------------------------------------#

    def write_external(self, file_name):
        """ Post: Write External CSS file """
        
        # Get CSS element attributes
        css_string = []
        for obj in self.object_list:
            css_string.append(obj.print_attributes())

                
        # Backup CSS file to backupCSS.css file 
        backup_file = open(file_name,'r')
          # Backup CSS file to backupCSS.css file 
        backup_file.close()


        # Write CSS list variable to file
        css_file = open(file_name,'w')
        css_file.write(css_string)
        css_file.close()



    def write_internal(self):
        """ Post: Create Internal CSS style sheet 'on the fly'/
                  as the website loads """

        # TODO: Find <head> in HTML file & insert the below text
        print "Content-Type: text/html \n"
        print "<style type='text/css'>"

        # Get CSS element attributes
        for obj in self.object_list:
            print obj.print_attributes()

        print "</style>"



#--------------------------------------------------------------------#
#     Import Elements from HTML file & create SQLite3 Database       #
#--------------------------------------------------------------------#

    def import_HTML_page(self, HTML_filename):
        """ Pre:  file_name must be a string with NO file extension defined
            Post: Create a SQLite3 database with a table that will catalog
                  all of this websites' HTML elements, ID's & classes. """

        """ Create SQLite3 database """
        try:
            # if HTML_filename = file.HTML
            if '.' in HTML_filename:
                HTML_filename = HTML_filename.split('.')[0]
            
            self.database_name = HTML_filename+".db"
            
            # If database file already exists
            if os.path.isfile(self.database_name):
                print "Notify: "+self.database_name+" Database file already exists in this directory."
                return self.database_name

            """ Create SQLite3 database with same name as file_name """
            conn = sqlite3.connect(self.database_name)
            cur = conn.cursor() 
            cur.execute("CREATE TABLE variables (element varchar, type varchar);")
            conn.commit()
            conn.close()

            print "Notify: "+self.database_name+" Database file created in this directory."
            return True
        
        except sqlite3.OperationalError:
            print "'import_HTML_page' Function Error: Failed to establish database connection."
            return False



    def format_file(self, HTML_filename):
        """ Post: Correctly format HTML file so we can identify HTML
                  elements & CSS elements."""

        """ Get HTML source code """
        HTML_file   = open(HTML_filename,'r')
        HTML_source = HTML_file.read()
        HTML_file.close()

        if HTML_source==None:
            return None
    
        """ Format HTML text for catalog_elements() """
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

        HTML_source = ''.join(HTML_list)
        return HTML_source



    def get_internal_CSS_data(self, HTML_source):
        """ Post: Extract internal CSS style sheet from HTML source
                  code & format CSS code."""

        CSS_data = None

        if '<style' in HTML_source and 'type="text/css"' in HTML_source and '</style' in HTML_source:

            CSS_data = HTML_source.split('<style')[1]
            CSS_data = CSS_data.split('>')[1]
            CSS_data = CSS_data.split('</style')[0]
            ## ABOVE MAYBE better as...
            ## CSS_data = CSS_data.split('</')[0]

            """ Delete any CSS comments from string """
            end = False
            while end==False:

                if '/*' in CSS_data and '*/' in CSS_data:
                    before_comment = CSS_data.split('/*',1)[0]
                    after_comment  = CSS_data.split('*/',1)[1]
                    before = ''.join(before_comment)
                    after  = ''.join(after_comment)
                    CSS_data = before+'\n'+after
                else:
                    end = True

        return CSS_data
            


    def catalog_elements(self, HTML_source):
        """ Post: Identify all HTML elements including custom classes
                  & id's and store their name & type in a list. """

        """ Identify & separate classes & id's """
        class_list = HTML_source.split('class=')
        id_list    = HTML_source.split('id=')

        target_element = {'<body': 'body',
                          '<p'   : 'p',
                          '<div' : 'div',
                          '<a'   : 'a',
                          '<ul'  : 'ul',
                          '<ol'  : 'ol'
                          }
        
        for string in class_list:
            if string[0] == '"':
                class_name = string.split('"')[1]
                if self.is_present(class_name) == None:
                    print "**creating object coz doesnt exist "+class_name
                    self.create_object(class_name,"class")

        for string in id_list:
            if string[0] == '"':
                id_name = string.split('"')[1]
                if self.is_present(id_name) == None:
                    self.create_object(class_name,"id")

        """ Identify HTML elements """
        for target in target_element:
            if target in HTML_source:
                if self.is_present(target_element[target]) == None:
                    self.create_object(target_element[target],target_element[target])



    def get_css_element(self, string):
        """ Post: Extract a CSS element name from a string
                  & determine its type. """

        """ Extract element name & its properties from string

            Eg, extract text inside [] tags
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


        """ Format CSS element

            Eg, element_name = " \t  body   \n  "
                element_name = "body"
        """
        delimiters = ('\n','\t','\r',' ')
        for delim in delimiters:
            element_name = element_name.replace(delim,'')

        """element_name = element_name.replace('\n','')
        element_name = element_name.replace('\t','')
        element_name = element_name.replace('\r','')
        element_name = element_name.replace(' ','')"""


        """ Determine element type """
        if '#' in element_name: 
            # Example: element_name = '"#navbar"'
            element_name = '"'+element_name+'"'
            element_type = "id"
        elif '.' in element_name:

            element_name = '"'+element_name+'"'
            element_type = "class"
        elif ',' in element_name:

            element_name = '"'+element_name+'"'
            element_type = "join"
        else:
            element_type = element_name


        result = (element_name, element_type, element_property, remaining_str)
        return result



    def get_css_element_properties(self, string):
        """ Post: Extract a CSS property & value from a string """

        """ Extract 1st occurence of property & value from string

            Eg, extract text inside [] tags
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


        """ Format property & value

            Eg, property = "  \n background-color   "
                property = "background-color"
        """
        delimiters = ('\n','\t','\r',' ')
        for delim in delimiters:
            property = property.replace(delim,'')
            value    = value.replace(delim,'')
            
        """property = property.replace('\n','')
        property = property.replace('\t','')
        property = property.replace('\r','')
        property = property.replace(' ','')
        value    = value.replace('\n','')
        value    = value.replace('\t','')
        value    = value.replace('\r','')
        value    = value.replace(' ','')"""
        

        result = (property, value, remaining_str)
        return result 



    def import_HTML_file(self, HTML_filename, db_filename):
        """ Pre:  db_filename string must be a SQLite3 database file
                  name including path & extension.
            Post: Catalog all HTML & CSS elements in HTML file.Create
                  an SQLite3 table for each HTML element. """

        HTML_source  = self.format_file(HTML_filename)

        if not HTML_source == None:
            self.catalog_elements(HTML_source)
            CSS_data = self.get_internal_CSS_data(HTML_source)

            # if HTML code contains internal CSS style sheet
            if not CSS_data == None:
                self.catalog_CSS_data(CSS_data)
                                      
            self.update_database(db_filename)
            return True

        else:
            print "'import_HTML_page' Function Error: HTML file is empty or incorrectly formated."
            return False



    def catalog_CSS_data(self, buf):
        """ Post: Identify all CSS elements including custom classes
                  & id's, store their name & type in a list & extract
                  element properties & values. """

        remaining_str = buf
        end = False

        while end==False:
            """ Extract element name """
            if '{' in remaining_str and '}' in remaining_str:

                tup = self.get_css_element(remaining_str)
                element_name   = tup[0]
                element_type   = tup[1]
                ele_properties = tup[2]
                remaining_str  = tup[3]
                sel_element = self.is_present(element_name)
                if sel_element == None:
                    self.create_object(element_name,element_type)
                    sel_element = self.object_list[-1]
                
                prop_end = False

                """ Extract element properties & their values """
                while prop_end==False:
                
                    if ':' in ele_properties and ';' in ele_properties:

                        tup = self.get_css_element_properties(ele_properties)
                        property = tup[0]
                        value    = tup[1]
                        ele_properties = tup[2]
                        sel_element.add_attribute(property,value)
                    else:
                        prop_end = True
            else:
                end = True



    def update_database(self, db_filename):
        """ """
        pass



    def debug_class(self):
        """ Post: Used for debugging class """
        
        for obj in self.object_list:
            stats = obj.print_attributes()
            print "Element in object_list[]"
            print stats

