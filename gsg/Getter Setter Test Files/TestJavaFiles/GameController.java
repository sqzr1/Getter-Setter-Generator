/*
 * 
 */


import java.util.Iterator;
import java.util.Vector;


public class GameController 
{
	// MUST ADD A MOVE COUNTER!!!!!!!!!!!
	/// Class Variables:
	public enum GameMessage { GAME_BEGIN, GAME_END, MOVE, UNDO, REDO, CLEAR };
	private GameWindow gameWindow;          // GUI window
	private GameBoard gameBoard;            // GameBoard
	private Vector <Player> players;        // List of players
	private Player selPlayer;               // Current player whose turn it is
	private Iterator <Player> iterPlayer;   // Iterate through player vector/set
	private int boardCells[];               // Logical game board cells list
	
	private boolean programEnd;
	public boolean gameEnd;

	
	
	/// Class Methods:
	
	public GameController()
	{
		
		initVariables();
	}
	
	
	public void initVariables()
	{
		
		programEnd = false;
		gameEnd    = false;
		players    = new Vector<Player>();
		boardCells = new int[49];
		
		gameWindow = new GameWindow( this );
		gameBoard  = new GameBoard( gameWindow );
		gameWindow.initComponents( gameBoard );
		
		// Create 2 players
		players.add( new Player( 1, "White" ) );
		players.add( new Player( 0, "Black" ) );
		
		iterPlayer = players.iterator();
		selPlayer  = iterPlayer.next();
		
	}
	
	
	public void mainLoop()
	{
		
		while ( !programEnd )
		{
			// Prompt select player colour
			//  v2.O - prompt select board size
		    //       - prompt select num of players
			
			gameWindow.setVisible( true );
			
			
			// getWinner();
			// prompt to play again
			//    if no break while loop OR programEnd = true;

		}
		
		// display goodbye
		// program end
	}
	
	
	public void windowProc( GameMessage msg, Object wParam ) throws PenteException
	{
		
		switch ( msg )
		{
		
			case GAME_BEGIN:
		    {
		    	
		    	reset();
		    	
		    }
		    break;
			case MOVE:
		    {
		    	
                // Check that the wParam object is a BoardCell object
                // if ( wParam.getClass() != BoardCell )
		    	if ( !(wParam instanceof BoardCell) )
		    	{
		    		throw new PenteException( -800 );
		    	}
                
		    	BoardCell selCell = (BoardCell) wParam;
				int ID = selCell.ID;
				
				if ( !isValidMove( ID ) )
				{
					throw new PenteException( -1000 );
				}
				
				boardCells[ID] = selPlayer.ID;
				System.out.println( "Selected Cell ID=" + ID + "\nBoardcell[ID] =" + boardCells[ID] );
				int capturedCells[] = findCapturedCells( ID );
				
				gameBoard.captureCell( ID, selPlayer.ID );
				
				/*
				for ( int i=0; i<capturedCells.length; i++ )
				{
				     
				     gameBoard.captureCell( capturedCells[i], selPlayer.ID );
				}
				*/
				
				selPlayer.setLastMove( capturedCells );
				gameWindow.printGameStatus( "Player " + selPlayer.name + " has captured " + capturedCells.length + "cells" );
				
				boolean gameOver = gameBoard.isFull();

                if ( gameOver )
			    {
			       // conduct winner function & pass selPlayer as param
			       // maybe send message windowProc( GAME_END ); INSIDE the mentioned function above
			    }
				   
				advanceTurn();
				
		    }
		    break;
		    case UNDO:
		    {
		    	
		    	int lastMove[] = selPlayer.getLastMove();
		    	
		    	if ( lastMove == null )
		    	{
		    		throw new PenteException( -700 );
		    	}
		    	
		    	for ( int i=0; i<lastMove.length; i++ )
		    	{
		    		gameBoard.releaseCell( lastMove[i] );
		    	}
		    	
		    	selPlayer.setLastMove( null );
		    	
		    	// advanceTurn(); ???
		    	
		    }
		    break;
		    case REDO:
		    {
		    	// Have no idea to do here
		    }
		    break;
		    case CLEAR:
		    {
		    	// Maybe unecessary, just use game begin!!
		    }
		    break;
		    case GAME_END:
		    {
		    	
		    }
		    break;
			default:
			{
				throw new PenteException( -1100 );
			}
		}
	}
	
	
	public void reset()
	{
		// initialises the board to remove all pebbles, resets the game history and zeroes the move counter. 
		
		clearCells();
    	gameBoard.clearBoard();
    	
    	// Clear players' last move records
    	for ( int i=0; i<players.size(); i++ )
    	{
    		players.elementAt(i).setLastMove( null );
    	}
    	
    	iterPlayer = players.iterator();
    	advanceTurn();
	}
	
	
	public boolean gameIsOver()
	{
		//returns a boolean to flag when the game has ended
		return true;
	}
	
	
	public int[] capturedPieces()
	{
		// to determine whether a pair of pieces have been captured by the last move
		
		// consider returning a Move object instead of an array
		return new int[1];
	}
	
	
	public void move()
	{
		// makes a move by updating the game state once the current player has decided how he wants to make the move. 
		// Notice how you can use the ideas of encapsulating the data with the methods that can update the data to 
		// structure the program so that the data required to make the move is not required as input to the move 
		// (although naturally that information must be preserved somewhere! 
	}
	
	
	public void undo()
	{
		// steps back one move in the game history, updating the board to reflect the fact that the last move has been rescinded. 
		
	}
	
	
	public void redo()
	{
		// steps forward one move in the game history, updating the board to reinstate the last move rescinded by a call to undo(). 
	}
	
	
	public boolean isValidMove( int cellID )
	{
		
		if ( boardCells[cellID] != -1 )
		{
			return false;
		}
		
		return true;
		
	}
	
	
	public int[] findCapturedCells( int cellID )
	{
		
		return new int[1];
		
	}
	
	
	public boolean advanceTurn()
	{
		
		// If board cell is already occupied
		
		
		// Check if selPlayer has captured any areas
		// update selPlayers last move
		
		// Check if game is over, we have a winner - Player winner = isWinner();
		/*   
		
		if ( winner != NULL ) 
		{   
		    gameWindow.printGameStatus( "Winner is " + winner.name ); 
            clearBoard(); 
            gameWindow.resetBoard(); 
		}
		
		*/
		
		
		if ( !iterPlayer.hasNext() )
		{
			iterPlayer = players.iterator();
		}
		
		selPlayer  = iterPlayer.next();
		
		return true;
		
	}
	
	
	public void clearCells()
	{
		
		for ( int i=0; i<boardCells.length; i++ )
		{
			boardCells[i] = -1;
		}
		
	}
	
	
	/// Main Method
	public static void main( String[] args )
	{
		
		GameController gameControl = new GameController();
		gameControl.mainLoop();  // Delete this !!!
		gameControl.windowProc( GameController.GameMessage.GAME_BEGIN, null );
	
	}
	
}



class PenteException extends Exception
{
	
	/// Class Variables:
	private static final long serialVersionUID = 1L;
	private int errorCode;
	
	/// Class Methods:
	
	PenteException( int _errorCode )
	{
		errorCode = _errorCode;
	}
	
}

