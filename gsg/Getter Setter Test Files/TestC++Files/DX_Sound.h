/// \file DX_Sound.h
/// \author Jared Chidgey
/// \author Corrupt Software

#ifndef _DX_SOUND_H
#define _DX_SOUND_H

#include "DX_Graphics.h"

#include <fmod.h>
#include <fmod_errors.h>

#include <string>

using namespace std;


/// \brief Class manages sound.

/// This class sets up fmod
/// and provides management and access.

typedef class DX_Sound
{
	friend class DX_Manager;
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton class instance.
		static DX_Sound*										_instance;

		/// \brief Private constructor.
																DX_Sound();

		/// \brief Private class destructor.
																~DX_Sound();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Pointer to DX Manager instance
		PGRAPHICS									graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Settings
		/// \brief Driver to use.
		int													driver;

		/// \brief Frequency.
		int													frequency;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton Instancer.
		static DX_Sound*							Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new DX_Sound;
																	}

																	return _instance;
																}

		/// \brief Singleton destroyer.
		static void										Release()
																{
																	if(_instance)
																	{
																		delete _instance;
																		_instance = 0;
																	}
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//initialise
		/// \brief Class initialiser.
		bool													init();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//action
		/// \brief Update 3d sound engine.
		void													update();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//setters
		/// \brief Set listener attributes.

		/// The attributes that are required are the isteners position
		/// velocity, and the vectors representing its forward and up directions.
		void													set_listener_position(D3DXVECTOR3 pos, D3DXVECTOR3 vel, D3DXVECTOR3 forward, D3DXVECTOR3 up);

		/// \brief Sets master volume.
		void													set_master_volume(int new_vol);

		/// \brief Sets channel volume.
		void													set_volume(int channel, int new_vol);

		/// \brief Sets the position/velocity of the listener for 3d sound.

		/// \brief Set listener attributes.
		void													set_listener();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//getters
		/// \brief Get master volume.
		int														get_master_volume();

		/// \brief Get channel volume.
		int														get_volume(int channel);
		//-------------------------------------------------------------------------------//

}SOUND,*PSOUND;

#endif // _DX_SOUND_H
