import os
import sys

def display_file_contents(HTML_filename):
    """ Post: Display contents of  """

    HTML_file   = open(HTML_filename,'r')
    HTML_source = HTML_file.read()

    print HTML_source

    HTML_file.close()

def format_file(HTML_filename):
    """ """

    HTML_file   = open(HTML_filename,'r')
    HTML_source = HTML_file.read()
    HTML_file.close()

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
    print "\n\n\n\n '<' Spaces taken out \n\n\n"
    print HTML_source

    """# Format all ID's & classes correctly
    temp_buf        = HTML_source.lower()
    class_occurence = temp_buf.count("class")
    ID_occurence    = temp_buf.count("id")

    for n in range(class_occurence):
        hit = temp_buf.find("class")
        if not hit==-1:
            temp_buf = temp_buf.replace(temp_buf[hit], '~')
            x = hit+5

            # delete any spaces until we reach a letter or number
            while x<len(temp_buf):
                if temp_buf[x] == ' ':
                    temp_buf    = temp_buf.replace(temp_buf[x],'')
                    HTML_source = HTML_source.replace(HTML_source[x],'')
                elif temp_buf[x] == '=':
                    pass
                else:
                    break
                x += 1

    for n in range(ID_occurence):
        hit = temp_buf.find("id")
        if not hit==-1:
            temp_buf = temp_buf.replace(temp_buf[hit], '~')
            x = hit+2

            # delete any spaces until we reach a letter or number
            while x<len(temp_buf):
                if temp_buf[x] == ' ':
                    temp_buf    = temp_buf.replace(temp_buf[x],'')
                    HTML_source = HTML_source.replace(HTML_source[x],'')
                elif temp_buf[x] == '=':
                    pass
                #elif temp_buf[x] == "'" or temp_buf[x] == '"' isalpha(temp_buf[x])
                else:
                    break
                x += 1

    print HTML_source
    print "\n temp_buf \n\n\n"
    print temp_buf"""

def get_css_data(buf, element_list):
    """ """

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
    """ """

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
    """ """

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

def get_internal_CSS_data(HTML_source):
    """ Post: Extract internal CSS style sheet from HTML source
              code."""

    HTML_file   = open('Study.HTML','r')
    HTML_source = HTML_file.read()
    HTML_file.close()

    CSS_data = None

    if '<style' in HTML_source and 'type="text/css"' in HTML_source and '</style' in HTML_source:

        CSS_data = HTML_source.split('<style')[1]
        CSS_data = CSS_data.split('>')[1]
        CSS_data = CSS_data.split('</style')[0]
        ## ABOVE MAYBE better as...
        ## CSS_data = CSS_data.split('</')[0]

        # Delete any CSS comments from string
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

    print CSS_data
    return CSS_data

def main():
    """ """

    """print "Original Document:\n\n"
    display_file_contents("Study.HTML")
    print "\n\n\n Result with changes: \n\n"
    format_file("Study.HTML")
    """

    a = """.imgcatalogo 
{  
    position: absolute; 
    margin-left: 100px; 
} 
 
#table_catalogo 
{ 
    left: 2%; 
    z-index: 0; 
} 
 
#stage_catalogo 
{ 
    left: 50%; 
    margin-left: -100px; 
    z-index: 1; 
} 
 
#displays_catalogo 
{ 
    left: 98%; 
    margin-left: -250px; 
    z-index: 2; 
} 
 
#image_catalogo 
{ 
    width: 240px; 
    height: 500px; 
    float: left; 
    text-align: left; 
}  """

    #get_css_data(a)
    #format_file("Study.HTML")
    get_internal_CSS_data('a')
    

if __name__ == "__main__":
    main()
