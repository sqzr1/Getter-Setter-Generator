"""
   Test of Website Updater Class
"""


from EasyCSS import *
import os

control = EasyCSS()

database_name = control.import_HTML_page("testme.HTML")

if type(database_name) == str:

    suc = control.establish_connection(database_name)
    if not suc == False:
        success = control.import_elements()
        print success
        control.import_element_properties()
    

control.import_HTML_file("testme.HTML",database_name)

print "Elements & their properties extracted from HTML file include: "
control.debug_class()
