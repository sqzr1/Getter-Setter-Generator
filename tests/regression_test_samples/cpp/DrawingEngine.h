/*
    Header file: My own simple 2d drawing engine where object's are
                 sent to a queue inside the class & then drawn onto
                 the main client window.
*/


#ifndef DRAWINGENGINE_H
#define DRAWINGENGINE_H

#include <windows.h>
#include <queue>


using namespace std;


// Constants //
#define DE_CLOCKTICK 50001


typedef class DrawEngine;
typedef class Object;

class DrawEngine
{
      public:
             
             DrawEngine();
             void SetWindowAtrib( HWND MainHwnd );
             void StartClockTimer();
             int  StopClockTimer();
             bool ExecuteDraw( HDC WindowHDC );
             void QueueDraw( Object *o );
             
      private:
      
             queue <Object*> qDrawList;
             HWND hwnd;
             HDC BufferCanvas;
             unsigned int ClockTickInterval;
};


class Object 
{
      public:
             
             Object();
             /* Object(POINT p, unsigned int nWidth, unsigned int nHeight)
                    : pos(p), width(nWidth), height(nHeight){} */
             virtual bool DrawSelf( HDC hdc );
             virtual void EraseSelf( HDC hdc );
             virtual void AddToDrawQueue();
             virtual void MoveToPoint( POINT dest );
             
      private:
              
};


class Circle : public Object
{
      public:
             
             Circle( DrawEngine *DController, POINT nPos, unsigned int nWidth, 
                     unsigned int nHeight, COLORREF colour );
             bool DrawSelf( HDC hdc );
             void EraseSelf( HDC hdc );
             void AddToDrawQueue();
             void MoveToPoint( POINT dest );
             
      private:
             // All these variables are exactly the same as those in Square
             // so why cant I just declare these in Object class? It wont let me then
             // set values for them in circle/square's constructor. 
             // Do I have to make them virtual??
             
             
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


class Square : public Object
{
      public:
             
             Square( DrawEngine *DController, POINT nPos, unsigned int nWidth, 
                     unsigned int nHeight, COLORREF colour );
             bool DrawSelf( HDC hdc );
             void EraseSelf( HDC hdc );
             void AddToDrawQueue();
             void MoveToPoint( POINT dest );
             
      private:
             
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



#endif // DRAWINGENGINE_H
