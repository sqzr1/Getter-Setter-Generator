/*

    Header File: Collision Handler

*/


#ifndef COLLISIONHANDLE_H
#define COLLISIONHANDLE_H


#include <vector>
#include "Object.h"


struct Cell
{
       unsigned int xPos;
       unsigned int yPos;
       const bool SitAllowed;
       const bool MoveAllowed;
       const int  Depth;
       Object *Occupant;
};


class CollisionHandler
{
      public:
             CollisionHandler();
             ~CollisionHandler();
             bool RequestMove( Cell nCell, int ObjDepth, int Action );
             void ReleaseCell( Cell nCell );
             Cell CollisionCell();
             
             
      private:
             
             vector <Cell*> RoomCells; 
              
};



#endif // COLLISIONHANDLE_H
