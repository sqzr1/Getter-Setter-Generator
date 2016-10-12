/// \file Menu_NewGame.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef MENU_NEWGAME_H
#define MENU_NEWGAME_H

#include "Menu_Layer.h"
#include "Menu_Main.h"

typedef class Menu_NewGame : public Menu_Layer
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Menu_NewGame*					_instance;

		/// \brief Private class constructor.
																Menu_NewGame();
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief State switching token.
		bool													start_game;

		/// \brief Display message 1
		string												message_1;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Menu_NewGame*					Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Menu_NewGame;
																	}

																	return _instance;
																}

		/// \brief Class constructor.
																~Menu_NewGame();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the menu layer's state.
		Menu_Layer*									update();

		/// \brief Renders the layer.
		void													render();

		/// \brief Indicates a state switch to the active game state.
		bool													start();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load the layer from a file (string).
		bool													load(string filename);

		/// \brief Load the layer from a file (stream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}MENU_NEWGAME,*PMENU_NEWGAME;

#endif // MENU_NEWGAME_H

