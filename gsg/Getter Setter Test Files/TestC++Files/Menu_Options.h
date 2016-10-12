/// \file Menu_Options.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef MENU_OPTIONS_H
#define MENU_OPTIONS_H

#include "Menu_Layer.h"

typedef class Menu_Options : public Menu_Layer
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Menu_Options*						_instance;

		/// \brief Private class constructor.
																Menu_Options();
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Menu_Options*						Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Menu_Options;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~Menu_Options();
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

}MENU_OPTIONS,*PMENU_OPTIONS;

#endif // MENU_OPTIONS_H

