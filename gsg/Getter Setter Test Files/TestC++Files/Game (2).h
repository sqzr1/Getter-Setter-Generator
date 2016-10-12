/// \file Game.h
/// \author Jared Chidgey

#ifndef GAME_H
#define GAME_H

#include <stdio.h>

#include "DX_Manager.h"

#include "Camera.h"

#include "State_Base.h"
#include "State_Splash.h"
#include "State_Menu.h"
#include "State_Exit.h"

#include "Config.h"

/// \brief Apllication control class.

/// This class is the main anchor point for the application.
/// It manages high level game resources and controls game states.

typedef class Game
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief singleton instance.
		static Game*											_instance;

		/// \brief private constructor.
																Game();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Complete directx manager instance.
		PMANAGER												manager;

		/// \brief Pointer to the DX manager.
		PGRAPHICS												graphics;

		/// \brief Pointer to the DInput manager.
		PDINPUT													input;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//game states
		/// \brief Pointer to the current game sate.
		PSTATE_BASE												game_state;
		
		/// \brief Pointer to the next state to be loaded.
		PSTATE_BASE												next_state;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Flag indicating the resource sate of the object.
		bool													clean;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton class instancer.
		static													Game* Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Game();
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~Game();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//init
		/// \brief Clean up function.
		void													shutdown();

		/// \brief Initiates the game.
		bool													init(HINSTANCE new_inst, HWND new_hwnd);
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the logical parts of thew game.

		/// This function updates logical sections within the game:
		/// polling and responding to input, calculates values etc.
		void													logic();

		/// \brief Render the current scene.
		void													render();
		//-------------------------------------------------------------------------------//

}GAME,*PGAME;

#endif

