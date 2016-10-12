#ifndef UPDATEBOX_H
#define UPDATEBOX_H

#include <windows.h>
#include <string>
#include <vector>

using namespace std;


/// Constants ///
#define UB_FOCUSCELL      50001
#define UB_PROPERTYDIALOG 50002
#define UBP_CONTROLBKCOL  50003
#define UBP_CELLBKCOL     50004
#define UBP_CELLFRAMECOL  50005
#define UBP_CELLTXTCOL    50006
#define UBP_APPLYCHANGES  50007
#define UBP_CANCEL        50008

#define VERIFYSUCCESS(x) if(!x) return false;


/// Functions ///
void RegisterUpdateboxClass();
void RegisterUpdatePropertyDialogClass();
LRESULT CALLBACK UpdateBoxWndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);
LRESULT CALLBACK UpdatePropertyDialogWndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam);


/// Update Box Cell Object ///
struct ubCell {
     
      // Public Functions
      ubCell(HWND Hwnd, POINT p, int nWidth, int nHeight, COLORREF colourProperties[]);
      ~ubCell();
      bool drawControl(HDC hdc);
      bool drawEditControl();


      // Public Variables
      // COLUMN parentCol; // consider a parent object column
      POINT pos;
      POINT textPos;
      int width;
      int height;
      HWND hwnd;
      HRGN region;
      HBRUSH bgBrush;
      HBRUSH frameBrush;
      COLORREF textColour;
      string data;
      
};


/// Update Box Properties Object ///
struct UpdatePropertyDialog {
      
      // Public Functions
      UpdatePropertyDialog(HWND hParent, COLORREF colourProperties[]);
      ~UpdatePropertyDialog();
      void createGUI(HWND hwnd);
      bool openColourDialog(HWND hwnd, UINT controlID);
      void applyColourChange(UINT controlID, COLORREF newColour);
      
      
      // Public Variables
      HWND parentHwnd;
      COLORREF bkColour;
      COLORREF cellBkColour;
      COLORREF cellFrameColour;
      COLORREF cellTextColour;
              
};


/// Win32 Control - Similar to a List Box control but with more custom functionality ///
class updateBox {
      
      public:
           // Public Variables
           ubCell *focusCell;
           ubCell *prevFocusCell;
           bool userDesignatedDraw;
           bool initialiseDraw;
           bool newColourAttrib;
           
           // Public Functions
           updateBox(HWND Hwnd, POINT p);
           ~updateBox();
           ubCell* addCell();
           void setDimensions(int nWidth, int nHeight);
           void setFocusCell();
           bool drawControl(HDC hdc);
           bool drawFocusCell();
           bool drawDefaultCell(HDC hdc);
           void redrawControl(HDC hdc);
           bool inCellRgn(int mouse_x, int mouse_y);
           ubCell* findSelection(int mouse_x, int mouse_y);
           void SelectCell(int mouse_x, int mouse_y);
           void eraseRgn();
           void openPropertyDialog(HWND hwnd);
           void applyChanges(HWND hwnd, UpdatePropertyDialog *upd);
           
           // Efficent Alternative Functions
           bool inCellRgnEffic(int mouse_x, int mouse_y);
           ubCell* findSelectedCell(vector <ubCell*> &v, int mouse_x, 
                                    int mouse_y);
           
            
      private:
           POINT pos;
           int width;
           int height;
           int cellHeight;
           HWND hwnd;
           HWND focusEdit;
           HRGN region; // Why HRGN & not RECT? So I can develop this class further to create controls that have irregular shapes
           HRGN cellRegion;
           HBRUSH bgBrush;
           HBRUSH frameBrush;
           COLORREF bkColour;
           COLORREF cellBkColour;
           COLORREF cellFrameColour;
           COLORREF cellTextColour;
           vector <ubCell*> cellList;
           //int columns;
           
};


#endif




