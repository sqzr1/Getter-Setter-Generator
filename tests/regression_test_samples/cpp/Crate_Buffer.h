/// \file Crate_Buffer.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef CRATE_BUFFER_H
#define CRATE_BUFFER_H

#include "DX_Manager.h"

#include <d3d9.h>
#include <d3dx9.h>

#include "Custom_Vertex.h"

/// \brief Class represents the 3d representation of a crate.

/// This class encapsulates the data for the 3d representation
/// of a crate, as singleton.


typedef class Crate_Buffer
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Allows the dxmanager class to destroy this instance;
		friend class										DX_Manager;

		/// \brief Singleton instance
		static Crate_Buffer*						_instance;

		/// \brief Private class constructor.
																Crate_Buffer();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interface
		/// \brief Graphics interface.
		PGRAPHICS									graphics;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//
		/// \brief The crate
		CUSTOMVERTEX*							crate;

		/// \brief Vertex Buffer.
		LPDIRECT3DVERTEXBUFFER9		vb;

		/// \brief Void pointer.
		void*													void_vb;

		/// \brief initialisation flag.
		bool														initialised;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Crate_Buffer*						Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Crate_Buffer;
																	}

																	return _instance;
																}

		/// \brief Class destructor.
																~Crate_Buffer();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Renders the crate buffer.
		void													render();

		/// \brief Set data for drawing by stages, (stream source and FVF)
		inline void										stage_set()
																{
																	   graphics->get_d3d_device()->SetStreamSource(0, vb, 0, sizeof(CUSTOMVERTEX));

																	graphics->get_d3d_device()->SetFVF(CUSTOM_FVF);
																}

		/// \brief Render by stages.
		void													render(int stage);

		/// \brief Initialises the buffer.
		void													init();
		//-------------------------------------------------------------------------------//


}CRATE_BUFFER,*PCRATE_BUFFER;

#endif // CRATE_BUFFER_H

