import GetterSetterSourceCode
import GetterSetterVariable as Variable


code = """
/*
   
   Win32 Application: Custom Control - Update Box Example
   " Delete this"
         
   Description: This application demonstrates a Windows 32 Control I made 
                myself called an Update Box. This custom control is very 
                similar to the List Box control except it has more
                user-friendly dynamic features.        
   
                Update Box Features:
                  - Double Click to create a new Update Box cell.
                  - Change the data in a cell by left clicking on it
                  - Right click to open property dialog & append 
                    the control's attributes.
                    
   
   Header File: Custom Win32 Control Update Box Definition
   
*/

"abcdefghij"

#ifndef UPDATEBOX_H
#define UPDATEBOX_H

#include <windows.h>
#include <string>
#include <vector>

using namespace std;



/// Constants ///
#define UB_FOCUSCELL      50001
#define UB_PROPERTYDIALOG 50002
#define UBP_CONTROLBKCOL  50003
#define UBP_CELLBKCOL     50004
#define UBP_CELLFRAMECOL  50005
#define UBP_CELLTXTCOL    50006
#define UBP_APPLYCHANGES  50007
#define UBP_CANCEL        50008

#define VERIFYSUCCESS          (x) if(!x) return false;


/// Functions ///
void RegisterUpdatebox;
void RegisterUpdatePropertyDialog();
LRESULT CALLBACK UpdateBoxWndProc( HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam );
LRESULT CALLBACK UpdatePropertyDialogWndProc( HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam );


/// Update Box Cell Object ///
struct ubCell 
{
     
      // Public Functions
      ubCell( HWND Hwnd, POINT p, int nWidth, int nHeight, COLORREF colourProperties[] );
      ~ubCell();
      bool drawControl( HDC hdc );
      bool drawEditControl();


      // Public Variables
      // COLUMN parentCol; // consider a parent object column
      POINT pos;
      POINT textPos, GETIT, DIDUGETIT;
      int width;
      int height;
      HWND hwnd;
      HRGN region;
      HBRUSH bgBrush;
      HBRUSH frameBrush;
      COLORREF textColour;
      string data;
      bool
      
};


/// Update Box Properties Object ///
struct UpdatePropertyDialog 
{
      
      // Public Functions
      UpdatePropertyDialog( HWND hParent, COLORREF colourProperties[] );
      ~UpdatePropertyDialog();
      void createGUI( HWND hwnd );
      bool openColourDialog( HWND hwnd, UINT controlID );
      void applyColourChange( UINT controlID, COLORREF newColour );
      
      
      // Public Variables
      HWND parentHwnd;
      COLORREF bkColour;
      COLORREF cellBkColour;
      COLORREF cellFrameColour;
      COLORREF cellTextColour;
              
};


/// Win32 Control - Similar to a List Box control but with more custom functionality ///
class updateBox 
{
      
      public:
           // Public Variables
           ubCell *focusCell;
           ubCell *prevFocusCell;
           bool userDesignatedDraw;
           bool initialiseDraw;
           bool newColourAttrib;
           
           // Public Functions
           updateBox( HWND Hwnd, POINT p );
           ~updateBox();
           ubCell* addCell();
           void setDimensions( int nWidth, int nHeight );
           void setFocusCell();
           bool drawControl( HDC hdc );
           bool drawFocusCell();
           bool drawDefaultCell( HDC hdc );
           void redrawControl( HDC hdc );
           bool inCellRgn( int mouse_x, int mouse_y );
           ubCell* findSelection( int mouse_x, int mouse_y );
           void selectCell( int mouse_x, int mouse_y );
           void eraseRgn();
           void openPropertyDialog( HWND hwnd );
           void applyChanges( HWND hwnd, UpdatePropertyDialog *upd );
           
           // Efficent Alternative Functions
           bool inCellRgnEffic( int mouse_x, int mouse_y );
           ubCell* findSelectedCell( vector <ubCell*> &v, int mouse_x, 
                                     int mouse_y );
           
            
      private:
           
           class a 
           {
                 a();
                 
                 int ll;
                 
                 class b 
                 {
                       b();
                         
                       int dd;
                       
                       void messjfnedkj()

                       
                       UINT EditBoxID[] = { IDF_PATH1, IDF_PATH2, IDF_PATH3 };
                 };
                 
                 float gg;
           };
           
           POINT pos;
           int width;
           int height;
           int cellHeight;
           HWND hwnd;
           HWND focusEdit;
           HRGN region; // Why HRGN & not RECT? So I can develop this further to create controls that have irregular shapes
           HRGN cellRegion;
           HBRUSH bgBrush;
           HBRUSH frameBrush;
           COLORREF bkColour;
           COLORREF cellBkColour;
           COLORREF cellFrameColour;
           COLORREF cellTextColour;
           vector <ubCell*> cellList;
           //int columns;
           
};


#endif
"""

j_code = """
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


"""

p_code = """

"
TODO:

- Find a way to alocate a hash value to a word(tag object)
- Find a way to alocate a hash value to a SolvedProblem object
  based upon the Tag objects it contains

"

## Constants ##
tags            = {}
solved_problems = []



class Tag:

    ## Class Variables: ##

    # self.name
    # self.code


    ## Class Functions: ##
    
    def __init__( self, _name, _code ):
        " Default Constructor: "

        self.name = _name
        self.code = _code

    def hash_code( self ):

        h_code = 0
        index  = 1

        for char in self.name:

            h_code += (char - '0') * index


        self.code = h_code
        
        return self.code



    
class SolvedProblem:

    ## Class Variables: ##

    # self.problem_tags:  a list containing tags associated/related
    #                     to this solution
    # self.h_code      :  hash_code value
    


    ## Class Functions: ##
    
    def __init__( self, problem_tags ):
        " Default Constructor: "

        self.problem_tags = problem_tags
        self.h_code       = self.hash_code()
        

    def hash_code( self ):

        h_code = 0
        

        for tag in self.problem_tags:

            h_code += tag.hash_code()


        self.h_code = h_code
        
        return self.h_code
    

    def get_relation( self, tag_list ):
        " Post: "

        hit_rate = 0
        
        for tag in tag_list:

            if not self.problem_tags.index( tag ) == -1:

                hit_rate += 1


        return hit_rate


    def get_relation_ex( self, tag_list ):
        " Post: "

        hit_rate = 0
        
        for tag in tag_list:

            if not self.problem_tags.index( tag ) == -1:

                hit_rate += 1


        return hit_rate



def remove_common_words( inverted_index ):

    common_words = ('the', 'is', 'at')

    for word in common_words:

        try:

            # inverted_index.pop( word )
            del inverted_index[ word ]

        except KeyError:

            " Add this exeption to debugging 'Event Log' "

    return inverted_index



def parse_email_contents( email_content, ignore_common_words ):
    " Post: "

    inverted_index = {}
    email_content = email_content.lower()

    for word in email_content.split():

        if inverted_index.has_key( word ):

            inverted_index[ word ] += 1;

        else:

            inverted_index[ word ] = 1


    # I could have removed these words from the Str rather than adding them
    # to the inverted index THEN deleting them from the Str BUT I believe
    # it is faster to search for & remove an element from a Dictionary(Map)
    # compared to searching for a wrd in a string then removing it
    if ignore_common_words  ==  True:

        inverted_index = remove_common_words( inverted_index )
    

    return inverted_index



def get_frequent_terms( inverted_index, n_terms ):
    " Post: "

    frequent_terms = []
    words          = inverted_index.keys()
    word_frequency = inverted_index.values()
    
    while ( n_terms > 0  and len(words) > 0 ):

        wrd_occrnc     = max(word_frequency)

        if wrd_occrnc <= 1:
            break
        
        freq_wrd_index = word_frequency.index( wrd_occrnc )

        frequent_terms.append( words[ freq_wrd_index ] )
        del words[ freq_wrd_index ]
        del word_frequency[ freq_wrd_index ]
        n_terms -= 1

    return frequent_terms



def get_key_terms( inverted_index, n_terms ):
    " Post: Search for specific key terms that may exist/occur in
              email contents(inverted_index) "

    key_terms = ( 'dvc', 'commbox', 'combox', 'video', 'commander',
                  'lite', 'avbox', 'mkii', 'det', 'joey', 'micro',
                  'micro6', 'digital', 'signage' )

    # I want to find out which key terms if any occur in inverted index
    # I want to find out the n most frequent key terms in inverted index
    # I want to return those n most frequent key terms in a list

        
        

def get_related_problems( frequent_terms, solved_problems, min_hit_rate ):
    " Post: "

    related_problems = []
    
    for problem in solved_problems:

        hit_rate = problem.get_relation( frequent_terms )

        if ( hit_rate >= min_hit_rate):

            related_problems.append( problem )


    return related_problems



### Main ###

if __name__ == "__main__":
    
    b = "  A B C D A D E F G H B"

    a = parse_email_contents( b, ignore_common_words = True )
    c = get_frequent_terms( a, 9 )


    print c



### Initiate Program ###

main()

"""

codeObj  = GetterSetterSourceCode.JavaCode( j_code )

var_list = codeObj.find_variables()


print "\n\nVARIABLES FOUND: "
for v in var_list:

    print v.var_name + ", " + str(v.data_type) + ", " + v.wrapper_name



"""def find_first_char( s, pos ):
    """ """

    chars = ':{;'
    found = [ n for n in [ s.rfind(c, 0, pos) for c in chars ] if not n==-1 ]

    if len(found) == 0:
        return -1
    else:
        return max(found)

    
m = " :uh h  Should have got me ;"

print m[ find_first_char(m, 8) ]"""


