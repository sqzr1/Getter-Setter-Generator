/*
    Header file: Example of inheritance functionality by use of protected 
                 variables & virtual functions
*/

#ifndef INHERITANCEOBJECT_H
#define INHERITANCEOBJECT_H


#include <windows.h>

#include "DrawingEngine.h"

using namespace std;

typedef class DrawEngine;

class Object 
{
      public:
             
             Object();
             virtual bool DrawSelf( HDC hdc );
             void EraseSelf( HWND hwnd );
             void AddToDrawQueue();
             
      protected:
              
             POINT pos;
             bool visible;
             HRGN ObjRegion;
             COLORREF ObjColour;
             unsigned int depth;
             unsigned int width;
             unsigned int height;
             unsigned int direction;
             unsigned int hSpeed;
             unsigned int vSpeed;
             DrawEngine *DrawController;
};


class Circle : public Object
{
      public:
             
             Circle( DrawEngine *DController, POINT nPos, unsigned int nWidth, 
                     unsigned int nHeight, COLORREF colour );
             bool DrawSelf( HDC hdc );
             
      private:
             
};


class Square : public Object
{
      public:
             
             Square( DrawEngine *DController, POINT nPos, unsigned int nWidth, 
                     unsigned int nHeight, COLORREF colour );
             bool DrawSelf( HDC hdc );
             
      private:
             
};


#endif // INHERITANCEOBJECT_H
