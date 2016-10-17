/// \file Game_Region.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_REGION_H
#define GAME_REGION_H

#include "DX_Manager.h"
#include "Timer.h"

#include <fstream>
#include <string>
#include <vector>

#include "Game_Terrain.h"
#include "Sky_Box.h"
#include "Light_Scene.h"

#include "Game_Object.h"
#include "Game_Player.h"
#include "Game_Crates.h"
#include "Game_Sound_Sample.h"
#include "Game_Gold.h"

using namespace std;

/// \brief Represents a complete area with in the game.

/// This class encompases the terrain, sky box,
/// objects and npc's active within a region of play.

typedef class Game_Region
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphics interface.
		PGRAPHICS									graphics;

		/// \brief Timer interface.
		PTIMER											timer;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//region representation
		/// \brief The terrain of the region.
		PTERRAIN										terrain;

		/// \brief The sky of the region.
		PSKY_BOX									sky_box;

		/// \brief Lighting for the scene.
		PLSCENE										lighting;

		/// \brief The name of the region.
		string												name;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//objects
		/// \brief A tree.
		POBJECT													tree;

		/// \brief The lava pool.
		POBJECT													lava_pool;

		/// \brief The swamp ground.
		POBJECT													swamp;

		/// \brief Healing crate.
		PCRATE													heal_crate;

		/// \brief Speed healing crate.
		PCRATE													speed_heal_crate;

		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//gold
		/// \brief Gold.
		PGOLD													gold;

		/// \brief Number of spawn locations.
		int														num_gold;

		/// \brief current spawn location.
		bool*													gold_collected;

		/// \brief Actual spawn locations.
		D3DXVECTOR3*											spawn_locations;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//sound
		/// \brief Music for region.
		PSAMPLE													music;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief controls the initialisation state.
		bool													initialised;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Region();

		/// \brief Class destructor.
																~Game_Region();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//init
		/// \brief Initialises the class.
		void													init();
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the state of the terrain.
		void													update(PENTITY player);

		/// \brief Renders the terrain.
		void													render();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//access
		/// \brief Returns a pointer to the regions terrain.
		inline PTERRAIN											get_terrain()
																{
																	if(terrain)
																	{
																		return terrain;
																	}

																	return NULL;
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Loads region data from a file (string).
		bool													load(string filename);

		/// \brief Loads region data from a file (fstream)
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}REGION,*PREGION;

#endif // GAME_REGION_H

