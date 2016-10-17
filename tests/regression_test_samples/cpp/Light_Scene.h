/// \file Light_Scene.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef LIGHT_SCENE_H
#define LIGHT_SCENE_H

#include <d3d9.h>
#include <d3dx9.h>

#include "DX_Manager.h"

#include <fstream>
#include <string>

#include <map>

using namespace std;

/// \brief Class controls the lighting of a scene

typedef class Light_Scene
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interaces
		/// \brief Graphics interface.
		PGRAPHICS									graphics;
		//*****************************************************//


		//*****************************************************//
		//-------------------------------------------------------------------------------//the lights
		/// \brief Vector
		map<string, D3DLIGHT9>				lights;

		/// \brief Ambient light
		D3DXVECTOR3							ambient;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Initialisation state.
		bool													initialised;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//priavte functions
		/// \brief Loads a directional light from a file.
		bool													load_directional(fstream &file);

		/// \brief Loads a point light from a file.
		bool													load_point(fstream &file);

		/// \brief Loads a spotlight from a file.
		bool													load_spot(fstream &file);
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Light_Scene();

		/// \brief Class destructor.
																~Light_Scene();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief Initialises the scene, turning all lights on.
		void													init();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//light creation
		/// \brief Gets light.
		D3DLIGHT9									get_light(string name);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Light management
		/// \brief turn light on.
		bool													switch_on(string name);

		/// \brief turn light off.
		bool													switch_off(string name);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//ambient light
		/// \brief Set new ambient values.
		void													set_ambient(D3DXVECTOR3 new_amb);

		/// \brief Updates ambient lighting.
		inline void										update_ambient()
																{
																	graphics->get_d3d_device()->SetRenderState(D3DRS_AMBIENT, D3DCOLOR_XRGB((int)ambient.x, (int)ambient.y, (int)ambient.z));
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Loads a scene from a file (string)
		bool													load(string filename);

		/// \brief Loads a scene from a file (fstream)
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}LSCENE,*PLSCENE;

#endif // LIGHT_SCENE_H
