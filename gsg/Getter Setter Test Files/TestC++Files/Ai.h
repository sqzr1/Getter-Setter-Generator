/// \file AI.h
/// \author Jared Chidgey
/// \date
/// \brief

#ifndef AI_H
#define AI_H

#include <cstdlib>
#include <time.h>
#include <queue>

#include "Box.h"
#include "Player.h"
#include "Game_Board.h"

// Random selection
const int AI_DUMB = 1;

// Attempts to play along walls
const int AI_DEFENSIVE = 2;

// following the last played move
const int AI_AGGRESSIVE = 3;

// ultimate player
const int AI_ULTIMATE = 4;

/// \brief Class runs AI algorithm for computer player turns.

typedef class AI_Brain
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//Player descriptors
		/// \brief AI algorithm.
		int														mode;

		/// \brief Is still the AI's turn.
		bool													turn;

		/// \brief Algorithm 1 wait delay.
		int														wait_1;

		/// \brief Algorithm 2 wait delay.
		int														wait_2;

		/// \brief Algorithm 3 wait delay.
		int														wait_3;

		/// \brief Algorithm 4 wait delay.
		int														wait_4;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
	
		//*****************************************************//
		//-------------------------------------------------------------------------------//constructor
		/// \brief Class constructor.
																AI_Brain();

		/// \brief Class destructor.
																~AI_Brain();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//controlling
		/// \brief Ai algortihm 1, random selection.
		int														algorithm_1(PBOARD, PLAYER*);

		/// \brief Ai Algorithm 2, defensive.
		int														algorithm_2(PBOARD, PLAYER*);

		/// \brief Ai Algorithm 3, aggesdssive.
		int														algorithm_3(PBOARD, PLAYER*);
	
		/// \brief Ai Algorithm 4, some planning.
		int														algorithm_4(PBOARD, PLAYER*);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//act delay
		/// \brief Set AI 1 act delay.
		void													set_act_delay_1(int new_delay);

		/// \brief Get AI 1 act delay.
		int														get_act_delay_1()				{ return wait_1; }

		/// \brief Set AI 2 act delay.
		void													set_act_delay_2(int new_delay);

		/// \brief Get AI 2 act delay.
		int														get_act_delay_2()				{ return wait_2; }

		/// \brief Set AI 3 act delay.
		void													set_act_delay_3(int new_delay);

		/// \brief Get AI 3 act delay.
		int														get_act_delay_3()				{ return wait_3; }

		/// \brief Set AI 4 act delay.
		void													set_act_delay_4(int new_delay);
		
		/// \brief Get AI 4 act delay.
		int														get_act_delay_4()				{ return wait_4; }

		/// \brief Get AI act delay.
		int														get_act_delay(int algorithm);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Data
		/// \brief Set AI mode.
		void													set_mode(int);

		/// \brief Get aI mode.
		int														get_mode()						{ return mode; }
		//-------------------------------------------------------------------------------//

}AI,*PAI;

#endif // AI_H
