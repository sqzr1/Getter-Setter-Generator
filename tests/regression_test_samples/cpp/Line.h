/// \file Line.h
/// \author Jared Chidgey
/// \date
/// \brief

#ifndef LINE_H
#define LINE_H

#include <fstream>

#include "Dot.h"

/// \brief Class represents a line on the game board.
typedef class Line
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Components
		/// \brief Dots/Points defining the line.
		DOT*													connections[2];

		/// \brief Is the line drawn.
		bool													drawn;

		/// \brief Id of the player owner.
		int														owner;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private functions
		bool													write(std::fstream &file);

		bool													read(std::fstream &file);
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		
		//*****************************************************//
		//-------------------------------------------------------------------------------//Construction
		/// \brief Class constructor.
																Line();

		/// \brief Class destructor.
																~Line();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Data
		/// \brief Mark the line claimed.
		void													draw_line()							{ drawn = true; }

		/// \bridf Mark the line not claimed.
		void													errase_line()						{ drawn = false; }

		/// \brief Returns whether the line is claimed.
		bool													is_drawn()							{ return drawn; }
		
		/// \brief Sets the owner of the line.
		void													set_owner(int player_id);

		/// \brief Returns the owner of the line.
		int														get_owner()							{ return owner; }
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Poinst/Dots
		/// \brief Set the points that define the line.
		bool													set_points(DOT* ptr1, DOT* ptr2);

		/// \brief Returns the first dot of the line.
		DOT*													pointer_1()							{ return connections[0]; }

		/// \brief Returns the second dot of the line.
		DOT*													pointer_2()							{ return connections[1]; }
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		bool													save(std::fstream &file);

		bool													load(std::fstream &file);
		//-------------------------------------------------------------------------------//

}LINE,*PLINE;

#endif // LINE_H
