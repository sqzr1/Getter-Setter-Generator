#!/usr/bin/python

"""CGI Web server

Will serve pages from the current directory and cgi
scripts from the cgi-bin subdirectory.
Listens on port 8000 by default but this can be
changed by giving the script a numeric argument. """

import BaseHTTPServer
import CGIHTTPServer 

import sys
import os


if len(sys.argv) > 1:
    port = int(sys.argv[1])
else:
    port = 8000

server_address = ('', port)

handler = CGIHTTPServer.CGIHTTPRequestHandler
httpd = BaseHTTPServer.HTTPServer(server_address, handler)

print "Server running, connect to http://localhost:%s/" % port
print "Scripts in the cgi-bin folder will be run as CGI."

httpd.serve_forever()


