/// \file Game_Sound_3d.h
/// \author Jared Chidgey
/// \date 29/06/2008

#ifndef _GAME_SOUND_3D_H
#define _GAME_SOUND_3D_H

#include "DX_Manager.h"

typedef class Game_Sound_3d
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Pointer to the DS Manager Instance.
		PSOUND											sound;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//data
		/// \brief Name/filename of the sample.
		string													name;

		/// \brief Channel that the sample is playing on.
		int														channel;

		/// \brief Data structure containing sample data.
		FSOUND_SAMPLE*							sample;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//3d attributes
		/// \brief Position of the source.
		D3DXVECTOR3								position;

		/// \brief Velocity of the source.
		D3DXVECTOR3								velocity;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Sound_3d();

		/// \brief Non standard class constructor.
																Game_Sound_3d(string filename);

		/// \brief Class destructor
																~Game_Sound_3d();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//actions
		/// \brief Begins playing segment
		void													play();

		/// \brief Update sound, call to update 3d data.
		void													update();

		/// \brief Pauses currently playing segment.
		void													pause();

		/// \brief Stops a plying segment.
		void													stop();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//setters
		/// \brief Sets the number of times to loop a sound.
		void													set_repeat(unsigned int mode);

		/// \brief Set sound position.
		void													set_position(D3DXVECTOR3 pos)			{ position = pos; }

		/// \brief Set sound velocity.
		void													set_velocity(D3DXVECTOR3 vel)			{ velocity = vel; }

		/// \brief Set minimum distance.
		void													set_min_distance(float minimum);

		/// \brief Set maximum distance.
		void													set_max_distance(float maximum);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Getters
		/// \brief Retruns true if the segment is playing.
		bool													playing();

		/// \brief Returns true if the sample is paused.
		bool													paused();

		/// \brief Returns the repeat mode of the sound.
		int													get_repeat();

		/// \brief Returns current channel, -1 if none.
		int													get_channel()												{ return channel; }

		/// \brief Returns channel reference count.
		int													get_channel_ref();

		/// \brief Returns the current position of the sound.
		bool													get_position(D3DXVECTOR3 &pos);

		/// \brief Returns the current velocity of the sound.
		bool													get_velocity(D3DXVECTOR3 &vel);

		/// \brief Returns the current min distance.
		float												get_min_distance();

		/// \brief Returns the current max distance.
		float												get_max_distance();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//loading
		/// \brief Load the smaple.
		void													load(string filaname);
		//-------------------------------------------------------------------------------//

}SOUND3D,*PSOUND3D;


#endif // _GAME_SOUND_3D_H
