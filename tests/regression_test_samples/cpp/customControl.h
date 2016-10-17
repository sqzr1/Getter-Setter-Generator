#ifndef UPDATEBOX_H
#define UPDATEBOX_H

#include <windows.h>


void RegisterCustomControlClass();
LRESULT CALLBACK CustomControlWndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);

class CustomControl {
      
      public:
           CustomControl();
           int counter;
             
      private:
           POINT pos;     
};

#endif
