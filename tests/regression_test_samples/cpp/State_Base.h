/// \file State_Base.h
/// \author Jared Chidgey

#ifndef STATE_BASE_H
#define STATE_BASE_H

#include "DX_Manager.h"

/// \brief Purely abstract class(Singleton).
/// This class provides a basis for all other
/// states to derive themselves from.

typedef class State_Base
{
																																			//
																																			//protected declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	protected:
		/// \brief Singleton instance.
		static State_Base* 							_instance;

		/// \brief Private class constructor.
																State_Base();

		/// \brief Pointer to DX manager instance;
		PGRAPHICS									graphics;

		/// \brief Pointer to DInput manager instance.
		PDINPUT											input;

		/// \brief Clean state.
		bool													clean;

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		/// \brief Virtual class destructor.
		virtual												~State_Base() {}

		/// \brief Virtual update function.
		virtual State_Base*							update() = 0;

		/// \brief Virtua cleaning function.
		virtual void										clean_up() = 0;

		/// \brief Virtual rendering function.
		virtual void										render() = 0;

}STATE_BASE,*PSTATE_BASE;

#endif
