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

struct RecentPath
{
      unsigned int FreqIndex;    // Frequency Index
      unsigned int AlphaIndex;   // Alphabetical Index
      string Path; 
};

enum DestinationType { APP_DATA = 0, LOCAL_APP_DATA };



// Function Declaration //

string GetAppDataFolderPath( DestinationType Dest );
bool CreateSearchLog( DestinationType Dest );
vector <string> ImportSearchLog( string FileName, DestinationType Dest );
void AddRecentPath( vector <RecentPath> &RecentSearches, string nPath );
int  BinarySearch( vector <RecentPath> &v, int begin, int end, string target );
int  IsPresent( vector <RecentPath> &RecentSearches, string Path );
bool AddToSearchLog( vector <RecentPath> &RecentSearches, string FileName, 
                     string Path, DestinationType Dest );


#endif // APPDATA_H
