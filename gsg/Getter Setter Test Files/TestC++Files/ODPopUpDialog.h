/*

   Win32 Pop-up Dialog: Owner Drawn Popup Dialog
   
*/


#ifndef ODPOPUPDIALOG
#define ODPOPUPDIALOG

#include <windows.h>
#include <string>



/// Constants ///

#define PD_TIMER       50001
#define PD_CLOCK_STEP  50002



/// Variables ///

enum           DisplayPos { CENTRE = 0, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM, TOP_LEFT, TOP_RIGHT, TOP };
typedef class  ODPopUpDialog;



/// PopUpDialog Class ///

class ODPopUpDialog
{
    
    public:
        
        HWND parentHwnd;
        
        
        ODPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, DisplayPos position, std::string bkImagePath );
        ODPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, DisplayPos position, HBITMAP bkImage );
        ~ODPopUpDialog();
        
        bool  isDialogRegistered();
        void  CalculateWindowPos();
        bool  IsBitmapFile( std::string bmpFilePath );
        bool  LoadDefBackground();
        bool  LoadBackgroundImage( std::string bitmapName );
        bool  LoadBackgroundImageEx( std::string bitmapName );
        bool  LoadResizeBitmap( std::string bitmapName );
        void  SetStaticPicture();
        bool  DrawPopupDialog( HDC hdc );
        
        int   BeginTimer( UINT timerMessage, unsigned int timerDuration );
        int   EndTimer(   UINT timerMessage );
        bool  KillDialog();
        
        virtual bool  PerformComplimentaryWindFuncts() {};
        virtual int   BeginWindowTimer();
        virtual bool  RunDialog( unsigned int _popupLifetime );
        
        
    protected:
        
        bool RegisterPopUpDialog();
        
        
        static bool              isRegistered;
        static const std::string defImgPath;
        
        
        bool                isRunning;
        HWND                hwnd;
        unsigned int        width;
        unsigned int        height;
        unsigned int        popupLifetime;
        HBITMAP             bkgdImage;
        DisplayPos          positionType;
        char*               windowClass;
        char*               windowCaption;
        DWORD               windowFlags;
        POINT               pos;
        
};



/// Functions ///

LRESULT CALLBACK PopUpDialogWndProc( HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam );
bool             CreateODPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, 
                                      char* caption, DisplayPos position, 
                                      unsigned int popupLifetime, std::string bkImagePath );
bool             CreateODPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, 
                                      char* caption, DisplayPos position,
                                      unsigned int popupLifetime, HBITMAP bkImage );



#endif // ODPOPUPDIALOG
