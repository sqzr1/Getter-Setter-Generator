/// \file HUD_Element.h.
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef HUD_ELEMENT_H
#define HUD_ELEMENT_H

#include "DX_Manager.h"

#include <d3d9.h>
#include <d3dx9.h>

#include <fstream>
#include <string>

#include "Timer.h"
#include "Stat.h"

using namespace std;

/// \brief Class abstracts Heads Up Display elements.

/// Actual elements derive from this class,
/// which provides some basic level functionality.

typedef class HUD_Element
{
																																			//
																																			//protected declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	protected:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphics interface.
		PGRAPHICS									graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//data
		/// \brief Position of element on the screen.
		D3DXVECTOR3							position;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																HUD_Element();

		/// \brief Virtual class destructor.
		virtual												~HUD_Element() {}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Update the element state.
		virtual void										update(STAT new_stat, string new_name) = 0;

		/// \brief Renders the current state.
		virtual void										render() = 0;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//position
		inline void										set_position(D3DXVECTOR3 new_pos)
																{
																	position = new_pos;
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Loads element from a file (string)
		bool													load(string filename);

		/// \brief Loads element from a file (fstream)
		virtual bool										load(fstream  &file) = 0;

}ELEMENT,*PELEMENT;

#endif // HUD_ELEMENT_H

