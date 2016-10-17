/// \file Character_Stats.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef CHARACTER_STATS_H
#define CHARACTER_STATS_H

#include <windows.h>

#include <map>
#include <string>
#include <fstream>

#include "Stat.h"

using namespace std;

const STAT EMPTY_STAT (0, 0, 0);
const int EMPTY_INT = -1;

const string BEGIN_STATS = "[BEGIN_STATS]";
const string END_STATS = "[END_STATS]";

/// \brief Class represents a collection of character stats

/// ?

typedef class Character_Stats
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief Character name.
		string											name;

		/// \brief Maximum health.
		map<string, STAT>						stats;

		/// \brief Error token.
		bool												error;
		//-------------------------------------------------------------------------------//
																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//Construction
		/// \brief Class constructor.
															Character_Stats();

		/// \brief Copy constructor.
															Character_Stats(Character_Stats &rhs);

		/// \brief Class destructor.
															~Character_Stats();

		/// \brief Operator =.
		void												operator=(Character_Stats &rhs);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Data accessors
		/// \brief Gets the specified stat value.
		STAT											get_stat(string token);

		/// \brief Gets the specified stat value.
		bool												get_stat(string token, STAT &ret);

		/// \brief Sets the specified stat value.
		bool												set_stat(string token, STAT stat);

		/// \brief Updates the current value of the stat.
		bool												update_cur_val(string token, int new_val);

		/// \brief Sets the cur value to the maximum value.
		bool												set_to_max(string token);

		/// \brief Returns the current value of the stat.
		int												get_cur_val(string token);

		/// \brief Returns the current value of the stat.
		int												get_max_val(string token);

		/// \brief Returns the current value of the stat.
		bool												get_cur_val(string token, int &ret);

		/// \brief Returns the current value of the stat.
		bool												get_max_val(string token, int &ret);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//error control
		/// \brief Tests the error flag if not found result is returned.
		bool												error_occured();
		//-------------------------------------------------------------------------------//



		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Read data from file (string)
		bool												load(string filename);

		/// \brief Read data from a file (fstream)
		bool												load(fstream &file);

		/// \brief Write data to a file (string)
		bool												save(string filename);

		/// \brief Write data to a file (fstream)
		bool												save(fstream &file);
		//-------------------------------------------------------------------------------//

}CHAR_STATS,*PCHAR_STATS;

#endif // CHARACTER_STATS_H

