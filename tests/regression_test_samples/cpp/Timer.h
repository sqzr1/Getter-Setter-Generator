/// \file Timer.h
/// \author Jared Chidgey
/// \author Student No. 113456826

#ifndef TIMER_H
#define TIMER_H

#include <windows.h>

/// \brief Timer class.
/// Dynammic timer class
/// Can base its self on performance frequency values (if available)
/// or failing that falls back to timeGetTime()

typedef class Timer
{
																									//
																									//private declarations
	//////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Timer*									_instance;

		/// \brief Private constructor.
																Timer();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//timer variables
		/// \brief Current time.
		LONGLONG									cur_time;

		/// \brief Last time.
		LONGLONG									last_time;

		/// \brief Used to time each frame.
		DWORD											time_count;

		/// \brief Performance timer's frequency.
		LONGLONG									perf_cnt;

		/// \brief Indicates which timing method is used.
		BOOL												perf_flag;

		/// \brief Time at which the timer next "ticks".
		LONGLONG									next_time;

		/// \brief
		BOOL												move_flag;

		/// \brief Controls the frames per second.
		int													frames_sec;

		/// \brief Tracks the time passed at the last call.
		double												time_passed;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Initialisation state.
		bool													initialised;
		//-------------------------------------------------------------------------------//

																									//
																									//public declarations
	//////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static												Timer* Instance()
																{
																	if ( _instance == 0 )
																	{
																		_instance = new Timer;
																	}

																	return _instance;
																}

		/// \brief Destructor.
																~Timer();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//functions
		/// \brief Initialises the timer.
		void													init();

		/// \brief Sets the frames per second
		bool													set_frames(int new_frames_sec);

		/// \brief Poll timer for tick.
		bool													poll_timer();

		/// \brief Returns the time recorded at the last poll.
		inline double									get_time_passed()
																{
																	return time_passed;
																}
		//-------------------------------------------------------------------------------//

} TIMER, *PTIMER;

#endif
