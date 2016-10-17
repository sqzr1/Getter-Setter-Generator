#ifndef OBJECT_H
#define OBJECT_H


#include <windows.h>
#include <cstdlib>

#include "2dEngine.h"

using namespace std;



class Object 
{
      public:
             
             Object();
             // virtual ~Object();
             virtual bool DrawSelf( HDC hdc ) {};
             virtual bool EraseSelf( HDC hdc ) {};
             virtual ObjectStatusPacket PerformStepLogic() {};
             virtual void MoveToPoint( POINT dest ) {};
             
      private:
              
};



class Circle : public Object
{
      public:
             
             enum Wall { LEFT = 0, UP, RIGHT, DOWN };
             
             Circle( unsigned int XPos, unsigned int YPos, unsigned int nWidth, 
                     unsigned int nHeight, COLORREF colour );
             bool DrawSelf( HDC hdc );
             bool EraseSelf( HDC hdc );
             ObjectStatusPacket PerformStepLogic();
             void MoveToPoint( POINT dest );
             void CalculateNewDestination();
             
      private:   
                 
             POINT pos;
             POINT Destination;
             bool visible;
             HRGN ObjRegion;
             COLORREF ObjColour;
             unsigned int depth;
             unsigned int width;
             unsigned int height;
             unsigned int direction;
             unsigned int hSpeed;
             unsigned int vSpeed;  
             float xOffset;
             float yOffset;
 
};



class Square : public Object
{
      public:
             
             Square( unsigned int XPos, unsigned int YPos, unsigned int nWidth, 
                     unsigned int nHeight, COLORREF colour );
             bool DrawSelf( HDC hdc );
             bool EraseSelf( HDC hdc );
             ObjectStatusPacket PerformStepLogic();
             void MoveToPoint( POINT dest );
             
      private:   
                 
             POINT pos;
             POINT Dest;
             bool visible;
             HRGN ObjRegion;
             COLORREF ObjColour;
             unsigned int depth;
             unsigned int width;
             unsigned int height;
             unsigned int direction;
             unsigned int hSpeed;
             unsigned int vSpeed;   
             float xOffset;
             float yOffset;
             
};






class CustomObject : public Object
{
      public:
             
             CustomObject( unsigned int XPos, unsigned int YPos, 
                           unsigned int nWidth, unsigned int nHeight, 
                           COLORREF colour );
             bool DrawSelf( HDC hdc );
             bool EraseSelf( HDC hdc );
             ObjectStatusPacket PerformStepLogic();
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
             float xOffset;
             float yOffset;  
};



#endif // OBJECT_H
