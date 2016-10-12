/// \file Game_Crates.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_CRATES_H
#define GAME_CRATES_H

#include "Game_Entity.h"
#include "Crate_Buffer.h"

typedef class Game_Crate : public Game_Entity
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief Crate instance.
		PCRATE_BUFFER										crate;

		/// \brief Texture.
		LPDIRECT3DTEXTURE9									texture;

		/// \brief Material
		D3DMATERIAL9										material;

		/// \brief Heal interval.
		float												heal_interval;

		/// \brief Current time.
		float												cur_heal_interval;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Classc constructor.
																Game_Crate();

		/// \brief Class destructor.
																~Game_Crate();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the state of the entity.
		void													update(PTERRAIN terrain);

		/// \brief Renders the player.
		void													render();

		/// \brief Unimplemented here.
		void													hook_camera(PCAMERA camera) {}

		/// \brief Interact with another game object.
		void													interact(Game_Entity* other);

		/// \brief Unimplemented here.
		void													zoom(float dir) {}

		/// \brief Sound effect.
		PSAMPLE													s_effect;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load entity data from a file(string).
		bool													load(string filename);

		/// \brief Load entity data from a file(fstream)
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}CRATE,*PCRATE;

#endif // GAME_CRATES_H

