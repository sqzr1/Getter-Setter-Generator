/// \file Stat_Database.h
/// \author Jared Chidgey
/// \author Corrupt Software

#ifndef STAT_DATABASE_H
#define STAT_DATABASE_H

#include <fstream>
#include <string>

#include "Stat.h"
#include "Character_Stats.h"

using namespace std;

/// \brief Class provides a basic template and initialisation of character skills.

/// The class loads a template from file, and subsequent characters
/// (both NPC and PC) use this data to initialise their own list of skills.
/// This allows a general interface for interactions between game entities.

typedef class Stat_Database
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Stat_Database*						_instance;

		/// \brief Private class constructor.
																Stat_Database();
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//the template
		/// \brief Character stats template.
		CHAR_STATS								stats_template;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Stat_Database*						Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Stat_Database;
																	}

																	return _instance;
																}

		/// \brief Class destrutor.
																~Stat_Database();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//template
		/// \brief Returns a copy of the stat template
		CHAR_STATS								get_template();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load the template from a file (string).
		bool													load(string filename);

		/// \brief Loads the template from a file (fstream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}STAT_DATABASE,*PSTAT_DATABASE;

#endif // STAT_DATABASE_H
