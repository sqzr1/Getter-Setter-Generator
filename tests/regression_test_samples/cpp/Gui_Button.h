/// \file Gui_Button.h
/// \author Jared Chidgey

#ifndef GUI_BUTTON_H
#define GUI_BUTTON_H

#include <sstream>
#include <iostream>
#include <string>

#include "Gui_Entity.h"
#include "Game_Sound_Sample.h"

//Defines a gui entity derived type
//-------------------------------------------------------------------------------//
/// \brief Constant value representing a gui_entity derived type, represents gui_button.
const int GUI_TYPE_BUTTON = 1;

//animation bitfield constanst
//-------------------------------------------------------------------------------//
/// \brief Constant value for the animation bitfield.
const int ANIM_NONE = 0;
/// \brief Constant value for the animation bitfield.
const int ANIM_OVER = 1;
/// \brief Constant value for the animation bitfield.
const int ANIM_CLICK = 2;

//Button state constants
//-------------------------------------------------------------------------------//
/// \brief Constant value for the button state.
const int BS_NORMAL = 0;
/// \brief Constant value for the button state.
const int BS_OVER = 1;
/// \brief Constant value for the button state.
const int BS_CLICKED = 2;

const int FRAME_NORML = 0;
const int FRAME_OVER = 1;

using namespace std;

/// \brief GUI object of type button
/// This class represents a button on a GUI
/// it inherits puiblically from gui_entity.

typedef class Gui_Button : public Gui_Entity
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//image data
		/// \brief Buttons image.
		LPDIRECT3DTEXTURE9 										sprite;

		/// \brief Centre of the image(default 0,0,0).
		D3DXVECTOR3												centre;

		/// \brief Physical width.
		int														width;

		/// \brief Physical height.
		int														height;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//animation data
		/// \brief Indicates whether the button is animated
		bool 													is_animated;

		/// \brief Further animation flags.
		int 													animation;

		/// \brief Dynaic RECT array for animation frames.
		LPRECT 													frames;

		/// \brief Number of frames and size of the frames array.
		int														num_frames;

		/// \brief Current frame.
		int 													cur_frame;

		/// \brief alpha value (drawing)
		int														alpha;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//state data
		/// \brief Current state of the button.
		int														state;

		/// \brief Sets button action.
		int														action;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Flag indicating whether the objects resources exist.
		bool 													initialised;

		/// \brief Defines whether all cleanable objects have been cleaned.
		bool 													clean;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//sound data
		/// \brief Sound when button is first focused on.
		PSAMPLE													over;

		/// \brief Sound when  button is clicked.
		PSAMPLE													click;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		/// \brief Private function calculates current frame.
		void													calculate_frame();

		/// \breif Reads text file data.
		bool													read_txt(fstream &file);
		//-------------------------------------------------------------------------------//

		virtual void											debug(PGRAPHICS graphics);

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Gui_Button();

		/// \brief Nonstandard class constructor.
																Gui_Button(int new_x, int new_y);

		/// \brief Class destructor.
																~Gui_Button();

		/// \brief Cleanup function.
		void													cleanup();
		//-------------------------------------------------------------------------------//

				/// \brief displays current frame.
		void													display_frame(PGRAPHICS graphics);


		//*****************************************************//
		//-------------------------------------------------------------------------------//animayion functions
		/// \brief Sets the frames for animation.
		bool													set_frames(string filename);

		/// \brief Sets the image file to load as the sprite.
		bool													set_sprite(string new_address);

		/// \brief Sets the animation types for the button.
		void													set_anim_flags(int new_flag);

		/// \brief Loads an image intot the sprite.
		bool													load_texture(PGRAPHICS graphics);

		/// \brief Sets mouse selection coordinates.
		bool													set_area(RECT new_area);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//get data
		/// \brief Returns the area bounded by the button.
		RECT													get_area();

		/// \brief Tests to see if the buuton is on focus.
		bool													is_focused_on(int m_x, int m_y);

		/// \brief Sends clicked message if button is in focus.
		bool													is_clicked_on(int m_x, int m_y);

		/// \brief Tests to see if the button state is "focused".
		bool													item_focused();

		/// \brief Sets the location of the button.
		bool													set_location(D3DXVECTOR3 new_loc);

		/// \brief  Sets physical existence.
		bool													set_attributes(int new_w, int new_h);

		//*****************************************************//
		//-------------------------------------------------------------------------------//filei io
		/// \brief Data io, file via a filename, according to.
		bool													load(string filename);

		/// \brief Data io, file via a fstream.
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}GUI_BUTTON,*PGUI_BUTTON;

#endif
