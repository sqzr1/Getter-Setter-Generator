/*

   Collision Algorithm:
   
*/


#ifndef COLLISIONALGORITHM_H
#define COLLISIONALGORITHM_H


#include <windows.h>
#include <cstdlib>
#include <vector>

using namespace std;


/// Constants ///
#define TI_CLOCKSTEP 1


/// Variables ///
enum State { LOOKING, HIT, NONE };
typedef class Object;

struct HashPos
{
     HashPos();
     HashPos( Object *nObj, int nValue );
     Object *obj;
     int hashValue;
};



/// Classes ///
class Room
{
      
      public:
             
          Room( int nWidth, int nHeight );
          ~Room();
          void drawSelf( HDC hdc );
         
          
      private:
              
          HRGN roomRgn;
          
};


class CollisionHandler
{
      
      public:
             
          CollisionHandler();
          ~CollisionHandler();
          void setConstPoint( int x, int y );
          int  pointAngle( POINT constant, POINT objPos );
          int  pointDistance( POINT constant, POINT objPos );
          int  findBestPlace( int hashValue, vector <HashPos*> objPos );
          void selectionSort();
          HashPos* registerObject( Object *obj, POINT objPos );
          HashPos* hashPosition( HashPos* oldHashPos, POINT objPos );
          
      private:
              
          vector <HashPos*> objectPos;
          POINT constantPnt;
};


class Object
{
      
      public:
             
          Object( CollisionHandler *col, int xPos, int yPos, int nWidth, int nHeight );
          ~Object();
          void drawSelf( HDC hdc );
          void drawHashPos( HDC hdc );
          void performStepLogic();
          bool collisionRect( CollisionHandler colH, int x, int y, int nWidth, int nHeight );
         
          
      private:
              
          CollisionHandler *colHandler;
          HRGN myRgn;
          POINT pos;
          POINT offset;
          State myState;
          HashPos* myPos;
          
};


class Controller
{
      
      public:
             
          Controller();
          ~Controller();
          void setHWND( HWND Hwnd );
          void createGameObjects();
          void instanceCreate( int x, int y );
          int  initiateClock();
          int  killClock();
          void performLogic();
          void performPaint( HDC hdc );
         
          
      private:
          
          HWND hwnd;
          vector <Object*> objList;
          Room *room;
          CollisionHandler *colHandler;
};


#endif // COLLISIONALGORITHM_H
