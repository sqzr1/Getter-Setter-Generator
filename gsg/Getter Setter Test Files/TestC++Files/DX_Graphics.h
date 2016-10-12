/// \file DX_Graphics.h
/// \author Jared Chidgey

#ifndef DX_GRAPHICS_H
#define DX_GRAPHICS_H

#include <windows.h>
#include <d3d9.h>
#include <d3dx9.h>

#include "Custom_Vertex.h"

/// \brief Singleton DirectX basics management class.
/// This class manages the basic set up of directX
/// and its graphical based devices.

typedef class DX_Graphics
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Allows the dxmanager class to destroy this instance;
		friend class DX_Manager;

		/// \brief singleton instance.
		static DX_Graphics*										_instance;

		/// \brief private singleton Constructor.
																DX_Graphics();

		/// \brief Destructor
																~DX_Graphics();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//device interfaces
		/// \brief pointer representing the insatance of direct3d.
		LPDIRECT3D9												d3d;

		/// \brief pointer representing the display device.
		LPDIRECT3DDEVICE9										d3d_dev;

		/// \brief struct reperesenting the display appaearance.
		D3DPRESENT_PARAMETERS									d3d_pp;

		/// \brief Pointer to directX sprite contorl device.
		LPD3DXSPRITE											d3d_sprt;

		/// \brief Current font.
		LPD3DXFONT												font;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//display data
		/// \brief Handle to the window.
		HWND													hwnd;

		/// \brief Handle to the application instance.
		HINSTANCE												hinstance;

		/// \brief Screen width.
		float 													screen_w;

		/// \brief Screen hwight.
		float													screen_h;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Flag indicating resource state.
		bool 													clean;

		/// \brief Indicates whether the class is in debug mode.
		bool													debug;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief singleton initialiser
		static DX_Graphics*										Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new DX_Graphics;
																	}

																	return _instance;
																}

		/// \brief init function
		bool 													init(HINSTANCE new_hinstance, HWND new_hwnd, int width, int height, bool windowed);

		/// \brief cleanup
		void													shutdown();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//rendering
		/// \brief Sets up a bew scene.
		void													begin_render();

		/// \brief Begin sprite rendering.
		void													begin_sprite();

		/// \brief End sprite Rendering.
		void													end_sprite();

		/// \brief Ends the rendering of a scene.
		void													end_render();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//get data
		/// \brief Returns current screen width.
		float													get_screen_w();

		/// \brief Returns current screen height.
		float													get_screen_h();

		/// \brief Returns a handle to the window.
		HWND													get_hwnd();

		/// \brief Returns a handle to the applicaion instance.
		HINSTANCE												get_hinstance();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//access devices
		/// \brief provides access to the d3d device.
		LPDIRECT3DDEVICE9										get_d3d_device();

		/// \brief provides accesto d3d sprite device.
		LPD3DXSPRITE											get_d3d_sprite();

		/// \brief Provides access to the font device.
		LPD3DXFONT												get_d3d_font();
		//-------------------------------------------------------------------------------//

}GRAPHICS,*PGRAPHICS;

#endif // DX_GRAPHICS_H
