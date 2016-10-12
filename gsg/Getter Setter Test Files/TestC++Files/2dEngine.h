/*
    Header file: My own simple 2d drawing engine where object's are
                 sent to a queue inside the class & then drawn onto
                 the main client window.
*/


#ifndef ENGINE_H
#define ENGINE_H


#include <windows.h>
#include <cstdlib>
#include <vector>

using namespace std;



///   Constants   ///
#define DE_CLOCKTICK 50001
#define DE_INACTIVE  50002
#define DE_ACTIVE    50003



/// Declare Types ///
typedef class Engine2d;
typedef class SystemEngine;
typedef class InputEngine;
typedef class GraphicEngine;
typedef class AudioEngine;
typedef class Object;
typedef struct ActionQueueElement;
typedef struct ObjectStatusPacket;
typedef unsigned int LogicalStatus;



///   Variables   ///
enum ObjectType     { CIRCLE = 0, SQUARE, CUSTOMOBJECT };
enum PhysicalStatus { DE_NONE = 0, DE_AUDIOSELF = 1, DE_DRAWSELF = 2, 
                      DE_DRAWAUDIOSELF = 3 };



class Engine2d
{
      public:
             
          Engine2d( unsigned int x,  unsigned int y, unsigned int width,  
                    unsigned int height, char title[], 
                    LRESULT CALLBACK EngineWndProc(HWND Hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
                   );
          ~Engine2d();
          int  RegisterEngineWindow( LRESULT CALLBACK EngineWndProc(HWND Hwnd, UINT msg, WPARAM wParam, LPARAM lParam) );
          int  CreateMainWindow( unsigned int x,  unsigned int y, 
                                 unsigned int width,  unsigned int height,
                                 char title[] );
          int  PerformGameLoop( int nCmdShow );
          int  StartClockTimer();
          int  StopClockTimer();
          void SetWindowAttributes( HWND Hwnd, HDC WindowHDC );
          void IncrementGameLoop();
          unsigned int GetGameLoopValue();
          void PerformLogicOperations();
          void PerformDrawOperations( HDC hdc );
          int  TransmitMessage( UINT Msg, WPARAM wParam, LPARAM lParam );
          Object * InstanceCreate( unsigned int XPos, unsigned int YPos, 
                                   ObjectType ObjType );
          int  InstanceDestroy( Object *Obj );
      
      
      private:
          
          SystemEngine  *SystemCont;
          InputEngine   *InputCont;
          GraphicEngine *GraphicCont;
          AudioEngine   *AudioCont;
          
          HWND hwnd; 
          HINSTANCE gInstance;
          unsigned int GameLoop;
          unsigned int ClockTickInterval;
          vector <Object*> ObjectList;
          

};



///////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                               //
//                                    Object Status Packet                                       //
//                                                                                               //
///////////////////////////////////////////////////////////////////////////////////////////////////


struct ObjectStatusPacket
{
       
       // Functions //
       ObjectStatusPacket();
       ObjectStatusPacket( PhysicalStatus PState, LogicalStatus LState );
       void SetStatus( PhysicalStatus PState, LogicalStatus LState );
       
       
       // Variables //
       PhysicalStatus PhysicalState;
       LogicalStatus  LogicalState;
       
};



///////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                               //
//                                  Action Queue Element                                         //
//                                                                                               //
///////////////////////////////////////////////////////////////////////////////////////////////////


struct ActionQueueElement
{
       
       // Functions //
       ActionQueueElement( Object *nObj, unsigned int GameLoop, 
                           unsigned int LoopIndex  );
       
       
       // Variables //
       Object *Obj;
       unsigned int GameLoopIndex;
           
};


#endif // ENGINE_H

