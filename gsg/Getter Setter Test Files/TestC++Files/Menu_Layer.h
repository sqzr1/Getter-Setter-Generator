/// \file Menu_Layer.h
/// \author Jared Chidgey

#ifndef MENU_LAYER_H
#define MENU_LAYER_H

#include <vector>

#include "DX_Manager.h"

#include "Gui_Entity.h"
#include "Gui_Button.h"

const int ML_STATE_INVIS = 0;
const int ML_STATE_VIS = 1;
const int ML_STATE_FRONT = 2;
const int ML_STATE_BACK = 4;

/// \brief Abstract class represents a menu layer.
/// This class abstractly represents a menu layer,
/// actual implementations inherit from this.

typedef class Menu_Layer
{
																																			//
																																			//protected declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	protected:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Pointer to DX Manager instance.
		PGRAPHICS									graphics;

		/// \brief Pointer to DInput Manager instance.
		PDINPUT											input;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief For singletons menu's.
		static Menu_Layer*						Instance()
																{
																	return NULL;
																}

		/// \brief Class constructor.
																Menu_Layer();

		/// \brief Class destructor.
		virtual												~Menu_Layer() {};
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Causes menu to parse input.
		virtual Menu_Layer*						update() = 0;

		/// \brief Draws the menu layer.
		virtual void										render() = 0;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Loads a menu_layer from a file stream.
		virtual bool										load(string filename) = 0;

		/// \brief Loads a menu_layer from a file stream.
		virtual bool										load(fstream &file) = 0;
		//-------------------------------------------------------------------------------//

}MENU_LAYER,*PMENU_LAYER;

#endif
