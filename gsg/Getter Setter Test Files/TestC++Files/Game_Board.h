/// \file Game_Board.h
/// \author Jared Chidgey
/// \date 2007
/// \brief

#ifndef GAME_BOARD_H
#define GAME_BOARD_H

#include "Dot.h"
#include "Line.h"
#include "Box.h"

#include "Display.h"

/// \brief Class represents the game board.

typedef class Game_Board
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Descritors
		/// \brief Game area width
		int 													width;

		/// \brief Game area height.
		int														height;

		/// \brief Drawing offset x.
		int														start_x;

		/// \brief Drawing offset y
		int														start_y;

		/// \brief Dot size.
		int 													dot_radius;

		/// \brief Dot spacing
		int 													dot_spacing;

		/// \brief Game area rect.
		RECT													game_area;

		// \brief Game area rect.
		RECT													line_1;

		// \brief Game area rect.
		RECT													line_2;

		/// \brief Calculate game area RECT.
		void													calculate_game_area();
		//-------------------------------------------------------------------------------//

	
		//*****************************************************//
		//-------------------------------------------------------------------------------//Entities
		/// \brief Array of dots, w*h
		DOT**													world;

		/// \brief Array of lines, cols*rows
		LINE**													lines;

		/// \brief Line to draw as highlight.
		LINE*													highlight_line;

		/// \brief Previous line to draw as highlight.
		LINE*													prev_highlight_line;

		/// \brief Cooresponding boxes (w-1 * h-1)
		BOX**													boxes;

		/// \brief Number of rows.
		int														num_rows;

		/// \brief Array with collumn sizes.
		int*													num_cols;
		//-------------------------------------------------------------------------------//

	
																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Construction
		/// \brief Class Constructor.
																Game_Board();

		/// \brief Class Destructor
																~Game_Board();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Functionality
		/// \brief Initialises the board.
		void													init();

		/// \brief Draws the board.
		void													draw(HDC hdc, PDISP display);

		/// \brief Resets the board state
		
		/// Passing zero as either of the parameters causes the board
		/// to retain its previous size.
		void													reset(int new_w, int new_h);

		/// \brief Draw/Claim a line. >0 score if the player captures boxes. Uses mouse coords.
		int														draw_line(int m_x, int m_y, int active_id);

		/// \brief Draw/Claim a line. >0 score if the player captures a box. Uses linje space.
		int														draw_line_direct(int row, int column, int active_id);
		
		/// \brief Rates a line according to its boxes.
		int														rate_line(int row, int column);

		/// \brief Checks for any uncaptured boxes.

		/// If there is an uncaptured box, it is assigned to the current player,
		/// and the player's turn is NOT ended.
		int														check_boxes(int player_id);

		/// \brief Tests whether the board is finished.
		bool													finished(int total_scores);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Dimensnions
		/// \brief Set the board width.
		void													set_width(int new_w);

		/// \brief Get board width.
		int														get_width()					{ return width; }

		/// \brief Set the board height.
		void													set_height(int new_h);

		/// \brief Get board height.
		int														get_height()				{ return height; }

		/// \brief Get num_rows.
		int														get_num_rows()				{ return num_rows; }

		/// \brief Get num_cols.
		int														get_num_cols(int at);
		
		/// \brief Set the top left position of the board.
		void													set_starting(int new_x, int new_y);

		/// \brief Get starting x.
		int														get_start_x()				{ return start_x; }

		/// \brief Get Starting y.
		int														get_start_y()				{ return start_y; }

		/// \brief Reset dot positions.
		void													reset_dot_position();

		/// \brief Get game board rect.
		RECT*													get_game_rect()				{ return &game_area; }

		/// \brief Get game board rect.
		RECT*													get_line_1_rect()			{ return &line_1; }

		/// \brief Get game board rect.
		RECT*													get_line_2_rect()			{ return &line_2; }
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//display dimensions
		/// \brief Set the size of the dots.
		void													set_dot_radius(int new_radius);

		/// \brief Get the radius of the dots.
		int														get_dot_radius()				{ return dot_radius; }

		/// \brief Set the distance between dots.
		void													set_dot_spacing(int new_spacing);

		/// \brief Returns the distance between dots.
		int														get_dot_spacing()				{ return dot_spacing; }
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Retrieve elements
		/// \brief Returns a pointer to a dot corresponding to given coordinates.
		DOT*													get_dot(int row, int col);
		
		/// \brief Returns a pointer to a line corresponding to given coordinates.
		LINE*													get_line(int row, int col);

		/// \brief Returns the highlight line.
		LINE*													get_highlight_line()			{ return highlight_line; }

		/// \brief Returns the previous highlight line.
		LINE*													get_prev_highlight_line()		{ return prev_highlight_line; }
		
		/// \brief Returns a pointer to a box corresponding to given coordinates.
		BOX*													get_box(int row, int col);

		/// \brief Returns a pointer to a dot corresponding to given mouse oordinates.
		DOT*													get_dot_mouse(int m_x, int m_y);

		/// \brief Returns a pointer to a line corresponding to given mouse oordinates.
		LINE*													get_line_mouse(int m_x, int m_y);

		/// \brief Returns a pointer to a box corresponding to given mouse oordinates.
		BOX*													get_box_mouse(int m_x, int m_y);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Retrieve elements
		/// \brief True if the given coordinates are over a dot.
		bool													over_dot(int m_x, int m_y);

		/// \brief True if the given coordinates are over a line.
		bool													over_line(int m_x, int m_y);

		/// \brief Sets the line the mouse is over as the highlightline.
		bool													over_line_highlight(int m_x, int m_y);

		/// \brief True if the given coordinates are over a line, hori will indicate if the line is horizontal.
		bool													over_line(int m_x, int m_y, bool &hori);

		/// \brief Sets the line the mouse is over as the highlightline, hori will indicate if the line is horizontal.
		bool													over_line_highlight(int m_x, int m_y, bool &hori);

		/// \brief True if the given coordinates are over a box.
		bool													over_box(int m_x, int m_y);
		//-------------------------------------------------------------------------------//

}BOARD,*PBOARD;

#endif // GAME_BOARD_H