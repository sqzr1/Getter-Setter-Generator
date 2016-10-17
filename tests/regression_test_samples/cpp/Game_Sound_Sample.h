/// \file Game_Sound_Sample.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef _GAME_SOUND_SAMPLE_H
#define _GAME_SOUND_SAMPLE_H

#include "DX_Manager.h"

/// \brief Class contains a sound sample to play. Non 3d sound.

/// This particular class is apropriate for short sounds as in sound effects,
/// and is not a 3 dimensional sound.
/// For longer data, use Game_Sound_Sample_Stream.
/// Samples can be played multiple times.
/// This class contains and maintains a sound, and its associated data and functionality.

typedef class Game_Sound_Sample
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Pointer to the Sound Manager Instance.
		PSOUND												sound;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//data
		/// \brief Name/filename of the sample.
		string													name;

		/// \brief Channel that the sample is playing on.
		int														channel;

		/// \brief Data structure containing sample data.
		FSOUND_SAMPLE*											sample;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Sound_Sample();

		/// \brief Non standard class constructor.
																Game_Sound_Sample(string filename);

		/// \brief Class destructor
																~Game_Sound_Sample();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//actions
		/// \brief Begins playing segment
		void													play();

		/// \brief Pauses currently playing segment.
		void													pause();

		/// \brief Stops a plying segment.
		void													stop();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//setters
		/// \brief Sets the number of times to loop a sound.
		void													set_repeat(unsigned int mode);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Getters
		/// \brief Retruns true if the segment is playing.
		bool													playing();

		/// \brief Returns true if the sample is paused.
		bool													paused();

		/// \brief Returns the repeat mode of the sound.
		int														get_repeat();

		/// \brief Returns current channel, -1 if none.
		int														get_channel()						{ return channel; }

		/// \brief Returns channel reference count.
		int														get_channel_ref();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//loading
		/// \brief Load the smaple.
		void													load(string filaname);
		//-------------------------------------------------------------------------------//


}SAMPLE,*PSAMPLE;

#endif // _GAME_SOUND_SAMPLE_H
