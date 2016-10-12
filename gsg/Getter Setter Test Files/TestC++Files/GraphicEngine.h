/*
    Header file: My own simple 2d drawing engine where object's are
                 sent to a queue inside the class & then drawn onto
                 the main client window.
*/


#ifndef GRAPHICENGINE_H
#define GRAPHICENGINE_H


#include <windows.h>
#include <cstdlib>
#include <queue>

#include "2dEngine.h"

using namespace std;


class GraphicEngine
{
      public:
             
          GraphicEngine( Engine2d *ParentEng );
          ~GraphicEngine();
          void StoreSiblingEngines( SystemEngine *SystemEng, 
                                    InputEngine *InputEng, 
                                    AudioEngine *AudioEng );
          void SetHwnd( HWND Hwnd );
          void CopyWindowHDC( HWND Hwnd, HDC WindowHDC );
          int  AddToDrawQueue( Object *Obj );
          bool ExecuteDrawLogic( HDC WindowHDC );
                       
             
      private:
              
          Engine2d     *ParentEngine;
          SystemEngine *SystemCont;
          InputEngine  *InputCont;
          AudioEngine  *AudioCont;
          
          HWND hwnd;
          RECT ClientRect;
          HDC BufferCanvas;
          HBITMAP hBlt;
          queue <Object*> DrawQueue;

};


#endif // GRAPHICENGINE_H
