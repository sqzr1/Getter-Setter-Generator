/// \file GUI_List.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GUI_LIST_H
#define GUI_LIST_H

#include "GUI_Entity.h"
#include "GUI_Button.h"

typedef class GUI_List : public GUI_Entity
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//image data
			/// \brief Buttons image.
		LPDIRECT3DTEXTURE9 				sprite_sheet;

		/// \brief Centre of the image(default 0,0,0).
		D3DXVECTOR3							centre;

		/// \brief Physical width.
		int													width;

		/// \brief Physical height.
		int													height;
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//scroll buttons
		/// \brief Button on left of list.
		GUI_BUTTON								button_left;

		/// \brief Button on right of list.
		GUI_BUTTON								button_right;
		//-------------------------------------------------------------------------------//


																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
}GUI_LIST,*PGUI_LIST

#endif // GUI_LIST_H

