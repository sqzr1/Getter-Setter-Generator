/// \file Simple_Animation.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef SIMPLE_ANIMATION_H
#define SIMPLE_ANIMATION_H

#include "DX_Manager.h"

#include <d3d9.h>
#include <d3dx9.h>

#include <fstream>
#include <string>

using namespace std;

/// \brief Class represents an animated object.

///This class represents an animated mesh, loads data from a
/// animation definition file, and loads the mesh file, renders
/// and updates frame positions.

typedef class Simple_Animation
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		PGRAPHICS									graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//image
		/// \brief Frames.
		LPD3DXMESH								frames;

		/// \brief Materials
		D3DMATERIAL9*							materials;

		/// \brief  Textures.
		LPDIRECT3DTEXTURE9*			textures;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//animation control
		/// \brief Current frame
		int													current_frame;

		/// \brief Time accumulated
		double												accumulated;

		/// \brief Model filename.
		string												model_file;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//animation data
		/// \brief Number of object sections/subsets.
		int													sections;

		/// \brief Number of total subsets.
		DWORD											sub_sets;

		/// \brief Number of frames for animation.
		int													num_frames;

		/// \brief Sequential frame order flag.
		bool													in_order;


		/// \brief Frame oreder (if object is out of oreder)
		int*													order;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//animating data
		/// \brief Time between frames.
		double												time_gap;

		/// \brief Flag indicating animation state.
		bool													finished;

		/// \brief Speed modifier for the animation.
		float												speed;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Simple_Animation();

		/// \brief Class destructor.
																~Simple_Animation();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Update the animation.
		void													update(double time_ellapsed);

		/// \brief Render the current frame.
		void													render();

		/// \brief Initialises animation state.
		void													begin();

		/// \brief Tests whether the animation has finished.
		inline bool										has_finished()
																{
																	return finished;
																}

		/// \brief Returns the current frame of animation.
		inline int											cur_frame()
																{
																	return current_frame;
																}

		/// \brief Returns the current speed modifier of the animation.
		inline float										get_speed()
																{
																	return speed;
																}

		/// \brief Sets the speed modifier.
		bool													set_speed(float new_speed);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load the animation definition file and create the animation(string).
		bool													load(string filename);

		/// \brief Load the animation definition file and create the animation(fstream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}SIMP_ANIM,*PSIMP_ANIM;

#endif // SIMPLE_ANIMATION_H

