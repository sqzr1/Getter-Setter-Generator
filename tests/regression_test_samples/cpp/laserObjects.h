#ifndef LASEROBJECTS_H
#define LASEROBJECTS_H

#include <windows.h>
#include <cstdlib>
#include <stdio.h>
#include <queue>

using namespace std;
 

/// Constants ///
#define LA_DRAWLASER  50000
#define LA_TIMER      50001
#define LA_ANIMATION  50002


/// Objects ///
struct target {
       
       // Functions
       target(LONG xPos, LONG yPos, int xOff, int yOff);
       ~target(); 
       void drawTarget(HDC hdc);
       
       // Variables
       POINT pos;    // Object position
       int xOffset;
       int yOffset;
       HRGN objRgn;
};


struct laser {
       
       // Functions
       laser();
       ~laser();
       bool hasTarget();
       void drawController(HDC hdc, HWND hwnd);
       void drawLaser(HDC hdc, HWND hwnd);
       void createTarget(HWND hwnd, int mouseX, int mouseY);
       void moveToTarget(HWND hwnd);
       void initiateDelay(HWND hwnd);
       void ceaseDelay(HWND hwnd);
       void initAnimationTimer(HWND hwnd);
       void ceaseAnimationTimer(HWND hwnd);
       
       // Variables
       POINT base;
       POINT top;
       HRGN objRgn;
       int laserWidth;
       int hSpeed;
       int vSpeed;
       
       bool lButtonDown;
       bool createTargetAllowed;
       bool drawNewTarget;
       bool drawNewLaser;
       UINT delayTimerID;
       UINT animTimerID;
       int targetDelay;
       queue <target*> targetList;
       int targetDimension;
       int AnimFrameRate;
       HPEN laserPen;
       
       int sleepValue;
};


/// Global Functions ///
void createGUI(HWND hwnd, HINSTANCE gInstance, RECT clientR);


#endif
