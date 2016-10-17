/*
   ******************************************************************************************
   Nim Game
   
   Student: Sam Zielke-Ryner
   SID:     41784707
   
   ******************************************************************************************
   Game Logic & Game Window Class:
   
   Controls all aspects of the game activity & creates the main frame window 
   
   ******************************************************************************************
*/


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.*;
import java.io.*;


/**
   
   Main Class to allow user to play game
   
*/
public class NimGameFrame extends JFrame implements ActionListener
{
	
	/// Class Variables:
	
	// GUI Components
	private JPanel mainPanel;
	private JPanel menuPanel;
	private GamePanel drawPanel;
	private JButton newGameBut;
	
	// Game variables
	public enum GameState { GAMEINTRO, GAMEPLAY, GAMEEND };
	private GameState gameState;
	private Vector <Pile> piles;
	private Vector <Player> players;
	private int playerIndex;
	
	
	/// Class Methods:
	
	/**
	   Constructor:
	   
	*/
	public NimGameFrame()
	{
		
		this.setSize( 700, 500 );
		this.setTitle( "Game of Nim" );
		this.setDefaultCloseOperation( EXIT_ON_CLOSE );
		this.setResizable( true );
		
		playerIndex = -1;
		players     = new Vector <Player>();
		piles       = new Vector <Pile>();
		
		
		initialiseControls();
		buildPanel();
		bindControls();
		
		
		setGameState( GameState.GAMEINTRO );
		
		
		//validate(); // pack(); ???
		this.setVisible( true );
		
	}
	
	
	/**
	 
	   Post: Handle all button events for this frame
	   
	*/
	public void actionPerformed( ActionEvent ev )
	{
		
		if ( ev.getSource() == newGameBut )
		{
			GameOptionsDialog gameOptions = new GameOptionsDialog( this );
			gameOptions.setLocationRelativeTo( this );
		}
		else return;
		
	}
	
	
	
	/**
	   Post: Set the current game state thus call relevant logic functions
	   
	   @param  currentState  the current state of the game
	   
	*/
	private void setGameState( GameState currentState )
	{
		
		gameState = currentState;
		
		
		switch (gameState)
		{
			case GAMEINTRO:
			{
				drawPanel.setDrawState( gameState );
				drawPanel.invalidatePanel( piles, null );
			}
			break;
			case GAMEPLAY:
			{
				drawPanel.setDrawState( gameState );
				drawPanel.invalidatePanel( piles, null );
				performGameLogic();
			}
			break;
			case GAMEEND:
			default:
			{
				drawPanel.sendPlayerStats( players, players.elementAt( playerIndex ));
				drawPanel.setDrawState( gameState );
				drawPanel.invalidatePanel( piles, null );
				// incrementPlayerStats();
			}
			break;
		}
	}
	
	
	/**
	 
	   Post: Responsible for advancing a players turn, testing whether the 
	         game has ended & redrawing/invalidating the game board panel
	   
	*/
	private void performGameLogic()
	{
		
		drawPanel.invalidatePanel( piles, null ); // Redraw game board
		
		if ( isGameOver() )
		{
			setGameState( GameState.GAMEEND );
			return;
		}
		
		// Advance player turn
		if ( playerIndex < players.size() - 1  )
		{
			playerIndex++;
		}
		else playerIndex = 0;
		
		
		Player selPlayer = players.elementAt( playerIndex );
		
		// Is is a computer players turn
		if ( selPlayer instanceof Computer )
		{
			SelectedObjectInfo computerMove = selPlayer.makeMove( piles );
			int matchesRemoved = piles.elementAt( computerMove.pileIndex ).remove( computerMove.matchIndex, 
                                                                                   selPlayer.alias );
            selPlayer.incrementMatches( matchesRemoved );
            performGameLogic();
		} 
		
	}
	
	/**
	
	   Post: Initialise window components
	   
	*/
	private void initialiseControls()
	{
		
		mainPanel      = (JPanel) getContentPane();
		menuPanel      = new JPanel();
		drawPanel      = new GamePanel( this );
		newGameBut     = new JButton( "New Game" );
		
	}
	
	
	/**
	
	   Post: Add components to main panel & set main panel layout
	   
	*/
	private void buildPanel()
	{
		
		Box box = Box.createVerticalBox();
		Box hBox = Box.createHorizontalBox();
		
		
		//mainPanel.setLayout( new BorderLayout() );
		menuPanel.setLayout( new BoxLayout( menuPanel, BoxLayout.Y_AXIS ));
		menuPanel.setBackground( Color.lightGray );
		
		box.add( Box.createVerticalStrut( 10 ));
		box.add( newGameBut );
		box.add( Box.createVerticalStrut( 10 ));
		box.add( Box.createVerticalGlue() );
		box.add( Box.createHorizontalStrut( 10 ));
		//box.add( grabMatchesBut );
		box.add( Box.createVerticalStrut( 10 ));
		hBox.add( Box.createHorizontalStrut( 20 ));
		
		menuPanel.add( box );
		menuPanel.add( hBox );
		//menuPanel.setSize( 200, 500);
	    mainPanel.add( menuPanel, BorderLayout.WEST );
	    mainPanel.add( drawPanel );
		
	    // Set Draw Panel Dimensions
	    //Dimension windowDim = this.getSize();
	    //int menuWidth       = (int) menuPanel.getSize().getWidth();
		//drawPanel.setSize( (int) windowDim.getWidth() - menuWidth, (int) windowDim.getHeight() );
	    //menuPanel.setSize( 200, 500);
	    //drawPanel.setSize( 500, 500);
	    //drawPanel.setPanelDimensions();
	    
	}
	
	
	/**
	
	   Post: Add event listeners
	   
	*/
	private void bindControls()
	{
		
		newGameBut.addActionListener( this );
		
	}
	
	
	/**
	   
	   Post: Begin a new game & clear all game variables
	   
	*/
	public void newGameEvent( Vector <Player> playerList, int nPiles )
	{
		
		players.clear();
		players = playerList;
		playerIndex = -1;
		buildPiles( nPiles, 10 );
		setGameState( GameState.GAMEPLAY );
		
	}
	
	
	/**
	
	   Post: A player has selected matches to remove, if it is a
	         human players turn then remove selected matches from
	         a pile.
	         
	   @param selectedMatch  object containing the selected pile 
	                         index & the selected match index.
	   
	*/
	public void grabMatchesEvent( SelectedObjectInfo selectedMatch )
	{
		
		Player selPlayer = players.elementAt( playerIndex );
		
		// Make sure it is not the computers turn
		if ( selPlayer instanceof Human )
		{
			// Remove x matches from n pile
			int matchesRemoved = piles.elementAt( selectedMatch.pileIndex ).remove( selectedMatch.matchIndex, 
					                                                                selPlayer.alias );
			selPlayer.incrementMatches( matchesRemoved );
			drawPanel.invalidatePanel( piles, selPlayer ); // draw matches 'X' sprite
			performGameLogic();
		}
		
	}
	
	
	/**
	
	   Post: Create piles of matches & set their dimensions 
	         according to the available window width & height
	         
	   @param  pileNum   the number of piles the player has 
	                     chosen to play with.
	                  
	   @param  pileSize  the number of matches each pile 
	                     contains.
	   
	*/
	private void buildPiles( int pileNum, int pileSize )
	{
		piles.clear();
		
		Dimension drawPanelDim = drawPanel.getSize();
		int panelWidth  = (int) drawPanelDim.getWidth();
		int panelHeight = (int) drawPanelDim.getHeight();
		
		int hGapNum = pileNum + 1;
		int vGapNum = pileSize + 1;
		int hGap    = (int) panelWidth / (pileNum + hGapNum);
		int vGap    = (int) (panelHeight * 0.8) / (pileSize + vGapNum);
		
		int pileWidth   = hGap;
		int pileHeight  = vGap * (pileSize + vGapNum) ;
		int matchWidth  = pileWidth;
		int matchHeight = vGap;
		
		int yBegin = (int)(panelHeight * 0.85) - pileHeight;
		int xStart = ( panelWidth - (hGap * (pileNum + hGapNum - 1)) ) / 2;
		int yStart = yBegin;
			
		// Create our piles & define their coords & dimensions
		for (int i=0; i < pileNum; i++)
		{
			
			Pile newPile = new Pile( xStart, yStart, pileWidth, pileHeight, pileSize );
			
			// Define each matches coords & dimensions (that exist inside newPile)
			for (int j = (pileSize - 1); j >= 0 ; j--)
			{
				newPile.at(j).setAttributes( xStart, yStart, matchWidth, matchHeight );
				yStart += vGap * 2;
			}
			
			piles.add( newPile );
			xStart += hGap * 2;
			yStart  = yBegin;
			
		}
	}
	
	
	/**
	   Post: Clear game board & restack all piles with matches
	   
	*/
	public void clear()
	{
		
		for (int i=0; i<piles.size(); i++)
		{
			piles.elementAt( i ).clearHeap();
		}
		
	}
	
	
	/**
	   Post: Returns true if the game is finished(there are no more matches)
	         & we have a winner
	   
	*/
	public boolean isGameOver()
	{
		
		for (int i=0; i<piles.size(); i++)
		{
			if ( piles.elementAt(i).size() > 0 )
			
				return false;
		}
		
		return true;
	}
	
}

