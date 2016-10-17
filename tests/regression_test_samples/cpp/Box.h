/// \file Box.h
/// \author Jared Chidgey
/// \date
/// \brief 

#ifndef BOX_H
#define BOX_H

#include <string>
#include <fstream>

#include "Line.h"

/// \brief Class represents a box on the game board.
typedef class Box
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Components
		/// \brief The box's corner dots.
		DOT														*dots[4];

		/// \brief The box's edge lines.
		LINE													*lines[4];
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//State
		/// \brief The box is enclosed
		bool													enclosed;

		/// \brief Player owner.
		int														owner;
		//-------------------------------------------------------------------------------//

		//private functions
		bool													write(std::fstream &file);
		bool													read(std::fstream &file);

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Constructor
		/// \brief Class constructor.
																Box();

		/// \brief Class destructor
																~Box();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Capturing
		// \brief Set player as owner of the box.
		bool													capture(int player_id);

		/// \brief test if the box is captured.
		bool													captured()							{ return enclosed; }

		/// \brief Returns the owner of the box.
		int														get_owner()							{ return owner; }

		/// \brief Mark the box as enclosed.
		void													enclose()							{ enclosed = true; }

		/// \brief Mark the box as open.
		void													open()								{ enclosed = false; }

		/// \brief Rates box according to how close to being captured it is.
		int														rate();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Components
		/// \brief Set the box's points.
		bool													set_points(DOT** new_dots);

		/// \brief Set the box's lines.
		bool													set_lines(LINE** new_lines);

		/// \brief Set the box's points.
		bool													set_points(DOT* d1, DOT* d2, DOT* d3, DOT* d4);

		/// \brief Set the box's lines.
		bool													set_lines(LINE* l1, LINE* l2, LINE* l3, LINE* l4);

		/// \brief Returns an array of four dots correspnding to this box.
		DOT**													get_dots()							{ return dots; }

		/// \brief Returns an array of four lines correspoinding to thsi box.
		LINE**													get_lines()							{ return lines; }

		bool													test_box(int player_id);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		bool													save(std::fstream &file);
		bool													load(std::fstream &file);
		//-------------------------------------------------------------------------------//

}BOX,*PBOX;

#endif
