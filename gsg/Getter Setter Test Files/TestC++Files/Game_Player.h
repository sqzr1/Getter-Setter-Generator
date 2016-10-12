/// \file Game_Player.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_PLAYER_H
#define GAME_PLAYER_H

#include "Game_Entity.h"

const int MOVE_JUMP = 1;

const string PLAYER_BEGIN = "[BEGIN_PLAYER]";
const string PLAYER_END = "[END_PLAYER]";

const string PLAYER_POSITION = "[PLAYER_POSITION]";
const string PLAYER_ANIMATIONS = "[PLAYER_ANIMATION]";
const string PLAYER_COLLISION = "[PLAYER_COLLISION]";
const string PLAYER_STATS = "[PLAYER_STATS]";

/// \brief Class represents a playable character.

/// The is class represents a playable character, extended from a game entity
/// (and a chracter?)
typedef class Game_Player : public Game_Entity
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//states
		/// \brief Current state in relation to movement.
		int														movement_state;

		/// \brief Current character state.
		int														player_state;

		/// \brief Third person camera distance.
		float													third_distance;

		/// \brief Idle flag, allows/disables other actions.
		bool													idle;

		/// \brief Walking animatio switch.
		bool													left_foot;

		/// \brief Animation use.
		float													save_walk_flag;

		/// \brief Animation use.
		float													save_strafe_flag;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Player();

		/// \brief Class destructor.
																~Game_Player();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the character.
		void													update(PTERRAIN terrain);

		/// \brief Renders the character.
		void													render();

		/// \brief Hooks the camera to the players current position.
		void													hook_camera(PCAMERA camera);

		/// \brief Zoom's the camera.
		void													zoom(float dir);

		/// \brief Unimplemented.
		void													interact(Game_Entity* other) {}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load entity data from a file(string).
		bool													load(string filename);

		/// \brief Load entity data from a file(fstream)
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//


}PLAYER,*PPLAYER;

#endif // GAME_PLAYER_H

