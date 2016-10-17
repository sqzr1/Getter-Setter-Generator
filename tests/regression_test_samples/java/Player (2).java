/*
 * 
 */



public class Player
{
	
	/// Class Variables:
	public int ID;
	protected String name;     // this variable is protected so I can extend this class to involve a computer player
	protected int[] lastMove;
	
	/// Class Methods:
	
	public Player( int ID, String name )
	{
		this.ID   = ID;
		this.name = name;
	}
	
	
	public int[] getLastMove()
	{
		
		if ( lastMove.length > 0 )
		{
			return lastMove;
		}
		else return null;
		
	}
	
	
	public void setLastMove( int move[] )
	{
		lastMove = move;
	}
}