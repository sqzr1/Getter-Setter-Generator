/*
   ******************************************************************************************
   Nim Game
   
   Student: Sam Zielke-Ryner
   SID:     41784707
   
   ******************************************************************************************
   Player Class:
   
   Uses inheritance to define the player object(both human & AI).
   
   ******************************************************************************************
*/

import java.util.*;


public abstract class Player
{
	
	// Class Variables:
	
	private int matchesOwned;
	private int lastMove;
	private int wins;
	private int losses;
	public String playerName;
	public char alias;
	
	
	// Class Methods:
	
	public Player( String name )
	{
		// Constructor:
		
		matchesOwned = 0;
		lastMove     = 0;
		wins         = 0;
		losses       = 0;
		playerName   = name;
		alias        = ( playerName.toUpperCase() ).charAt(0);
		
	}
	
	// Virtual Methods:
	
	abstract public SelectedObjectInfo makeMove( Vector <Pile> piles );
	
	public String getName()
	{
		// Post: Return this Players name
		
		return playerName;
		
	}
	
	
	public int incrementWin()
	{
		// Post: Increment wins & return its value
		
		wins++;
		return wins;
	}
	
	
	public int incrementLoss()
	{
		// Post: Increment wins & return its value
		
		losses++;
		return losses;
	}
	
	
	public void incrementMatches( int num )
	{
		// Post: Increment number of matches player owns
		
		matchesOwned += num;
		
	}
	
	
	public int getWins()
	{
		// Post: Return the total no. of wins this player has
		
		return wins;
	}
	
	
	public int getLosses()
	{
        // Post: Return the total no. of times this player has lost
		
		return losses;
	}
	
	
	public int getMatches()
	{
		// Post: Return number of matches this player owns
		
		return matchesOwned;	
	}
	
	
	public void storeLastMove( int pileValue, int matchValue )
	{
		// Post: Store the most recent game move made by this player
		
		lastMove = (pileValue * 100) + matchValue;
	}
	
	
	public int getLastMove()
	{
		// Post: Return the most recent game move player has made in encrypted form
		
		return lastMove;
	}
	
}


///////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                           //
//                            Child class of Player: Human Class                             //
//                                                                                           //
///////////////////////////////////////////////////////////////////////////////////////////////

class Human extends Player
{
	
	// Class Variables:
	
	
	// Class Methods:
	
	public Human(  String name )
	{
		// Constructor:
		
		super( name );
	}
	
	
	public SelectedObjectInfo makeMove( Vector <Pile> piles )
	{
		// Post: Unused but necessary to compile
		
		return null;
	}
}


///////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                           //
//                         Child class of Player: Computer Class                             //
//                                                                                           //
///////////////////////////////////////////////////////////////////////////////////////////////

class Computer extends Player
{
    
	// Class Variables:
	
	
	// Class Methods:
	
	public Computer( String name )
	{
		// Constructor:
		
		super( name );
	}
	

	public SelectedObjectInfo makeMove( Vector <Pile> piles )
	{
		// Post: Get computer to randomly select a pile to remove matches from.
		//       Get computer to randomly select how many matches to remove 
		//       the selected pile.
		
		int randomPile  = (int) (Math.random() * piles.size());
        int randomMatch = (int) ( Math.random() * piles.elementAt( randomPile ).size() );
		
        computerPause(1000);
        		
		return ( new SelectedObjectInfo( randomPile, randomMatch ));
		
	}
	
	
	private void computerPause( int nTime )
	{
		// Post: Make it appear the computer player is thinking about their
        //       next move
		
		try
		{
			System.out.println( "PAUSE BEGINS ");
			Thread.sleep( nTime );
		}
		catch ( InterruptedException ie )
		{
			return;
		}
		System.out.println( "PAUSE ENDS ");
	}
	
}

