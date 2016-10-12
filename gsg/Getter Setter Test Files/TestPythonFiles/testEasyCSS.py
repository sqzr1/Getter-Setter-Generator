"""
   Test of EasyCSS Class
"""


from EasyCSS import *
import os

control = EasyCSS()

database_name = control.import_HTML_page("testme.HTML")

if type(database_name) == str:

    suc = control.establish_connection(database_name)
    if not suc == False:
        success = control.import_elements()
        control.import_element_properties()
    

control.import_HTML_file("testme.HTML",database_name)

print "\n\nElements & their properties extracted from HTML file include: \n"
control.debug_class()
