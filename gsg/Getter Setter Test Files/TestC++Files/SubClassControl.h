/*
  
   Example: Sub-Class a windows EditBox
   
   Header file

*/


#ifndef SUBCLASS_EB
#define SUBCLASS_EB

#include <windows.h>


LRESULT CALLBACK customEditBoxProc( HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam );
bool subClassControl( HWND controlHwnd, LRESULT newWndProc );


#endif // SUBCLASS_EB

