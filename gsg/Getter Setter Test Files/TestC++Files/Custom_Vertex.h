/// \file Custom_Vertex.h
/// \author Jared Chidgey

#ifndef CUSTOM_VERTEX_H
#define CUSTOM_VERTEX_H

#include <d3d9.h>
#include <d3dx9.h>

#define CUSTOM_FVF (D3DFVF_XYZ |  D3DFVF_NORMAL  | D3DFVF_TEX1)

/// \brief Custom vertex structure.
/// Used within the DX application for representing
/// points within 3d spaces.

typedef struct CUSTOMVERTEX
{
		/// \brief Strucxt constructor
		CUSTOMVERTEX() {}

		/// \brief Struct nonstandard constructor.
		CUSTOMVERTEX(float new_x, float new_y, float new_z, float new_n_x, float new_n_y, float new_n_z, float new_u, float new_v)
		{
			x = new_x;
			y = new_y;
			z = new_z;

			NORMAL.x = new_n_x;
			NORMAL.y = new_n_y;
			NORMAL.z = new_n_z;

			u = new_u;
			v = new_v;
		}

		/// \brief Represents the position of the vertex.
		FLOAT											x,
																y,
																z;

		/// \brief Repesents the normal of the vector (lighting.
		D3DXVECTOR3							NORMAL;

		/// \brief Represents texture coordinates.
		FLOAT											u,
																v;
}C_VERTEX;

#endif
