/// \file Menu_Main.cpp
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef MENU_MAIN_H
#define MENU_MAIN_H

#include "Menu_Layer.h"

#include <sstream>

using namespace std;

/// \brief Class acts as the main interface to the game.
/// This class is the top level of the interface hiercachy
/// ivloves more hardcoding then a dynamic layer.

typedef class Menu_Main : public Menu_Layer
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Menu_Main*							_instance;

		/// \brief Class constructor.
																Menu_Main();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//GUI widgets
		/// \brief Background image for the menu layer.
		GUI_BUTTON								backing;

		/// \brief Basic gui_button object acts as a label.
		GUI_BUTTON								header;

		/// \brief Linked list of gui widgets.
		vector<PGUI_ENTITY>					widgets;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Menu_Main*							Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Menu_Main;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~Menu_Main();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the menu layer's state.
		Menu_Layer*									update();

		/// \brief Renders the layer.
		void													render();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load the layer from a file (string).
		bool													load(string filename);

		/// \brief Load the layer from a file (stream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}MENU_MAIN,*PMENU_MAIN;

#endif // MENU_MAIN_H

