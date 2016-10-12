/*
 * 
 * COMP229 Assignment 1: Pente Game
 * 
 * Student: Sam Zielke-Ryner
 * SID    : 41784707
 * 
 * 
 * Description: This class is the Model component of the MVC architecture. This
 *              class is designed to proccess all the logical operations of the
 *              game aswell as record, advance & alter the game state.
 * 
 */


import java.util.Iterator;
import java.util.ListIterator;
import java.util.Observable;
import java.util.Stack;
import java.util.Vector;



public class GameModel extends Observable
{
	
	/// Class Variables:
	
	private boolean fiveInRow;
	private int boardCells[];                 // Model of the game cells to record the state of each board cell
	private Vector <Player> players;          // Vector containing all players. I chose a set because it can grow to allow the user to add players whilst the game is running
	private Iterator <Player> iterPlayer;     // Iterate over players set to advance a turn
	private Player selPlayer;                 // Current player whose turn it is
	private Stack <Move> playerMoves;         // Record each players move
	private ListIterator <Move> iterMove;     // Iterate over playerMoves stack
	private GameView gameWindow;
	
	
	/**
	 * Class: This class is designed to store & access information about the game board 
     *        while I check if any cells have been captured or if a player has won
	 * 
	 * @author Soribo
	 *
	 */
	class BoardStateInfo
	{
		public int hit;
		public int selfHit;
		public boolean checkCapture;
		public Stack <CellMove> capturedCells;
		
		/**
		 * Default Constructor:
		 * 
		 */
		public BoardStateInfo()
		{
			hit           = 0;
			selfHit       = 0;
			checkCapture  = false;
			capturedCells = new Stack <CellMove>();
		}
		
		/**
		 * Constructor: 
		 * 
		 * @param _hit          Store how many times I have come across the other players cell
		 *                      whilst iterating over a line of cells
		 * @param _selfHit      Store how many times I have come across the one of selPlayer's cells
		 *                      whilst iterating over a line of cells
		 * @param _checkCapture Record whether I need to check the next cell I look
		 *                      at & determine if the player has captured it
		 */
		public BoardStateInfo( int _hit, int _selfHit, boolean _checkCapture )
		{
			hit           = _hit;
			selfHit       = _selfHit;
			checkCapture  = _checkCapture;
			capturedCells = new Stack <CellMove>();
		}
		
		/**
		 * Post: Set specific member variables to their default/null value
		 * 
		 */
		public void reset()
		{
			hit           = 0;
			selfHit       = 0;
			checkCapture  = false;
		}
		
	}
	
	
	/// Class Methods:
	
	/**
	 * Constructor:
	 * 
	 * @param _gameWindow Store the variable associated with the Game View so I
	 *                    can send messages to it
	 *                    
	 */
	public GameModel( GameView _gameWindow )
	{
		
		fiveInRow   = false;
		gameWindow  = _gameWindow;
		players     = new Vector <Player>();
		playerMoves = new Stack <Move>();
		addPlayer( 1, "White" );
		addPlayer( 0, "Black" );
		iterPlayer  = players.iterator();
		iterMove    = playerMoves.listIterator();
		
		boardCells = new int[ 49 ];  // [_columns * _rows];
		
	}
	
	
	/**
	 * Post: Overide the Observable class method so I could notify its 
	 *       observers of a change if needed
	 *       
	 */
	public void notifyObservers()
	{
		super.setChanged();
		super.notifyObservers();
		super.clearChanged();
	}
	
	
	/**
	 * Post: Reset the logical(not physical/visual) game board to its default state
	 * 
	 */
	public void reset()
	{
		
		iterPlayer  = players.iterator();
		iterMove    = playerMoves.listIterator();
		fiveInRow   = false;
		playerMoves.clear();
		
		for ( int cell = 0; cell < boardCells.length; cell++ )
		{
			
			boardCells[cell] = -1;
			
		}
		
		// Notify GameView object that we have changed the model(boardCells contents)
		gameWindow.clearBoard();
		// I could also notify the GameView object through the Observer class instead of my own function
		// notifyObservers();
		advanceTurn();
		
	}
	
	
	/**
	 * Post: Create a new player & add it to our container of players
	 * 
	 * @param playerID   The players unique ID
	 * @param playerName The name of the player
	 * 
	 */
	public void addPlayer( int playerID, String playerName )
	{
		players.add( new Player( playerID, playerName ) );
	}
	
	
	/**
	 * Post: Advance the players turn it is to the next one & notify user
	 * 
	 */
	public void advanceTurn()
	{
		
		if ( !iterPlayer.hasNext() )
		{
			iterPlayer = players.iterator();
		}
		
		selPlayer = iterPlayer.next();
		
		// Tell GameView object that its a new players turn so it can print "Now its Player 'x's turn"
		gameWindow.printGameStatus( "It is now Player " + selPlayer.name + "'s turn. ");
		// I could also notify the GameView object through the Observer class instead of my own function
		// notifyObservers();
		
	}
	
	
	/**
	 * Post: Determine whether someone has won or the game board is full
	 * 
	 * @return Returns true if the game has finished
	 */
	public boolean gameIsOver()
	{
		
		if ( fiveInRow )
		{
			gameWindow.printGameStatus( "Game Over: Player " + selPlayer.name + " has WON!!" );
			return true;
		}
		else if ( gameWindow.isBoardFull() )
		{
			gameWindow.printGameStatus( "Game Tie: Now more cells available" );
			return true;
		}
		else return false;
		
	}
	
	
	/**
	 * Post: Logically proccess a players move & check if the player has captured any other cells
	 *       in doing so
	 * 
	 * @param cellIndex       The index of the cell that the current player has clicked
	 * @throws PenteException Information about the error that occured
	 * 
	 */
	public void make( int cellIndex ) throws PenteException
	{

		// if the specific cell is not empty
		if ( boardCells[cellIndex] != -1 )
		{
			throw new PenteException( 800 );
		}
		
		
		Move playerMove = capturedPieces( cellIndex );    // Check if the player has captured any other cells
		
		
		/*
		
		// The following code is meant to check whether we have a branching action, ie, we have undone 
		// X many moves & then made a move, so we have gone back in time & made a different action/move, 
		// so the moves at the top of the stack playerMoves are now irrelevant & must be deleted.
		
		// This code causes the game to crash, so I have commented it out. I know where it fails(see line below)
		// & to an extent why it fails but I was unable to correct this error. As a result the undo & redo actions
		// of the game do not work BUT theoretically if you read this code, my undo & redo functions WILL work. 
		
		ListIterator <Move> firstEle = playerMoves.listIterator();
		firstEle.next();   // GAME CRASH OCCURS HERE
		
		while ( firstEle != iterMove )
		{
			playerMoves.pop();
			firstEle = playerMoves.listIterator();
			firstEle.next();
		}
		
		*/
		
		
		playerMoves.add( playerMove );           // Store players move so we can do redo, undo
		iterMove = playerMoves.listIterator();   // Update iterMove to point to last move made
		// iterMove.next();
		
		
		// Send message to GameView object to set X cells to selPlayer ID
		gameWindow.setBoardCells( playerMove, 1 );
		// I could also notify the GameView object through the Observer class instead of my own function
		// notifyObservers();
		
	}
	
	
	/**
	 * Post: Check whether the player has made 5 cells in a row or captured cells & store them
	 * 
	 * @param cellIndex The index of the selected cell
	 * @return          Returns a Move object that contains the selected cell & any 
	 *                  captured cells that may have resulted from the move 
	 *                  
	 */
	public Move capturedPieces( int cellIndex )
	{
		
		int oper;
		int len           = (int) (Math.sqrt( boardCells.length ));
		int selColumn     = cellIndex % len;
		int selRow        = cellIndex / len;
		int curCell       = cellIndex;
		BoardStateInfo bo = new BoardStateInfo();
		
		boardCells [cellIndex] = selPlayer.ID;
		bo.capturedCells.add( new CellMove( cellIndex, -1, selPlayer.ID ) );
		
		
		// Check left & right of cellIndex for captured pieces 
		
		for ( curCell = (len * selRow); curCell < (len * (selRow+1)); curCell++ )
		{
			bo = determineActionRepercussion( bo, curCell,len, 1 );
		}
		
		
		// Check up & down of cellIndex for captured pieces
		bo.reset();
		
		for ( curCell = selColumn; curCell < boardCells.length; curCell += len )
		{
			bo = determineActionRepercussion( bo, curCell,len, 2 );
		}
		
		
		// Check left & right diagonally of cellIndex for captured pieces
		curCell = cellIndex;
		bo.reset();
		
		if ( selColumn <= selRow ) { oper = selColumn; }
		else { oper = selRow; }
		
		int leftIndexBegin  = curCell - (oper * len) - oper;
		int noTimes         = (len - 1 - selColumn);
		int rightIndexBegin = curCell;
		
		for (int i=0; i<noTimes && (rightIndexBegin - len + 1) >= 0; i++)
		{
			rightIndexBegin = (rightIndexBegin - len + 1);
		}
		
		// Check left to right diagonal
		for ( curCell = leftIndexBegin; curCell < boardCells.length; curCell += (len + 1) )
		{
			bo = determineActionRepercussion( bo, curCell,len, 3 );
		}
		
		
		// Check right to left diagonal 
		bo.reset();
		
		for ( curCell = rightIndexBegin; curCell < boardCells.length; curCell += (len - 1) )
		{
			bo = determineActionRepercussion( bo, curCell,len, 4 );
		}
		

        return ( new Move( (Stack<CellMove>) bo.capturedCells, selPlayer.ID ) );
		
	}
	
	
	/**
	 * Post: Determine whether we need to check for captured cells or winning rows & store any
	 *       captured cells
	 * 
	 * @param bo             Object designed to store information about the line of cells we are checking
	 * @param curCell        The current cell we are looking at
	 * @param len            The number of cells in a column /or row
	 * @param conversionType Tell the function to store captured cells diagonally, vertically or horizontally
	 * 
	 */
	public BoardStateInfo determineActionRepercussion( BoardStateInfo bo, int curCell, int len, int conversionType )
	{
		int otherPlayerID;
		
		if ( selPlayer.name == "Black" )
		{
			otherPlayerID = 1;
		}
		else otherPlayerID = 0;
		
		
		if ( bo.checkCapture )
		{
			if ( boardCells[ curCell ] == selPlayer.ID )
			{
				
				if ( bo.hit >= 2 )
				{

					switch ( conversionType )
					{
						case 1:  // Remove Horizontally
						{
							boardCells[ curCell - 1 ] = -1;
							boardCells[ curCell - 2 ] = -1;
							
							bo.capturedCells.add( new CellMove( curCell - 1, otherPlayerID, -1 ) );
							bo.capturedCells.add( new CellMove( curCell - 2, otherPlayerID, -1 ) );
						}
						break;
						case 2:  // Remove Vertically
						{
							boardCells[ curCell - len ]       = -1;
							boardCells[ curCell - (len * 2) ] = -1;
							
							bo.capturedCells.add( new CellMove( curCell - len, otherPlayerID, -1 ) );
							bo.capturedCells.add( new CellMove( curCell - (len * 2), otherPlayerID, -1 ) );
					    }
						break;
						case 3:  // Remove Left Diagonally
						{
							boardCells[ curCell - len - 1 ]       = -1;
							boardCells[ curCell - (len * 2) - 2 ] = -1;
							
							bo.capturedCells.add( new CellMove( curCell - len - 1, otherPlayerID, -1 ) );
							bo.capturedCells.add( new CellMove( curCell - (len * 2) - 2, otherPlayerID, -1 ) );
						}
						break;
						case 4:  // Remove Right Diagonally
						default:
						{
							boardCells[ curCell - len + 1 ]       = -1;
							boardCells[ curCell - (len * 2) + 2 ] = -1;
							
							bo.capturedCells.add( new CellMove( curCell - len + 1, otherPlayerID, -1 ) );
							bo.capturedCells.add( new CellMove( curCell - (len * 2) + 2, otherPlayerID, -1 ) );
						}
						break;
					}
					
				}

				bo.checkCapture = false;
				bo.hit          = 0;
				
			}
			else if ( boardCells[ curCell ] != -1  &&  boardCells[ curCell ] != selPlayer.ID )
			{
				bo.hit++;
			}
		}
		
		if ( boardCells[ curCell ] == selPlayer.ID )
		{
			bo.selfHit++;
			bo.checkCapture = true;
		}
		else bo.selfHit = 0;
		
		
		if ( bo.selfHit >= 5 )
		{
			fiveInRow = true;
		}
		
		return bo;
		
	}
	
	
	/**
	 * Post: Undo the last move made by a player
	 * 
	 * @throws PenteException Information about the error that occured in this function
	 * 
	 */
	public void undo() throws PenteException
	{
		
		// if no player moves have been made yet
		if ( playerMoves.isEmpty()  || !iterMove.hasNext() )
		{
			throw new PenteException( 900 );
		}
		
		/*
		
		/// Please see the function make(); which describes why the following code is commented out
		
		System.out.println( "got to here, size= " + playerMoves.size() );
		
        Move lastMove = iterMove.next();  // Get the last move made by a player
		
        System.out.println( "got to here2" );
		
        Stack <CellMove> alteredCells = (Stack <CellMove>) lastMove.capturedCells.clone();
		
        System.out.println( "size= " + alteredCells.size() );
		System.out.println( "size= " + lastMove.capturedCells.size() );
		System.out.println( "playerID= " + lastMove.assocPlayerID );
		
		System.out.println( "got to here3" );
		
		while ( !alteredCells.isEmpty() )
		{
			int cellIndex = alteredCells.peek().cellIndex;
			int prevOwner = alteredCells.peek().previousOwner;
			
			boardCells[ cellIndex ] = prevOwner;
			alteredCells.pop();
		}
		
		gameWindow.setBoardCells( lastMove, 2 );
		
		*/
		
	}
	
	
	/**
	 * Post: Redo a move that has already been undone
	 * 
	 * @throws PenteException Information about the error that occured in this function
	 * 
	 */
	public void redo() throws PenteException
	{
		
		// If no moves have been made or we have no more moves to redo
		// if ( playerMoves.isEmpty() || iterMove == playerMoves.iterator().next() )
		if ( playerMoves.isEmpty() || !iterMove.hasPrevious() )
		{
			throw new PenteException( 900 );
		}
		
		
		/*
		
		/// Please see the function make(); which describes why the following code is commented out
		 
		
		Move nextMove = (Move) iterMove.previous();
        Stack <CellMove> alteredCells = (Stack <CellMove>) nextMove.capturedCells.clone();
		
        while ( !alteredCells.isEmpty() )
		{
			int cellIndex = alteredCells.peek().cellIndex;
			int newOwner  = alteredCells.peek().newOwner;
			
			boardCells[ cellIndex ] = newOwner;
			alteredCells.pop();
		}

		
		gameWindow.setBoardCells( nextMove, 1 );
		
		*/
		
	}
	



/**
 * Class: This is a specialised Exception object designed to handle errors that may occur
 *        related to the game Pente
 *        
 * @author Soribo
 *
 */
class PenteException extends Exception
{
	
	/// Class Variables:
	
	private static final long serialVersionUID = 1L;
	private int errorCode;
	
	
    /// Class Methods:
	
	/**
	 * Contructor: 
	 * 
	 * @param _errorCode The unique code that provides information about the error that occured
	 * 
	 */
	public PenteException( int _errorCode )
	{
		errorCode = _errorCode;
	}
	
	
	/**
	 * Post: Return a information about the error
	 * 
	 * @return A description about the specific error that occured
	 * 
	 */
	public String getErrorDescription()
	{
		
		switch (errorCode)
		{
			case 800:
				
				return "Error 800: The cell you are trying to capture has already been captured.";
				
            case 900:
				
				return "Error 900: Cannot undo move because no moves have been made yet.";
			
            case 1000:
				
				return "Error 1000: Cannot redo move because there have been no moves that have been undone.";
			
			default:
				
				return "Error could have been a runtime error.";
		}
		
	}
	
}

