/// \file Game.h
/// \author Jared Chidgey
/// \date 2007
/// \brief

#ifndef GAME_H
#define GAME_H

#include "Game_Board.h"
#include "Player.h"

#include "Display.h"
#include "AI.h"

#include "Config.h"

/// \brief Class represents the state of the game.

typedef class Game
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instace.
		static Game*											_instance;

		/// \brief Private class constructor.
																Game();

		/// \brief Private class destructor.
																~Game();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Game data
		/// \brief Display data.
		PDISP													display;

		/// \brief The game board.
		PBOARD													board;

		/// \brief Game configuration file.
		PCONFIG													config;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//game control
		/// \brief Indicates that the game has started.
		bool													game_has_started;

		/// \brief Indicates that the gane is over.
		bool													game_has_ended;

		/// \brief Game paused.
		bool													game_is_paused;

		/// \brief AI control brain.
		PAI														ai_control;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Players
		/// \brief Number of players.
		int														num_players;

		/// \brief Players.
		PLAYER*													players[4];

		/// \brief Number of active players.
		int														active_num;

		/// \brief Active players.
		PLAYER*													active;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Game timing
		/// \brief Seconds per move.
		int														timed_seconds;

		/// \brief Minuts per move.
		int 													timed_minutes;

		/// \brief Current elapsed seconds.
		int														current_seconds;

		/// \brief Current elapsed minutes.
		int														current_minutes;

		/// \brief Indicates whether the current game is a timed one.
		bool													timed_game;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Singleton
		/// \brief Singleton instancer.
		static Game*											Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Game();
																	}

																	return _instance;
																}

		/// \brief Singleton destroyer.
		static void												Release()
																{
																	if(_instance)
																	{
																		delete _instance;
																		_instance = 0;
																	}
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//core founctionality
		/// \brief Initialises the game.
		void													init();

		/// \brief Writes settings to the configuration file.
		void													save_settings();

		/// \brief Draws the game board.
		void													draw_board(HDC hdc);

		/// \brief Sets up the game.
		void													set_up_game();

		/// \brief Reset the game.
		bool													reset_game(int new_w, int new_h);

		/// \brief Ends the 
		bool													end_active_turn();

		/// \brief Run active player AI.
		int														run_active_ai();

		/// \brief Indicates whether the current game has begun.
		bool													game_started()					{ return game_has_started; }

		/// \brief Causes the game to start.
		void													start_game();

		/// \brief Stops/Pauses the game.
		void													stop_game();

		/// \brief Checks the game pause state.
		bool													game_paused()					{ return game_is_paused; }

		/// \brief Indicates whether the game has ended.
		bool													game_ended()					{ return game_has_ended; }

		/// \brief Causes the game to end.
		bool													end_game();

		/// \brief Test the board.
		void													test_board();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//setters
		/// \brief Return the current display settings.
		PDISP													get_display()					{ return display; }

		/// \brief Return current game board.
		PBOARD													get_board()						{ return board; }

		/// \brief Return current AI brain object.
		PAI														get_ai_brain()					{ return ai_control; }

		/// \brief Resize window appropriately.
		void													resize_window(HWND hwnd);
		//-------------------------------------------------------------------------------//
		

		//*****************************************************//
		//-------------------------------------------------------------------------------//Time settings
		/// \brief Make the games timed.
		void													make_timed_game()				{ timed_game = true; }

		/// \brief Make the game untimed.
		void													remove_timed_game()				{ timed_game = false; }

		/// \brief Is the game timed.
		bool													is_timed()						{ return timed_game; }

		/// \brief Set the time per turn for timed games.
		void													set_timer(int new_minutes, int new_seconds);

		/// \brief Returns current seconds.
		int														get_current_seconds()			{ return current_seconds; }

		/// \brief returns current minutes.
		int														get_current_minutes()			{ return current_minutes; }
				
		/// \brief Ticks the games time over.
		void													tick_timer();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Players
		/// \brief Get the total number of players.
		int														get_num_players()				{ return num_players; }

		/// \brief Remove a player.
		bool													remove_player_num(int num);

		/// \brief Remove a player.
		bool													remove_player(int index);

		/// \brief Add player to the game.
		bool													add_player(PLAYER* plr);

		/// \brief Get player.
		PLAYER*													get_player(int index);

		/// \brief Get the current active player.
		PLAYER*													get_active()					{ return active; }

		/// \brief Reset player display settings.
		void													reset_player_display();

		/// \brief Ends the current players turn.
		void													end_turn();

		/// \brief End of game place list.
		string													construct_list();
		//-------------------------------------------------------------------------------//

		void													set_placings();
		
}GAME,*PGAME;

#endif // GAME_H
