/// \file Display.h
/// \author Jared Chidgey
/// \date 27/10/2008
/// \brief

#ifndef DISPLAY_H
#define DISPLAY_H

#include <windows.h>

/// \brief Class contains display data for the game.
typedef class Display
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//display colours
		/// \brief Line colour triple.
		int														line_colour[3];

		/// \brief Dot colour.
		int														dot_colour[3];

		/// \brief Dot is solid or a circle.
		bool													fill_dot;

		/// \brief Line thickness.
		int														line_thickness;

		/// \brief Background colour.
		int														background_colour[3];
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Pens and brushes
		/// \brief Pen for each player.
		HPEN													player_pen[4];

		/// \brief Pen for each player, thin.
		HPEN													player_pen_thin[4];

		/// \brief Pen for each player, higlighting lines.
		HPEN													player_pen_high[4];

		/// \brief Pen with which to draw the dots
		HPEN													dot_pen;

		/// \brief Pen with which to draw the lines.
		HPEN													line_pen;

		/// \brief Line Pen for hihlighted lines.
		HPEN													line_pen_high;

		/// \brief Null pen.
		HPEN													null_pen;
		
		/// \brief Fill brush.
		HBRUSH													fill;

		/// \brief Brush for each player.
		HBRUSH													player_brush[4];

		/// \brief Background brush.
		HBRUSH													background_brush;

		/// \brief Creates a brush.
		void													create_brush(HBRUSH &brush, int* colours, bool fillled);
		//-------------------------------------------------------------------------------//


																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Display();

		/// \brief Class destructor.
																~Display();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Pens
		/// \brief Creates the line pen.
		void													set_dot_pen();

		/// \brief Returns the line pen.
		HPEN													get_dot_pen()					{ return dot_pen; }

		/// \brief Creates the line pen.
		void													set_line_pen();

		/// \brief Returns the line pen.
		HPEN													get_line_pen()					{ return line_pen; }

		/// \brief Returns the line highlight pen.
		HPEN													get_line_pen_high()				{ return line_pen_high; }

		/// \brief Get Null Pen.
		HPEN													get_null_pen()					{ return null_pen; }

		/// \brief Create player pen.
		void													set_player_pen(int player_id, int red, int blue, int green);

		/// \brief Get player pen.
		HPEN													get_player_pen(int player_id);

		/// \brief Get player pen thin.
		HPEN													get_player_pen_thin(int player_id);

		/// \brief Get player pen line higlight.
		HPEN													get_player_pen_high(int player_id);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Brushes
		/// \brief Create a brush.
		void													create_brush(HBRUSH &brush, int red, int blue, int green, bool fillled);

		/// \brief Creates the background brush.
		void													set_background_brush(bool filled);

		/// \brief Returns the background brush.
		HBRUSH													get_background_brush()			{ return background_brush; }

		/// \brief Creates the fill brush.
		void													set_fill_brush(bool filled);

		/// \brief Returns the fill brush.
		HBRUSH													get_fill_brush()				{ return fill; }

		/// \brief Create player brush.
		void													set_player_brush(int player_id, int red, int blue, int green);

		/// \brief Get player brush.
		HBRUSH													get_player_brush(int player_id);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//display colours
		/// \brief Sets the line colour.
		void													set_dot_colour(int red, int green, int blue);

		/// \brief Returns access to the line colour array.
		int*													get_dot_colour()				{ return dot_colour; }

		/// \brief Set Dot fill mode.
		void													set_dot_fill(bool new_fill);

		/// \brief Get dot fill mode.
		bool													get_dot_fill()					{ return fill_dot; }

		/// \brief Sets the line colour.
		void													set_line_colour(int red, int green, int blue);

		/// \brief Returns access to the line colour array.
		int*													get_line_colour()				{ return line_colour; }

		/// \brief Set the line thickness.
		void													set_line_thickness(int new_thickness);

		/// \brief Get the line thickness.
		int														get_line_thickness()			{ return line_thickness; }

		/// \brief Sets the line colour.
		void													set_background_colour(int red, int green, int blue);

		/// \brief Returns access to the line colour array.
		int*													get_background_colour()			{ return background_colour; }
		//-------------------------------------------------------------------------------//

}DISP,*PDISP;

#endif // DISPLAY_H
