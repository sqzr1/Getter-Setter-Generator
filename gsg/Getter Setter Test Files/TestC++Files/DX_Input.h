/// \file DX_Input.h
/// \author Jared Chidgey

#ifndef DX_INPUT_H
#define DX_INPUT_H

#include <windows.h>
#include <d3d9.h>
#include <d3dx9.h>
#include <dinput.h>

#include <string>
#include <stdio.h>

#include "DX_Graphics.h"

using namespace std;

/// \brief Singleton class managing DInput.
/// This singleton class sets up and provides management
/// for input devices and the associated data acquired from
/// DX and Dinput.

typedef class DX_Input
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		friend class DX_Manager;
		/// \brief singleton class instance pointer
		static DX_Input*								_instance;

		/// \brief Private class constructor
																DX_Input();

		/// \brief Private class destructor.
																~DX_Input();

		//Dx control structures
		//-------------------------------------------------------------------------------//
		/// \brief DirectInput object.
		LPDIRECTINPUT8							d_input;

		/// \brief Input device representing the keyboard.
		LPDIRECTINPUTDEVICE8			d_in_keyb;

		/// \brief Input device representing the mouse.
		LPDIRECTINPUTDEVICE8			d_in_mouse;

		/// \brief Pointer to the DXManager instance.
		PGRAPHICS									graphics;
		//-------------------------------------------------------------------------------//


		//Device state structures
		//-------------------------------------------------------------------------------//
		/// \breif Represents keystates of the keyboard.
		char													app_keyb[256];

		/// \brief Rperesents the current state of the mouse.
		DIMOUSESTATE							app_mouse;
		//-------------------------------------------------------------------------------//

		//mouse variable data
		//-------------------------------------------------------------------------------//
		/// \brief Sensitivity of the mouse.
		float												mouse_sensitivity;

		/// \brief Tracks the location of the mouse.
		D3DXVECTOR3							mouse_location;

		/// \brief Point of the mouse for focus.
		D3DXVECTOR3							mouse_hotspot;

		/// \brief Screen width.
		float												screen_w;

		/// \brief Screen height.
		float												screen_h;

		/// \brief Image used as the mouse cursor.
		LPDIRECT3DTEXTURE9				mouse_cursor;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Resource state of the object.
		bool													clean;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static DX_Input*								Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new DX_Input;
																	}

																	return _instance;
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//init/shutdown
		/// \brief DI initator.
		bool 												init(HINSTANCE hinstance, HWND hwnd);

		/// \brief Keyboard initialiser.
		void													init_keyboard();

		/// \brief Mouse initialiser.
		void													init_mouse();

		/// \brief Clean up function.
		void													clean_DInput();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief update input.
		bool													update();

		/// \brief Draws the mouse cursor to the screen.
		void													draw_mouse();

		/// \brief Write the current mouse coordinates to the screen.
		void													mouse_coords();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//set mouse data
		/// \brief Assigns mouse attribute.s
		bool													set_mouse_cursor(string filename);

		/// \brief Sets the cursor hot spot
		void													set_mouse_hot(float h_x, float h_y);

		/// \brief Sets the cursor position.
		void													set_cursor_pos(float new_x, float new_y);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//get mouse data
		/// \brief Returns mouse data, change of x-axis.
		float												relative_x();

		/// \brief Returns mouse data, change of y-axis.
		float												relative_y();

		/// \brief Returns mouse data, change of z-axis (wheel).
		float												relative_z();

		/// \brief Relays mouse data, current x-pos.
		float												absolute_x();

		/// \brief Relays mouse data, current y-pos.
		float												absolute_y();

		/// \brief Relays mouse data, button state.
		bool													mouse_button(int button);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//keyboard
		/// \brief Relays keyboard data.
		bool													key_pressed(int key);

		/// \brief Tests to see if any key has been pressed.
		bool													any_key();

		/// \brief Clears the keyboard buffer.
		void													clear_keys();
		//-------------------------------------------------------------------------------//

}DINPUT,*PDINPUT;

#endif // DX_INPUT_H
