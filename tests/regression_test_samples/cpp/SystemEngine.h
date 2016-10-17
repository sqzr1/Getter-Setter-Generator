/*
    Header file: My own simple 2d drawing engine where object's are
                 sent to a queue inside the class & then drawn onto
                 the main client window.
*/


#ifndef SYSTEMENGINE_H
#define SYSTEMENGINE_H

#include <windows.h>
#include <cstdlib>

#include "2dEngine.h"


class SystemEngine
{
      public:
             
          SystemEngine( Engine2d *ParentEng );
          ~SystemEngine();
          void StoreSiblingEngines( InputEngine *InputEng, 
                                    GraphicEngine *GraphEng, 
                                    AudioEngine *AudioEng );
          void SetState();
          void ExectuteSystemLogic();
             
             
      private:
              
          Engine2d      *ParentEngine;
          InputEngine   *InputCont;
          GraphicEngine *GraphicCont;
          AudioEngine   *AudioCont;

};



#endif // SYSTEMENGINE_H
