/// \file Stat.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef STAT_H
#define STAT_H

/// \brief Simple strut represents a character stat

typedef struct Stat
{
	/// \brief Struct constructor.
	Stat()
	{
		min_value = 0;
		max_value = 0;
		cur_value = 0;
	}

	/// \brief Struct non-standard constructor.
	Stat(int new_cur, int new_min, int new_max)
	{
		cur_value = new_cur;
		min_value = new_min;
		max_value = new_max;
	}

	/// \brief Minimum value of the stat
	int														min_value;

	/// \brief Maximum value of the stat
	int														max_value;

	/// \brief Current value of the stat.
	int														cur_value;
}STAT,*PSTAT;

#endif // STAT_H

