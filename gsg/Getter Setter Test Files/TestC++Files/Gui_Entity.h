/// \file Gui_Entity.h
/// \author Jared Chidgey

#ifndef GUI_ENTITY_H
#define GUI_ENTITY_H

#include <d3d9.h>
#include <d3dx9.h>

#include <fstream>
#include <string>

#include "DX_Manager.h"

using namespace std;

const int GUI_TYPE_BASE = 0;
const int GUI_TYPE_ENTITY = GUI_TYPE_BASE;

/// \brief base class of gui objects
/// This class is the base class from which all gui
/// objects inherit, it provides a base level functionality of
/// recording the rect at which the object visually exists

typedef class Gui_Entity
{
																																			//
																																			//protected declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	protected:
		//*****************************************************//
		//-------------------------------------------------------------------------------//display data
		/// \brief Physical location.
		D3DXVECTOR3 							location;

		/// \brief Space that the button takes up
		RECT												area;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//other data
		/// \brief Width of the buttons image file.
		int													file_width;

		/// \brief Height of the buttons image file.
		int													file_height;

		/// \brief Image file for the sprite.
		string 												address;

		/// \Brief Represents the object type (for file io)
		int													type;
		//-------------------------------------------------------------------------------//
																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Constructor.
																Gui_Entity();

		/// \brief Nonstandard class constructor.
																Gui_Entity(float new_x, float new_y);

		/// \brief virtual Destructor.
		virtual												~Gui_Entity() {}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//button data
		/// \brief Virtual function sets entity area.
		virtual bool										set_area(RECT new_area) = 0;

		/// \brief Returns the area bounded by the button.
		virtual RECT									get_area() = 0;

		/// \brief Virtual function sets location.
		virtual bool										set_location(D3DXVECTOR3 new_loc) = 0;

		/// \brief Sets the z-coord of existence.
		bool													set_z(FLOAT new_z);

		/// \brief Gets the location of the entity.
		D3DXVECTOR3							get_location();

		/// \brief Sets the type of the object.
		bool													set_type(int new_type);

		/// \brief Gets the objects type.
		int													get_type();

		/// \brief Virtual functions sets physical existence.
		virtual bool										set_attributes(int new_w, int new_h) = 0;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//animation
		/// \brief Virtual draw function.
		virtual void										display_frame(PGRAPHICS graphics) = 0;

		/// \brief Virtual function sets entity image.
		virtual bool										set_sprite(string new_address) = 0;

		/// \brief Virtual function sets animation flags.
		virtual void										set_anim_flags(int new_flag) = 0;

		/// \brief Virtual function to see if the buuton is on focus
		virtual bool										is_focused_on(int m_x, int m_y) = 0;

		/// \brief Virtual function to detect mouse clicks.
		virtual bool										is_clicked_on(int m_x, int m_y) = 0;

		/// \brief Virtual function to retur focus state.
		virtual bool										item_focused() = 0;
		//-------------------------------------------------------------------------------//

		virtual void										debug(PGRAPHICS graphics) = 0;

		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Data io, file via a filename.
		virtual bool										load(string filename) = 0;

		/// \brief Data io, file via a fstream.
		virtual bool										load(fstream &file) = 0;
		//-------------------------------------------------------------------------------//


} GUI_ENTITY,*PGUI_ENTITY, **PTPGUI_ENTITY;

#endif // GUI_ENTITY_H
