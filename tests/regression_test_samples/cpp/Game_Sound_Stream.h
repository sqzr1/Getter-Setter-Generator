/// \file Game_Sound_Stream.h
/// \author Jared Chidgey
/// \date 28/06/2008

#ifndef _GAME_SOUND_STREAM_H
#define _GAME_SOUND_STREAM_H

#include "DX_Manager.h"

/// \brief Class contains a sound stream.

/// This particular class is apropriate for longer segments
/// of sound, such as background music or speech segments.
/// Segments cannot be played multiple times.
/// For sh

typedef class Game_Sound_Stream
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
		/// \brief Name/filename of the stream.
		string													name;

		/// \brief Channel that the stream is playing on.
		int														channel;

		/// \brief Data structure containing stream data.
		FSOUND_STREAM* 						stream;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Sound_Stream();

		/// \brief Non standard class constructor.
																Game_Sound_Stream(string filename);

		/// \brief Class destructor
																~Game_Sound_Stream();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//actions
		/// \brief Begins playing segment
		void													play();

		/// \brief Pauses currently playing segment.
		void													pause();

		/// \brief Stops a plying segment.
		void													stop();

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
		int													get_repeat();

		/// \brief Returns current channel, -1 if none.
		int													get_channel()					{ return channel; }

		/// \brief Returns channel reference count.
		int													get_channel_ref();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//loading
		/// \brief Load the smaple.
		void													load(string filaname);
		//-------------------------------------------------------------------------------//

}STREAM,*PSTREAM;

#endif // _GAME_SOUND_STREAM_H
