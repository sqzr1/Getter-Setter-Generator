/// \file Game_HUD.
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_HUD_H
#define GAME_HUD_H

#include "DX_Manager.h"

#include <d3d9.h>
#include <d3dx9.h>

#include <fstream>
#include <string>

#include "Game_Player.h"

#include "Game_Region.h"

#include "HUD_Bar.h"

using namespace std;

/// \brief Class represents the Heads Up Display

/// Displays any immediately required player statistics, and
/// other valuable and useful infromation.

typedef class Game_HUD
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphics interface.
		PGRAPHICS									graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief The health bar.
		BAR												health_bar;

		/// \brief The speed bar.
		BAR												speed_bar;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//display values
		/// \brief Character stats class hooked into
		PCHAR_STATS								stats;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_HUD();

		/// \brief Class destructor.
																~Game_HUD();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the state of the HUD from the input entity, and Region.
		void													update(PENTITY entity, PREGION region);

		/// \brief Renders the current state of the HUD.
		void													render();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Loads HUD setup from a file (string).
		bool													load(string filename);

		/// \brief Loads HUD setup from a file (fstream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}HUD,*PHUD;

#endif // GAME_HUD_H

