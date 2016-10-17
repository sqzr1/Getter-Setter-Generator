/// \file Player.h
/// \author Jared Chidgey
/// \date
/// \brief

#ifndef PLAYER_H
#define PLAYER_H

#include <string>
#include <fstream>

#include <windows.h>

#include "Dot.h"
#include "Line.h"
#include "Box.h"

/// \brief Class represents a player

/// The class represents a player, holding data on the current game, as well
/// As historical data, and defining behaviour for AI players

typedef class Player
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//Player descriptors
		/// \brief Player name.
		std::string												name;

		/// \brief Player Id number.
        int														id;

		/// \brief Save state.
        bool													saved;

		/// \brief Previous save file name.
        std::string												prev_filename;

		/// \brief Player colour.
		int														colour[3];

		/// \brief Players pen.
		HPEN													pen;

		/// \brief Players brush.
		HBRUSH													brush;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Player game data
		/// \brief Player score.
        int														score;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Player record
		/// \brief Number of games played.
        int														games;

		/// \brief Number of games won.
        int														wins;

		/// \brief Number of games drawn.
        int														draws;

		/// \brief Number of games lost.
        int														losses;
		//-------------------------------------------------------------------------------//

        
		//*****************************************************//
		//-------------------------------------------------------------------------------//AI player info
		/// \brief Player is AI.
        bool													ai;

		/// \brief AI algorithm to use.
        int														algorithm;
		//-------------------------------------------------------------------------------//


        //*****************************************************//
		//-------------------------------------------------------------------------------//Private functoions
		/// \brief Write player to file.
        bool													write(std::fstream &file);

		/// \brief Read player from file.
        bool													read(std::fstream &file);
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
        /// \brief Class constructor
																Player();

        /// \brief Class destructor.
																~Player();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Ai function
		/// \brief Will run the appropriate AI function.
		void													run_ai();
		//-------------------------------------------------------------------------------//


        //*****************************************************//
		//-------------------------------------------------------------------------------//Setters
		/// \brief Increase the players wins and games.
		void													won();

		/// \brief Increase the players draws and games.
		void													drew();

		/// \brief Increase the players losses and games.
		void													lost();

		/// \brief Player has captured a box, increase they're score.
		void													has_captured(int num_boxes);

		/// \brief Reset scroe to zero.
		int														reset_score();
        
		/// \brief Set the players name.
		bool													set_name(std::string new_name);

		/// \brief Set the players Id number.
		bool													set_id(int new_id);

		/// \brief Set the players colour.
		bool													set_colour(int red, int blue, int green);

		/// \brief Set the players colour (array method).
		bool													set_colour(int* col, int col_size);

		/// \brief Set as AI and algorithm.
		void													set_ai_algorithm(int new_a);

		/// \brief Set as human player.
		void													set_human_algorithm();
		//-------------------------------------------------------------------------------//

		
		//*****************************************************//
		//-------------------------------------------------------------------------------//Getters
		/// \brief Get the number of games a player has played.
		int														num_games()						{ return games; }

		/// \brief Get the number of games the player has won.
		int														num_wins()						{ return wins; }

		/// \brief Get the number of games the player has drawm.
		int														num_draws()						{ return draws; }

		/// \brief Get the number of games the player has lost.
		int														num_losses()					{ return losses; }

		/// \brief Get the players Id number.
		int														get_id()						{ return id; }

		/// \brief String version of games.
        std::string												get_games();

		/// \brief String version of wins.
        std::string												get_wins();

		/// \brief String version of draws.
        std::string												get_draws();

		/// \brief String version of losses.
        std::string												get_losses();

		/// \brief Get player colour (as array of ints)
		int*													get_colour()					{ return colour; }

		/// \brief Get the players name.
		std::string												get_name()						{ return name; }

		/// \brief Get the players current score.
		int														get_score()						{ return score; }

		/// \brief test if the player has been previously saved.
		bool													previously_saved()				{ return saved; }

		/// \brief Tests whether the player is AI.
		bool													is_ai()							{ return ai; }

		/// \brief Get ai algorithm.
		int														get_ai_algorithm()				{ return algorithm; }
		//-------------------------------------------------------------------------------//


        //*****************************************************//
		//-------------------------------------------------------------------------------//File io
		/// \brief Save the character
		bool													save();

		/// \brief Save the character.
		bool													save_prev();


        bool													save(std::fstream &file);
        bool													save(std::string filename);
        bool													load(std::fstream &file);
        bool													load(std::string filename);
		//-------------------------------------------------------------------------------//

}PLAYER,*PPLAYER;

#endif // PLAYER_H
