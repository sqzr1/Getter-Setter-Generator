#ifndef DOT_H
#define DOT_H

#include <fstream>
#include <iostream>

using namespace std;

typedef class _dot
{
	private:
		int x, y;

		//private functions
		bool write(fstream &file);
		bool read(fstream &file);

	public:
		//constructor
		_dot();
		_dot(int new_x, int new_y);

		//copy constructor
		_dot(_dot &rhs);

		//destructor
		~_dot();

		//setters
		bool set_x(int new_x);
		bool set_y(int new_y);
		bool set_xy(int new_x, int new_y);

		//getters
		int get_x();
		int get_y();

		//fileio
		bool save(fstream &file);
		bool load(fstream &file);

}DOT,*PDOT;

#endif // FOT_H
