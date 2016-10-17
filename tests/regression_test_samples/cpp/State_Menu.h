/// \file State_Menu.h
/// \author Jared Chidgey

#ifndef STATE_MENU_H
#define STATE_MENU_H

#include <list>
#include <string>
#include <fstream>

#include <d3d9.h>
#include <d3dx9.h>

#include "State_Base.h"

#include "Menu_Layer.h"
#include "Menu_Main.h"
#include "Menu_Options.h"
#include "Menu_Quit.h"
#include "Menu_NewGame.h"

using namespace std;

/// \brief Singleton class representing a menu.
/// This singleton class represents and controls
/// the menu system within a game.

typedef class State_Menu : public State_Base
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton class instance.
		static State_Menu*							_instance;

		/// \brief Private constructor.
																State_Menu();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//menus
		/// \brief Main menu layer.
		PMENU_LAYER							main;

		/// \brief Options menu.
		PMENU_LAYER							options;

		/// \brief Active menu layer.
		PMENU_LAYER							active_layer;

		/// \brief Next menu layer.
		PMENU_LAYER							next_layer;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Control the menu layer.
		int													state;

		/// \brief Logs whether the state has been initialised.
		bool													initialised;

		/// \brief Resource state of the object.
		bool													clean;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		/// \brief Initialisation function.
		void													init();

		/// \brief Loads the game menu configurations file.
		void													load_menus();
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//conctruction
		/// \brief Singleton class instancer.
		static State_Menu*							Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new State_Menu;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~State_Menu();

		/// \brief Clean up function.
		void													clean_up();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates menu state on current input buffer (no update).
		State_Base*										update();

		/// \brief Calls all drawing functions.
		void													render();
		//-------------------------------------------------------------------------------//

}MENU,*PMENU;

#endif
