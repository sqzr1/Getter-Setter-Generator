/// \file Game_Object.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_OBJECT_H
#define GAME_OBJECT_H

#include "Game_Entity.h"

/// \brief Class represents an object within the game

typedef class Game_Object : public Game_Entity
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//object data
		/// \brief Objects state.
		int														state;

		/// \brief Class data.
		bool													initialised;

		/// \brief Sound effect.
		PSAMPLE													s_effect;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		/// \brief Initialise the object.
		void													init(PTERRAIN terrain);
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Object();

		/// \brief Class destructor.
																~Game_Object();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the objects state.
		void													update(PTERRAIN terrain);

		/// \brief Renders the object.
		void													render();

		/// \brief Unimplemented here.
		void													hook_camera(PCAMERA camera) {}

		/// \brief Unimplemented here.
		void													zoom(float dir) {}

		/// \brief Interacts with another game entity
		void													interact(Game_Entity* other);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load entity data from a file(string).
		bool													load(string filename);

		/// \brief Load entity data from a file(fstream)
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}OBJECT,*POBJECT;

#endif // GAME_OBJECT_H

