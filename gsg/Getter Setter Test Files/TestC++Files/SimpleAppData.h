/*
   
   Header File: Functions relating to APP DATA Folder
   
   Description:
               
*/

#ifndef APPDATA_H
#define APPDATA_H

#include <windows.h>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;


// Variable Declarations //

enum DestinationType { APP_DATA = 0, LOCAL_APP_DATA };
typedef vector <string> ::iterator PathIndex;

// Function Declaration //

string GetAppDataFolderPath( DestinationType Dest );
bool CreateSearchLog( DestinationType Dest );
vector <string> ImportSearchLog( string FileName, DestinationType Dest );
PathIndex IsPresent( vector <string> &RecentSearches, string Path );
bool AddToSearchLog( vector <string> &RecentSearches, string FileName, 
                     string Path, DestinationType Dest );


#endif // APPDATA_H
