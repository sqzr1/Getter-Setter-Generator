# Practice 6

import sys

def writeHtml(template, content):

    result = template %content;
    return result
    

def main():

    # HTML String Templates
    paraTemp = "<p> %s </p>"
    linkTemp = "<a href=> %s </a>"

    test = writeHtml(linkTemp,"Home Page")
    print(test)


main()
