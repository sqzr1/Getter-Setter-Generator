#ifndef CONTVCATALOG_H
#define CONTVCATALOG_H

#include <windows.h>
#include <cstdlib>
#include <string>

using namespace std;

struct tvShow {
       
       tvShow();
       
       string name;
       string otherData;
       string synopsis;
       float timeStart;
};

class channel {
      
      public: 
           channel();
             
     private:
           string name;
           
};

// Visual Control - Similar to a List Box control but with more custom functionality
class updateBox {
      
      public:
           updateBox();
             
      private:
              
};

class controller {
     
     public: 
           controller();
           void createGUI(HWND hwnd, HINSTANCE gInstance, RECT clientR, UINT controlID[]);
           bool displaySchedule(HWND hwnd, HINSTANCE gInstance, RECT windowR);
           bool createDatabase();
           bool openDatabase();
           bool closeDatabase();
             
     private:
          string classificationDetails;
          string consumerAdvice;
};

#endif
