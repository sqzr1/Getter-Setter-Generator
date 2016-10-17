# Week 3 Practical

import sys

def generate(letterList, st):

    for i in range(len(letterList)):
        tempStr = letterList[i]+st
        print(tempStr)

def encouragement(st, nTimes):

    goStr  = "Go! "
    result = goStr + st + " "

    for x in range(nTimes):
        result += goStr
        
    return result

def htmlEg(content, templateStr):

    templateStr = templateStr %content

    return templateStr

def main():

    HTMLTemplate = "<html> \n<head> \n\n</head> \n<body> \n %s \n</body> \n</html>"
    nameTurple = ['Steve','Sam']
    name = "Steve"

    s = htmlEg(nameTurple,"<a href=#> %s </a> \n")
    print(s)
    s = htmlEg(name,HTMLTemplate)
    print(s)
    
main()
