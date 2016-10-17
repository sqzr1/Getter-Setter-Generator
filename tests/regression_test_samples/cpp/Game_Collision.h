/// \file GamE_Collision.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_COLLISION_H
#define GAME_COLLISION_H

#include <d3d9.h>
#include <d3dx9.h>

#include <fstream>
#include <string>

const int BOUND_BOX = 0;
const int BOUND_CYLINDER = 1;
const int BOUND_SPHERE = 2;

using namespace std;

/// \brief Class handles collisions.

/// This class handles collisions, and represents the
/// bounding volumes of entities within the game, there are three
/// types of bounding volumes avaliable
/// Simple box, sphere, and cylinder.

typedef class Game_Collision
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief Bounding type.
		int													type;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//bounding data
		/// \brief Width of the bounding box.
		float												width;

		/// \brief Height of the bounding box, or cylinder.
		float												height;

		/// \brief Depth of the bounding box.
		float												depth;

		/// \brief Radius of the sphere and cylinder,
		float												radius;


		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//private collision functions
		bool													collision_box_box(Game_Collision lhs, D3DXVECTOR3 pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);

		bool													collision_box_cylinder(Game_Collision box, D3DXVECTOR3 box_pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);

		bool													collision_box_sphere(Game_Collision lhs, D3DXVECTOR3 pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);

		bool													collision_cylinder_cylinder(Game_Collision lhs, D3DXVECTOR3 pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);

		bool													collision_cylinder_sphere(Game_Collision lhs, D3DXVECTOR3 pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);

		bool													collision_sphere_sphere(Game_Collision lhs, D3DXVECTOR3 pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Collision();

		/// \brief Class destructor.
																~Game_Collision();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief Tests collision.
		bool													collide(D3DXVECTOR3 pos, Game_Collision rhs, D3DXVECTOR3 rhs_pos);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load bounding data from a file (string)
		bool													load(string filename);

		/// \brief Load bounding data from a file (fstream)
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//


}COLLISION,*PCOLLISION;

#endif // GAME_COLLISION_H

