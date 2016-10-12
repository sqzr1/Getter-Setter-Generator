/// \file State_In_Game.h
/// \author Jared Chdgey
/// \author Student No. 11345826

#ifndef STATE_IN_GAME_H
#define STATE_IN_GAME_H

#include "State_Base.h"
#include "State_Menu.h"

#include "Game_Region.h"
#include "Game_Player.h"
#include "Game_Crates.h"

#include "Camera.h"

#include "Game_HUD.h"

/// \brief State class controls in game state.

/// This class represents the ingame state, and controls the variables
/// data and behaviour associated with the in game state.

typedef class State_In_Game : public State_Base
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static State_In_Game*									_instance;

		/// \brief Private constructor.
																State_In_Game();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Pointer to DX Manager Instance.
		PGRAPHICS												graphics;

		/// \brief Pointer to DI Manager Instance.
		PDINPUT													input;
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//game specific
		/// \brief Camera object, representing a 3d view.
		PCAMERA													cam;

		/// \brief Game region
		PREGION													region;

		D3DXVECTOR3												position;

		/// \brief Whether the camera is free to roam of hooked to the player.
		bool													cam_free;

		/// \brief Player entity.
		PENTITY													entity;

		/// \brief Game HUD
		HUD														hud;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Logs whether the state has been initialised.
		bool													initialised;

		/// \brief Resource state of the object.
		bool													clean;

		/// \brief Tracks wireframe rendering.
		bool													wire_frame;

		/// \brief Tracks scene lighting.
		bool													lighting;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		/// \brief Initialisation function.
		void													init();

		/// \brief Toggles wiremesh mode.
		void													toggle_wireframe();

		/// \brief Toggles scene lighting.
		void													toggle_light();
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static State_In_Game*									Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new State_In_Game;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~State_In_Game();

		/// \brief Cleaning function
		void													clean_up();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates object state.
		State_Base*												update();

		/// \brief Renders current state.
		void													render();
		//-------------------------------------------------------------------------------//

}STATE_IN_GAME,*PSTATE_INN_GAME;

#endif
