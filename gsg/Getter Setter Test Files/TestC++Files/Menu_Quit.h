/// \file Menu_Quit.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef MENU_QUIT_H
#define MENU_QUIT_H

#include "Menu_Layer.h"

/// \brief A token class used to switch states.
/// This class does little, but enables switching into
/// the exit state.

typedef class Menu_Quit : public Menu_Layer
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Menu_Quit*							_instance;

		/// \brief Private class constructor.
																Menu_Quit();
		//-------------------------------------------------------------------------------//
																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Menu_Quit*							Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Menu_Quit;
																	}

																	return _instance;
																}

		/// \brief Class  destructor.
																~Menu_Quit();
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


}MENU_QUIT,*PMENU_QUIT;

#endif // MENU_QUIT_H

