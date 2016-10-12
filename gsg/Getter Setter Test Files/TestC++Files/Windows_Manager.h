/// \file Windows_Manager.h
/// \author Jared Chidgey
/// \date 24/10/2008
/// \brief

#ifndef WINDOWS_MANAGER_H
#define WINDOWS_MANAGER_H

#include <windows.h>

typedef class Windows_Manager
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:

		//*****************************************************//
		//-------------------------------------------------------------------------------//singleton
		/// \brief Singleton instance.
		static Windows_Manager*									_instance;

		/// \brief Private class constructor.
																Windows_Manager();

		/// \brief Private class destructor.
																~Windows_Manager();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//windows data
		/// \brief Application instance.
		HINSTANCE												hinstance;

		/// \brief
		HWND													hwnd;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:

		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Singleton instancer.
		static Windows_Manager*									Instance()
																{
																	if(_instance == 0)
																	{
																		_instance = new Windows_Manager;
																	}

																	return _instance;
																}

		/// \brief Singleton destroyer.
		static void												Release()
																{
																	if(_instance)
																	{
																		delete _instance;
																		_instance = 0;
																	}
																}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//core
		/// \brief Initialises windows.
		bool													init(HINSTANCE new_i, LRESULT (CALLBACK* windows_procedure)(HWND, UINT, WPARAM, LPARAM) );
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Getters
		/// \brief Returns hInstance.
		HINSTANCE												get_hinstance()				{ return hinstance; }

		/// \brief Returns hWnd.
		HWND													get_hwnd()					{ return hwnd; }
		//-------------------------------------------------------------------------------//

}WIN_MAN,*PWIN_MAN;

#endif // WINDOWS_MANAGER_H
