/// \file Game_Terrain.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_TERRAIN_H
#define GAME_TERRAIN_H

#include "DX_Manager.h"

#include "Custom_Vertex.h"

#include <string>
#include <fstream>

using namespace std;

/// \brief Class represents the terrain on the ground.

/// This class loads size and height values from a file to create uniformly
/// spaced terrain. The terrain is calculated in indexed vertices

typedef class Game_Terrain
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief graphics interface.
		PGRAPHICS												graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Vertex buffer
		/// \brief The vertex buffer.
		LPDIRECT3DVERTEXBUFFER9									vb;

		/// \brief Verticies void pointer.
		VOID*													vert_void;

		/// \brief vertex object array.
		CUSTOMVERTEX*											vertices;

		/// \brief Number of vertices.
		int														num_vertices;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Index buffer
		/// \brief The inbdex Buffer.
		LPDIRECT3DINDEXBUFFER9									ib;

		/// \brief Indicies void pointer.
		VOID*													ind_void;

		/// \brief Indicies.
		WORD*													indices;

		/// \brief Number of indicies.
		int														num_indices;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//lighting
		/// \brief Lighting
		D3DLIGHT9 												light;

		/// \brief light 2
		D3DLIGHT9												light2;

		/// \brief material
		D3DMATERIAL9											material;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//textures
		/// \brief Texture.
		LPDIRECT3DTEXTURE9										texture;

		/// \brief Number of textures int the set.
		int														num_tiles;

		/// \brief  Starting coord of a texture tile
		float*													start_coord;

		/// \brief Ending coord of a texture tile.
		float*													end_coord;

		/// \brief Textur map.
		int**													tex_index;

		/// \brief Width of texture data array.
		int														tc_width;

		/// \brief Height of texture array.
		int														tc_height;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//height data array
		/// \brief height map array.
		int**													data;

		/// \brief Width of array.
		int														width;

		/// \brief Height of array.
		int														height;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//cell data
		/// \brief Width of a cell.
		float													cell_width;

		/// \brief Height of a cell.
		float													cell_height;

		/// \brief Number of cells wide.
		int														num_cells_wide;

		/// \brief Number of cells high.
		int														num_cells_high;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//class data
		/// \brief Init state.
		bool													initialised;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//terrain functions
		/// \brief Fill the vertex buffer for indexed drawing.
		void													fill_indexed_vertices();

		/// \brief Calculates lighting normals.
		void													calculate_normals();

		/// \brief Fills the index buffer.
		void													fill_indices();
		//-------------------------------------------------------------------------------//


																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Terrain();

		/// \brief Class destructor.
																~Game_Terrain();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Draws the terrain.
		void													render();

		/// initialise
		void													init();

		/// \brief Gets the height at a particular point
		float													get_height(float x, float z);

		/// \brief Returns cell spacing of the z axis
		float													get_bredth_spacing();

		/// \brief Returns cell spacing of the x axis.
		float													get_width_spacing();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load terrain data from a file (string).
		bool													load(string filename);

		/// \brief Loads terrain data from a file (fstream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}TERRAIN,*PTERRAIN;

#endif // GAME_TERRAIN_H

