/// \file Game_Entity.h
/// \author Jared Chidgey
/// \author Student No. 11345826

#ifndef GAME_ENTITY_H
#define GAME_ENTITY_H

#include <d3d9.h>
#include <d3dx9.h>

#include "DX_Manager.h"
#include "Camera.h"

#include "Game_Terrain.h"

#include "Simple_Animation.h"
#include "Game_Collision.h"
#include "Character_Stats.h"
#include "Game_Gold.h"

#include "Game_Sound_Sample.h"

using namespace std;

/// \brief Base class represents an entity within the world

/// The class defines basic position, and existence,
///and handles collision detection

typedef class Game_Entity
{
																																			//
																																			//protected declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	protected:
		//*****************************************************//
		//-------------------------------------------------------------------------------//interfaces
		/// \brief Graphics interface.
		PGRAPHICS											graphics;

		/// \brief Timer interface (timed motion)
		PTIMER												timer;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//existence
		/// \brief Anchor, usually the centre of the object
		D3DXVECTOR3											anchor;

		/// \brief Position in the world.
		D3DXVECTOR3											position;

		/// \brief Previous position.
		D3DXVECTOR3											prev_position;

		/// \brief Bounding collision.
		COLLISION											collision;

		/// \brief The approximate height of the object.
		float												height;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//direction
		/// \brief The direction that the entity is looking in.
		D3DXVECTOR3											look;

		/// \brief The direction the entity is physically facing.
		D3DXVECTOR3											facing;

		/// \brief Used for strafing.
		D3DXVECTOR3											right;

		/// \brief Used fopr jumping.
		D3DXVECTOR3											up;

		/// \brief Time variable.
		float												time_passed;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//movement flags
		/// \brief Set to indicate the entities direction is to be updated.
		float												turn_flag;

		/// \brief Set to indicate the entities position is to be updated.
		float												walk_flag;

		/// \brief Set to indicate the entities position is to be updated.
		float												strafe_flag;
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//other
		/// \brief Character animations.
		PSIMP_ANIM											animations;

		/// \brief Entity stats.
		PCHAR_STATS											stats;

		/// \brief Number of animations.
		int													num_anims;

		/// \brief Current animation.
		int													cur_anim;

		/// \brief Direction of turn.
		float 												turn_a;

		/// \brief Entities gold.
		GOLD												gold;
		//-------------------------------------------------------------------------------//
																																			//
																																			//public declarations
	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public:
		//*****************************************************//
		//-------------------------------------------------------------------------------//construction
		/// \brief Class constructor.
															Game_Entity();

		/// \brief Class destructor.
		virtual												~Game_Entity() {}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//update
		/// \brief Updates the state of the entity.
		virtual void										update(PTERRAIN terrain) = 0;

		/// \brief Renders the player.
		virtual void										render() = 0;

		/// \brief Reverts to the previously stored position.
		void												revert();

		/// \brief Hooks the camera to the entities current position.
		virtual void										hook_camera(PCAMERA camera) = 0;

		/// \brief Interact with another entity.
		virtual void										interact(Game_Entity* other) = 0;

		/// \brief Interact with another entity.
		void												interact(PGOLD more_gold);

		/// \brief Returns a pointer to the stats class.
		inline PCHAR_STATS									get_stats()
															{
																return stats;
															}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//interaction
		/// \brief Returns player gold.
		inline PGOLD										get_gold()
															{
																return &gold;
															}
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//movment
		/// \brief Turns the entity in the specified direction.
		inline void											turn(float dir)
															{
																turn_flag = dir;
															}

		/// \brief Walks the entity in the specified direction.
		inline void											walk(float dir)
															{
																walk_flag = dir;
															}

		/// \brief Strafes the entity in the specified direction.
		inline void											strafe(float dir)
															{
																strafe_flag = dir;
															}

		inline COLLISION									get_collision()
															{
																return collision;
															}

		inline D3DXVECTOR3									get_position()
															{
																return position;
															}

		virtual void										zoom(float dir) = 0;

		void												debug();
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//get data

		//*****************************************************//
		//-------------------------------------------------------------------------------//collision
		bool												intersect(Game_Entity* other);

		bool												intersect(PGOLD other);
		//-------------------------------------------------------------------------------//


		//*****************************************************//
		//-------------------------------------------------------------------------------//file io
		/// \brief Load entity data from a file(string).
		virtual bool										load(string filename) = 0;

		/// \brief Load entity data from a file(fstream)
		virtual bool										load(fstream &file) = 0;
		//-------------------------------------------------------------------------------//

}ENTITY,*PENTITY;

#endif // GAME_ENTITY_H

