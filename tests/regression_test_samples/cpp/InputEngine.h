/*
    Header file: My own simple 2d drawing engine where object's are
                 sent to a queue inside the class & then drawn onto
                 the main client window.
*/


#ifndef INPUTENGINE_H
#define INPUTENGINE_H


#include <windows.h>
#include <cstdlib>
#include <deque>

#include "2dEngine.h"

using namespace std;



class InputEngine
{
      public:
             
          InputEngine( Engine2d *ParentEng );
          ~InputEngine();
          void StoreSiblingEngines( SystemEngine *SystemEng,
                                    GraphicEngine *GraphEng, 
                                    AudioEngine *AudioEng );
          unsigned int GetGameLoopValue();
          int  AddToActionQueue( Object *Obj, LogicalStatus LogicalState  );
          int  InsertQueueElement( unsigned int TargetLoop );
          int  ToggleObjectActivation( Object *Obj );
          void ExecuteActionLogic(); 
             
             
      private:
              
          Engine2d      *ParentEngine;
          SystemEngine  *SystemCont;
          GraphicEngine *GraphicCont;
          AudioEngine   *AudioCont;
          
          deque  <ActionQueueElement> ObjectActivityQueue; 

};


#endif // INPUTENGINE_H
