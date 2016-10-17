/// \file Game_Gold.h
/// \author Jared Chidgey
/// \author Corrupt Software

#ifndef GAME_GOLD_H
#define GAME_GOLD_H

#include "DX_Manager.h"

#include <fstream>
#include <string>

#include "Simple_Animation.h"
#include "Game_Collision.h"
#include "Game_Terrain.h"
#include "Game_Sound_Sample.h"

using namespace std;

const string BEGIN_ITEM = "[BEGIN_ITEM]";
const string END_ITEM = "[END_ITEM]";

const string ITEM_NAME = "[ITEM_NAME]";
const string ITEM_VALUE	 = "[ITEM_VALUE]";
const string ITEM_PICTURE = "[ITEM_PICTURE]";
const string ITEM_COLLISION = "[ITEM_COLLISION]";
const string ITEM_ANIMATION = "[ITEM_ANIMATION]";
const string ITEM_SOUNDEFFECT = "[ITEM_SOUNDEFFECT]";

typedef class Game_Gold
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphics interface.
		PGRAPHICS											graphics;

		/// \brief Timer interface (timed motion)
		PTIMER												timer;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//representation
		/// \brief Character animations.
		PSIMP_ANIM											animations;

		/// \brief Inventory pic.
		LPDIRECT3DTEXTURE9									pic;

				/// \brief Position in the world.
		D3DXVECTOR3											position;

		/// \brief Previous position.
		D3DXVECTOR3											prev_position;

		/// \brief Bounding collision.
		COLLISION											collision;

		/// \brief The approximate height of the object.
		float												height;

		/// \brief Turn angle.
		float 												turn_a;

		/// \brief Current animation.
		int													cur_anim;

		/// \brief Number of animations
		int													num_anims;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//sound effects
		/// \brief Sound effect.
		PSAMPLE												s_effect;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//item values
		/// \brief Amount of gold in instance.
		int													count;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Gold();

		/// \brief Class destructor.
																~Game_Gold();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Update gold state.
		void													update(PTERRAIN terrain);

		/// \brief Renders the gold in the 3d world.
		void													render();

		/// \brief Renders the gold as part of the an inventory.
		void													render_menu(float pos_x, float pos_y, float pos_z, int alpha);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interaction
		/// \brief Reverts to the previously stored position.
		inline void												revert()
																{
																	position = prev_position;
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//gold interface
		/// \brief Add gold to the intertaface.
		inline void												add_gold(int addition)
																{
																	count += addition;
																}

		/// \brief Gets the current count.
		inline int												get_count()
																{
																	return count;
																}

		/// \brief Plays interact sound.
		void													interact_sound();


		/// \brief Retrurns the coilision object.
		inline COLLISION										get_collision()
																{
																	return collision;
																}

		/// \brief Sets the position in the game world of the gold.
		inline void												set_position(D3DXVECTOR3 new_pos)
																{
																	position = new_pos;
																}

		/// \brief returns the current position
		inline D3DXVECTOR3										get_position()
																{
																	return position;
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load from file (string).
		bool													load(string filename);

		/// \brief Loads from a file (fstream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}GOLD,*PGOLD;

#endif // GAME_GOLD_H

