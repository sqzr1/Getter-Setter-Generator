/// \file State_Exit.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef STATE_EXIT_H
#define STATE_EXIT_H

#include "State_Base.h"

#include <fstream>
#include <string>

#include "Game_Sound_Sample.h"

using namespace std;

/// \brief Class representing the exit state.
/// This class represents the exit state,
/// and shuts down the game and displays the credit roll.

typedef class State_Exit : public State_Base
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static State_Exit*										_instance;

		/// \brief Private class constructor.
																State_Exit();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//credit data
		/// \brief String holding the lines to be displayed as the credits.
		string**												credits;

		/// \brief Number of headings/grounps.
		int														headings;

		/// \brief Number of lines under each heading.
		int*													num_lines;

		/// \brief controls timing of the exit sxreen.
		int														last_line;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//sound data
		/// \brief Music during credits
		PSAMPLE													music;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Logs whether the state has been initialised.
		bool													initialised;

		/// \brief Counting frames.
		int														frame_count;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		/// \brief Initialisation function.
		void													init();

		/// \brief Loads text file with credits.
		bool													load_credits(string filename);
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief singleton instancer.
		static State_Exit*										Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new State_Exit;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~State_Exit();

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

}EXIT,*PEXIT;

#endif
