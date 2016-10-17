/// \file HUD_Bar.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef HUD_BAR_H
#define HUD_BAR_H

#include <sstream>
#include <string>

#include "HUD_Element.h"

const string HEADER_BAR = "[HUD_BAR]";
const string FOOTER_BAR = "[/HUD_BAR]";

using namespace std;

/// \brief Represents (stat) data in the form of a progressive bar.

/// This class inherits from the HUD_Elements clss
/// and renders a prgressive bar based on its
/// class attributes.

typedef class HUD_Bar : public HUD_Element
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//image data
		/// \brief Anchor of the bar.
		D3DXVECTOR3							centre;

		/// \brief Graphics for the bar.
		LPDIRECT3DTEXTURE9				bar;

		/// \brief Alpha value to draw bar.
		int													alpha;
		//-------------------------------------------------------------------------------//

		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Current stat state to display
		STAT												cur_stat;

		/// \brief Indeicates bar text mode.
		bool													text_mode;

		/// \brief Length of the bar
		float												length;

		/// \brief stat name
		string 												name;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//drawing data
		/// \brief Points of stat per piece.
		int													points_per_piece;

		/// \brief Pieces to draw next render loop.
		int													pieces_to_draw;

		/// \brief Current filler piece to use.
		int 													cur_piece;
		//-------------------------------------------------------------------------------//


																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																HUD_Bar();

		/// \brief Class destructor.
																~HUD_Bar();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Update the element state.
		void													update(STAT new_stat, string new_name);

		/// \brief Renders the current state.
		void													render();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Loads element from a file (fstream)
		bool													load(fstream  &file);
		//-------------------------------------------------------------------------------//

}BAR,*PBAR;

#endif // HUD_BAR_H

