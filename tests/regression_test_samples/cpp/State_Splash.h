/// \file State_Splash.h
/// \author Jared Chidgey

#ifndef STATE_SPLASH_H
#define STATE_SPLASH_H

#include <windows.h>

#include "State_Base.h"

#include "DX_Sound.h"

#include "Game_Sound_Sample.h"

#include <sstream>
#include <string>

/// \brief Splash screen state class.
/// This class represents splash screens shown
/// usually at the beggining of the game.

typedef class State_Splash : public State_Base
{
																									//
																									//private declarations
	//////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static State_Splash*									_instance;

		/// \brief Private constructor.
																State_Splash();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//splash data
		/// \brief Counts frames.
		int														frame_count;

		/// \brief Splash screen image.
		LPDIRECT3DTEXTURE9										background;

		/// \brief Fade out.
		int														fading;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Logs whether the state has been initialised.
		bool													initialised;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		/// \brief Initialisation function.
		void													init();
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief singleton instancer.
		static State_Splash*									Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new State_Splash;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~State_Splash();

		/// \brief Clean up function.
		void													clean_up();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief State update function.
		State_Base*												update();

		/// \brief State rendering function.
		void													render();
		//-------------------------------------------------------------------------------//

}SPLASH,*PSPLASH;

#endif
