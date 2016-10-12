/*
    Header file: My own simple 2d drawing engine where object's are
                 sent to a queue inside the class & then drawn onto
                 the main client window.
*/


#ifndef AUDIOENGINE_H
#define AUDIOENGINE_H


#include <windows.h>

#include "2dEngine.h"


class AudioEngine
{
      public:
             
          AudioEngine( Engine2d *ParentEng );
          ~AudioEngine();
          void StoreSiblingEngines( SystemEngine *SystemEng, 
                                    InputEngine *InputEng, 
                                    GraphicEngine *GraphEng );
          int  AddToAudioQueue( Object *Obj );                          
          bool ExecuteAudioLogic();            
          
             
      private:
              
          Engine2d      *ParentEngine;
          SystemEngine  *SystemCont;
          InputEngine   *InputCont;
          GraphicEngine *GraphicCont;
          
          vector <Object*> AudioObjQueue;

};


#endif // AUDIOENGINE_H
