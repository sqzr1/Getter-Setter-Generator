/// \file Camera.h
/// \author Jared Chidgey

#ifndef CAMERA_H
#define CAMERA_H

#include <d3d9.h>
#include <d3dx9.h>

#include "DX_Manager.h"

#include <sstream>

/// \brief X-axis vector constant.
const D3DXVECTOR3 X_AXIS = D3DXVECTOR3(1.0f, 0.0f, 0.0f);

/// \brief Y-axis vector constant.
const D3DXVECTOR3 Y_AXIS = D3DXVECTOR3(0.0f, 1.0f, 0.0f);

/// \brief Z-axis vector constant.
const D3DXVECTOR3 Z_AXIS = D3DXVECTOR3(0.0f, 0.0f, 1.0f);

/// \brief The camera class controls a camera.

/// This class encapsulates the matricies, vectors and other  values
/// which are necessary for representing the
/// current view point of the 3d world. Calling update will set
/// the camera as the active view.

typedef class Camera
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Pointer to the DX manager.
		PGRAPHICS												graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//position
		/// \brief Matrix representing the current view.
		D3DXMATRIX												view;

		/// \brief Vector representing the camera's position.
		D3DXVECTOR3												eye_pos;

		/// \brief Vector representing direction of the camera.
		D3DXVECTOR3												look_at;

		/// \brief Vector representing orientation of the camera.
		D3DXVECTOR3												up;

		/// \brief Vector representing the direction of RIGHT
		D3DXVECTOR3												right;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//base values
		/// \brief Vector representing direction of the camera.
		D3DXVECTOR3												look_base;

		/// \brief Vector representing orientation of the camera.
		D3DXVECTOR3												up_base;

		/// \brief Vector representing the direction of RIGHT
		D3DXVECTOR3												right_base;

		/// \brief Rotaion yaw.
		float													y_rotation;

		/// \brief Rotaion pitch.
		float													x_rotation;

		/// \brief Rotaion roll.
		float													z_rotation;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//projection
		/// \brief Matrix representing the current projection.
		D3DXMATRIX												proj;

		/// \brief Represents camera angle.
		FLOAT													angle;

		/// \brief Represents nearest visible plane.
		FLOAT													nearest;

		/// \brief Represents furthest visible plane.
		FLOAT													furthest;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Indicates whether the camera is locked or not.
		bool													locked;
				
		/// \brief Flag for orientation update.
		bool													update_orientation;

		/// \brief Updates orientation of camera.
		void													orientate();
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class Constructor.
																Camera();

		/// \brief Class Destructor.
																~Camera();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//position
		/// \brief Strafe the camera.
		void													strafe(float num);

		/// \brief Walk.
		void													walk(float num);

		/// \brief Get the current position of the camera
		D3DXVECTOR3												get_position();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//getters
		/// \brief Get look.
		D3DXVECTOR3												get_look();

		/// \brief Get right.
		D3DXVECTOR3												get_right();

		/// \brief Get up.
		D3DXVECTOR3												get_up();

		/// \brief Get the view matrix.
		D3DXMATRIX												get_view();

		/// \brief Get the projection matrix.
		D3DXMATRIX												get_proj();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//direction
		/// \brief Look up or down.
		void													pitch(float new_angle);

		/// \brief Look arround.
		void													yaw(float new_angle);

		/// \brief Roll.
		void													roll(float new_angle);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//projection
		/// \brief sets the projection(lens) angle (deg).
		void													set_proj_angle_deg(FLOAT new_angle);

		/// \brief sets the projection(lens) angle (rad).
		void													set_proj_angle_rad(FLOAT new_rad);

		/// \brief sets the furthest distance at which objects will appear.
		bool													set_far(FLOAT new_far);

		/// \brief sets the nearest distance at which objedcts will appear.
		bool													set_near(FLOAT new_near);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//hooking functions
		/// \brief Locks the camera to be given data.
		inline void												lock()
																{
																	locked = true;
																}

		/// \brief Unlocks/frees the camera.
		inline void												unlock()
																{
																	locked = false;
																}

		/// \brief Sets the camera's position.
		void													set_position(D3DXVECTOR3 new_pos);

		/// \brief Sets the new view of the camera.
		void													set_view(D3DXVECTOR3 new_look, D3DXVECTOR3 new_up, D3DXVECTOR3 new_right);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//render
		/// \brief Update camera.
		void													update();
		//-------------------------------------------------------------------------------//

		void													debug();

}CAMERA,*PCAMERA;

#endif
