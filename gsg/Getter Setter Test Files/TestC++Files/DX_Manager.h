/// \file DX_Manager.h
/// \author Jared Chidgey
/// \author Student No. 11346826

#ifndef DX_MANAGER_H
#define DX_MANAGER_H

#include <string>

#include "DX_Graphics.h"
#include "DX_Input.h"
#include "DX_Sound.h"
#include "Timer.h"

#include "Config.h"
#include "Crate_Buffer.h"

using namespace std;

typedef class DX_Manager
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static DX_Manager*						_instance;

		/// \brief Private class constructor.
																DX_Manager();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphical interface.
		PGRAPHICS									graphics;

		/// \brief Input interface.
		PDINPUT											input;

		/// \brief Sound interface.
		PSOUND										sound;

		/// \brief Main configuration file.
		CONFIG											config;

		/// \brief Config file name.
		string												name;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Game continue state.
		bool													quit;

		/// \brief initialisation flag.
		bool													initialised;

		/// \brief Clean flag.
		bool													clean;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static DX_Manager*						Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new DX_Manager;
																	}

																	return _instance;
																}

		/// \brief Private class destructor.
																~DX_Manager();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//init/shut down
		/// \brief Initialises all of the devices
		bool													init(HINSTANCE hinst, HWND hwnd, int w, int h, bool wind);

		/// \brief Clean up function.
		void													clean_up();
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//main config file
		/// \brief Loads the main configuration file.
		bool													load_config(string filename);

		/// \brief Returns a pointer to the main configuration file.
		PCONFIG										get_config();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//quiting
		/// \brief Set the quit state.
		void													set_quit();

		/// \brief Test the quit state.
		bool													has_quit();
		//-------------------------------------------------------------------------------//

}MANAGER,*PMANAGER;

#endif
