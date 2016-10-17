/// \file Game_Inventory.h
/// \author Jared Chidgey
/// \author Corrupt Software

#ifndef GAME_INVENTORY_H
#define GAME_INVENTORY_H


#include "Game_Item.h"

typedef class Game_Inventory
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//Items
		/// \brief Inventory of items.
		vector<ITEM>									inventory;
		//-------------------------------------------------------------------------------//
																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Inventory();

		/// \brief Class destructor.
																~Game_Inventory();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//Inventory interface
		/// \brief Adds an item to the inventory.
		bool													add_item(ITEM &to_add);

		/// \brief Removes an item from the inventory.
		bool													remove_item(string name, int count);
		//-------------------------------------------------------------------------------//


}INVENTORY,*PINVENTORY;

#endif // GAME_INVENTORY_H

