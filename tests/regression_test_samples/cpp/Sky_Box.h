/// \file Sky_Box.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef SKY_BOX_H
#define SKY_BOX_H

#include <d3d9.h>
#include <d3dx9.h>

#include <fstream>
#include <string>

#include "DX_Manager.h"

#include "Custom_Vertex.h"

using namespace std;

/// \brief Class represents a sky box.

/// This class holds data, and renders the backdrop image
///also known as a skybox.

typedef class Sky_Box
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphical interface.
		PGRAPHICS										graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//textures
		/// \brief Front texture.
		LPDIRECT3DTEXTURE9					front;

		/// \brief Back texture.
		LPDIRECT3DTEXTURE9					back;

		/// \brief Left texture.
		LPDIRECT3DTEXTURE9					left;

		/// \brief Right texture.
		LPDIRECT3DTEXTURE9					right;

		/// \brief Top texture.
		LPDIRECT3DTEXTURE9					top;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//data
		/// \brief The actual box.
		CUSTOMVERTEX*							sky_box;

		/// \brief The VertexBuffer.
		LPDIRECT3DVERTEXBUFFER9		vb;

		/// \brief Void pointer for vertices.
		void*													void_vb;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Initialisation state.
		bool														initialised;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																	Sky_Box();

		/// \brief Class destructor.
																	~Sky_Box();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//use
		/// \brief Initialises the sky box.
		void														init();

		/// \brief Renders the sky box.
		void														render();

		/// \brief Loads the sky box from a file(string).
		bool														load(string filename);

		/// \brief Loads a sky box from a file(fstream).
		bool														load(fstream &file);
		//-------------------------------------------------------------------------------//
}SKY_BOX,*PSKY_BOX;

#endif // SKY_BOX_H

