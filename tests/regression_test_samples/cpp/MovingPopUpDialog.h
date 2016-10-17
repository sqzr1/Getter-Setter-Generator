/*

   Win32 Pop-up Dialog: Subclass object of PopUpDialog class that moves to 
                        across the screen
   
*/


#ifndef MOVPOPUPDIALOG
#define MOVPOPUPDIALOG

#include <windows.h>
#include <queue>
#include "PopUpDialog.h"


/// Functions ///

bool CreateMovingPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, 
                              PopUpDialog :: DisplayPos position, unsigned int popupLifetime, std::string bkImagePath );
bool CreateMovingPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, 
                              PopUpDialog :: DisplayPos position, unsigned int popupLifetime, HBITMAP bkImage );
                                    

/// MovingPopUpDialog Class ///

class MovingPopUpDialog  :  public PopUpDialog
{
    
    public:
        
        MovingPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, DisplayPos position, std::string bkImagePath );
        MovingPopUpDialog( HWND nParentHwnd, unsigned int nWidth, unsigned int nHeight, char* caption, DisplayPos position, HBITMAP bkImage );
        
        void  CalculateWindowPos();
        
        float PointDistance( POINT p1, POINT p2 );
        float DecelerateObject( float initialSpeed, float finalSpeed );
        POINT MoveToPoint( POINT myPos, float speed );
        void  PerformPathFinding( unsigned int xTarget, unsigned int yTarget, float initSpeed );
        bool  UpdateWindowPos();
        
        bool  PerformComplimentaryWindFuncts();
        int   BeginWindowTimer();
        bool  RunDialog( unsigned int _popupLifetime );
        
        
    private:
        
        static unsigned int TIMESTEP;
        POINT               dest;
        std::queue <POINT>  perStepMovement;
        
};


#endif // MOVPOPUPDIALOG
