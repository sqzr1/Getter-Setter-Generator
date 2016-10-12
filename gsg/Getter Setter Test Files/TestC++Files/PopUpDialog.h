/*

   Win32 Pop-up Dialog: Subclasses a Static Control
   
*/


#ifndef POPUPDIALOG
#define POPUPDIALOG

#include <windows.h>
#include <string>



/// Constants ///

#define PD_TIMER       50001
#define PD_CLOCK_STEP  50002
#define PD_TEXT_DLG    50003



/// Variables ///

typedef class  PopUpDialog;
typedef struct PopUpDialogInfo;

struct PopUpDialogInfo
{
      // Variables:
      PopUpDialog *popUpWindow;
      WNDPROC      defaultWndProc;
      
      // Constructor:
      PopUpDialogInfo( PopUpDialog *_popUpWindow, WNDPROC _defaultWndProc );
};



/// PopUpDialog Class ///

class PopUpDialog
{
        
    public:
        
        enum DisplayPos { CENTRE = 0, BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM, TOP_LEFT, TOP_RIGHT, TOP };
        HWND parentHwnd;
        
        
        PopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, DisplayPos position, std::string bkImagePath );
        PopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, DisplayPos position, HBITMAP bkImage );
        ~PopUpDialog();
        
        bool  SubClassWindow();
        void  CalculateWindowPos();
        bool  IsBitmapFile( std::string bmpFilePath );
        bool  LoadDefBackground();
        bool  LoadBackgroundImage( std::string bitmapName );
        bool  LoadBackgroundImageEx( std::string bitmapName );
        bool  LoadResizeBitmap( std::string bitmapName );
        
        int   BeginTimer( UINT timerMessage, unsigned int timerDuration );
        int   EndTimer(   UINT timerMessage );
        bool  KillDialog();
        
        virtual bool  PerformComplimentaryWindFuncts() {};
        virtual int   BeginWindowTimer();
        virtual bool  RunDialog( unsigned int _popupLifetime );
        
        
    protected:
        
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

LRESULT CALLBACK PopUpDialogSubWndProc( HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam );
bool             CreatePopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, 
                                    char* caption, PopUpDialog :: DisplayPos position, 
                                    unsigned int popupLifetime, std::string bkImagePath );
bool             CreatePopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, 
                                    char* caption, PopUpDialog :: DisplayPos position,
                                    unsigned int popupLifetime, HBITMAP bkImage );



#endif // POPUPDIALOG
