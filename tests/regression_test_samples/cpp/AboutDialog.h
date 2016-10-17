/*

   About Dialog Header: 
               
*/


#ifndef ABOUTDIALOG_H
#define ABOUTDIALOG_H


#include <windows.h>
#include <vector>


/// Constants ///
#define AB_OK 50001


/// Variables ///
typedef class  AboutDialog;
typedef struct AboutDialogInfo;


/// Functions ///
int RegisterAboutDialog();
LRESULT CALLBACK AboutDlgWndProc( HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam );



struct AboutDialogInfo
{
       char* AppTitle;
       char* AppDescription;
       char* AppShortcuts;
       char* AppAuthor;
       
};



struct TabInfo
{
       // Public Functions
       TabInfo( HDC hdc, char* string );
       void IdentifyTabs( HDC hdc );
       
       // Public Variables
       char *str;
       int StrLength;
       int ReqHeight;
       std::vector <int> TabPositions; 
       
};



struct TabInfoEx
{
       // Public Functions
       TabInfoEx( char* string );
       ~TabInfoEx();
       void IdentifyTabs();
       
       // Public Variables
       char *str;
       int StrLength;
       int TabNumber;
       int *TabPositions; // Dynamic Array to store positions of tabs
       
};



class AboutDialog
{
      public:
            
            AboutDialog( HDC hdc, AboutDialogInfo nDialogInfo, RECT ScreenR, 
                         RECT ClientR );
            ~AboutDialog();
            void CalculateOptimalDimensions( HDC hdc );
            void CreateGUI( HWND hwnd ); 
             
             
      private:
              
            AboutDialogInfo DialogInfo;
            
            POINT ControlPos[5];
            POINT ControlDim[5];
            unsigned int WindowWidth;
            unsigned int WindowHeight;

};


#endif // ABOUTDIALOG_H
