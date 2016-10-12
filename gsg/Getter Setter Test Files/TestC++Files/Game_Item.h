/// \file Game_Item.h
/// \author Jared Chidgey
/// \author Corrupt Software

#ifndef GAME_ITEM_H
#define GAME_ITEM_H

#include "DX_Manager.h"

#include <fstream>
#include <string>

#include "Simple_Animation.h"

#include "Game_Terrain.h"

#include "Game_Entity.h"

using namespace std;

const string TYPE_NONE = "NONE";

/// \brief An item within the game.

typedef class Game_Item : public Game_Entity
{
																																			//
																																			//private declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	private:
		//*****************************************************//
		//-------------------------------------------------------------------------------//representation
		/// \brief Inventory pic.
		LPDIRECT3DTEXTURE9				pic;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//item values
		/// \brief Name of the item
		string												name;

		/// \brief Type of the item.
		string												type;

		/// \brief Value.
		int													value;

		/// \brief Where there are multiple numbers of the same object.
		int													count;

		/// \brief Combineed value.
		int													combined_value;
		//-------------------------------------------------------------------------------//

																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
																Game_Item();

		/// \brief Class copy constructor.
																Game_Item(Game_Item &rhs);

		/// \brief Class copy constructor (const variant).
																Game_Item(const Game_Item &rhs);

		/// \brief Class destructor.
																~Game_Item();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//operator functions
		/// \brief Operator += function.
		void													operator+=(Game_Item &rhs);

		/// \brief Operator -= function.
		void													operator-=(Game_Item &rhs);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Update item state.
		void													update(PTERRAIN terrain);

		/// \brief Renders the item in the 3d world.
		void													render();

		/// \brief Renders the item as part of the an inventory.
		void													render_menu(float pos_x, float pos_y, float pos_z, int alpha);

				/// \brief Reverts to the previously stored position.
		void													revert();

		/// \brief Unimplemented
		void													hook_camera(PCAMERA camera)
																{

																}

		/// \brief unimplemented
		void													zoom(float dir)
																{

																}


		/// \brief Interact with another entity.
		void													interact(Game_Entity* other);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//data
		/// \brief Retruns the name of the item.
		inline string									get_name()
															{
																return name;
															}

		/// \brief Gets the count of the item.
		inline int										get_count()
															{
																return count;
															}

		/// \brief Sets the count
		inline void									set_count(int new_c)
															{
																count = new_c;
															}

		/// \brief Sets the world position.
		void												set_position(D3DXVECTOR3 new_pos);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load from file (string).
		bool													load(string filename);

		/// \brief Loads from a file (fstream).
		bool													load(fstream &file);
		//-------------------------------------------------------------------------------//

}ITEM,*PITEM;

#endif // GAME_ITEM_H

