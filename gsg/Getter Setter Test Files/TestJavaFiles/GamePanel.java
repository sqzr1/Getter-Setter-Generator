/*
   ******************************************************************************************
   Nim Game
   
   Student: Sam Zielke-Ryner
   SID:     41784707
   
   ******************************************************************************************
   Game Panel Class:
   
   This object is an extension of a JPanel & where the main game board components(piles, 
   matches) are drawn onto. This object acts like a canvas where the game components are 
   drawn & erased as the gameplay changes. 
   
   ******************************************************************************************
*/

import javax.swing.*;

import java.awt.*;
import java.util.*;
import java.awt.font.FontRenderContext;
import java.awt.geom.Rectangle2D;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;


public class GamePanel extends JPanel implements MouseListener
{
	
	/// Class Variables:
	
	private enum DrawState { DRAWTITLE, DRAWGAMEPLAY, DRAWPLAYERSTATS };
	private DrawState drawState;
	private NimGameFrame parentWindow;
	private Vector <Pile> piles;
	private Vector <Player> players;
	private Player winner;
	
	/// Class Methods:
	
	
	/**
	
	   Constructor: 
	   
	   @param parent  the parent frame that declared this object
	   
	*/
	public GamePanel( NimGameFrame parent )
	{
		
		drawState       = DrawState.DRAWTITLE;
		parentWindow    = parent;
		piles           = new Vector <Pile>();
		players         = null;
		winner          = null;

        setSize( 500, 500);
		this.addMouseListener( this );
		
	}
	
	
	/**
	   
	   Post: According to the game state, this object draws the gameboard, 
	         title sequence & player results onto this objects client area
	         
	*/
	public void paintComponent( Graphics g )
	{
		
        super.paintComponent( g );
        this.setSize(500,500);
        Graphics2D g2d = (Graphics2D) g;
		
		
		switch ( drawState )
		{
		
			case DRAWGAMEPLAY:

				drawPiles( g2d );
                //computerPause( 1000 );
                
			break;
			
			case DRAWPLAYERSTATS:
				
				drawPlayerStats( g2d );
				
			break;
			
			case DRAWTITLE:
			default:
				
				drawTitleSequence( g2d );
				
			break;
			
		}
		
	}
	
	
	/**
	   Post: Determine if a match has been selected & inform game logic class of the
	         index of the match selected.
	*/
	public void mouseClicked( MouseEvent me )
	{
		
		//SelectedObjectInfo selectedMatch = findSelectedMatch( me.getX(), me.getY() );
		SelectedObjectInfo selectedMatch = findSelectedMatchEffic( me.getX(), me.getY() );
		
		if ( selectedMatch != null )
		{
			// send message to GameLogic class to remove n matches
			parentWindow.grabMatchesEvent( selectedMatch );
		}
		
	}

	
	/**
	   Post: Unused mouse event but necessary to compile
	*/
	public void mousePressed( MouseEvent me ) 
	{

	}

	
	/**
	   Post: Unused mouse event but necessary to compile 
	*/
	public void mouseReleased( MouseEvent me) 
	{
	       
	}

	
	/**
	   Post: Unused mouse event but necessary to compile 
	*/
	public void mouseEntered( MouseEvent me ) 
	{
		
	}

	
	/**
	   Post: Unused mouse event but necessary to compile
	*/
    public void mouseExited( MouseEvent me ) 
    {
	 
	}


    /**
	   Post: Set game panels 'drawing state' according to the game logic 
	         class's 'game state'
	         
	   @param  gameState  the game logic class's enumeration variable to
	                      determine the game state
	*/
    public void setDrawState( NimGameFrame.GameState gameState )
    {
    	
    	switch ( gameState )
    	{
	    	case GAMEINTRO:
			{
				drawState = DrawState.DRAWTITLE;
			}
			break;
			case GAMEPLAY:
			{
				drawState = DrawState.DRAWGAMEPLAY;
			}
			break;
			case GAMEEND:
			default:
			{
				drawState = DrawState.DRAWPLAYERSTATS;
			}
			break;
    	}
    	
    	// Which function do I call to make this object redraw itself?
    	this.invalidate(); // redraw self
    	this.repaint();
    	// this.revalidate();
    }
    
    
	/**
	 
	   Post: Invalidate the client area of this panel therefore call
	         the paint component function
	         
	   @param  nPiles     a vector containing the games's pile object. 
	                      This is required so we can call the drawSelf()
	                      function of each match within paintComponent();
	                   
	   @param  selPlayer  the current player whose turn it is. This is 
	                      required by the drawPlayerPrompt() function
	                      to obtain the players name.
	                      
	*/
	public void invalidatePanel( Vector <Pile> nPiles, Player selPlayer )
	{
		
		piles = nPiles;
		
		// Which function do I call to make this object redraw itself?
		this.invalidate();
		this.repaint();
		// this.revalidate(); 
		
	}
	
	
	/**
	   Post: Draw the welcome message & 'press Enter' prompt onto this
	         objects' client area
	*/
	private void drawTitleSequence( Graphics2D g2d )
	{
		
		String welcomeMsg = "Welcome to 'The Game of Nim' \nClick New Game button to begin";
		g2d.setFont(new Font("Serif", Font.PLAIN, 12));
        FontRenderContext frc = g2d.getFontRenderContext();
	    Font f = g2d.getFont();
		Rectangle2D b = f.getStringBounds( welcomeMsg, frc );
		
		g2d.setPaint( Color.blue );
        g2d.drawString( welcomeMsg, (int) (this.getWidth()/2 - b.getWidth()/2), 
        		        (int) (this.getHeight()/2 - b.getHeight()/2));

	}
	
	
	/**
	   Post: Draw matches & pile labels onto game board
	*/
	private void drawPiles( Graphics2D g2d )
	{
		
		for (int i=0; i < piles.size(); i++)
		{
			
			Pile selPile = piles.elementAt(i);
			
			// Draw this piles title
			g2d.drawString( "Pile no." + (i+1), selPile.at(0).x - 10, 
					selPile.at(0).y + selPile.at(0).height + 20 );
			
			// Draw each match that exists in selPile
			//for (int j=0; j < selPile.size(); j++)
			for (int j=0; j < selPile.capacity(); j++)
			{
				if ( selPile.at(j).value == '*' || selPile.at(j).value == 'x' )
					selPile.at(j).drawMatch( g2d );
			}
			
		}
		
	}
	
	
	/**
	   Post: Draw player statistics & end game result
	*/
	private void drawPlayerStats( Graphics2D g2d )
	{
		
		String result      = "";
		String winnerStats = " %s is the winner:  Total matches collected = %s \t No. of wins = %s \t No. of losses = %s \r\n\r\n";
		String loserStats  = " Player Name: %s  Total matches collected = %s \t No. of wins = %s \t No. of losses = %s \r\n\r\n";
		
		result += String.format( winnerStats, winner.getName(), winner.getMatches(), 
				                 winner.incrementWin(), winner.getLosses() );
		result += " Other Player statistics: \r\n";
		
		for (int i=0; i<players.size(); i++)
		{
			Player selPlayer = players.elementAt(i);
			
			if ( selPlayer.playerName != winner.playerName )
			{
				result += String.format( loserStats, selPlayer.getName(), 
						                 selPlayer.getMatches(), selPlayer.getWins(), 
						                 selPlayer.incrementLoss() );
			}
		}
		
		System.out.println( result );
		FontRenderContext frc = g2d.getFontRenderContext();
	    Font f = g2d.getFont();
		Rectangle2D b = f.getStringBounds( result, frc );
		
		g2d.drawString( result, (int) (this.getWidth()/2 - b.getWidth()/2), 
		        (int) (this.getHeight()/2 - b.getHeight()/2));
		
		//g2d.drawString( "Not implemented try to exit app", 10,10);
	}
	
	
	/**
	   Post: Find which Match has been selected by the users cursor,
	         return its index & its parent Pile's index as a
	         SelectedObjectInfo object
	         
	   @param  mouseX  the x coordinate of where the mouse left 
	                   clicked our client area. Units in client 
	                   coords as opposed to screen coords.
	                    
	   @param  mouseY  the y coordinate of where the mouse left 
	                   clicked our client area.
	                   
	   @return         returns an object called a SelectedObjectInfo
	                   which contains the index of the selected match 
	                   & the index of the matches parent pile.
	*/
	public SelectedObjectInfo findSelectedMatch( int mouseX, int mouseY )
	{
		
		for (int i=0; i < piles.size(); i++)
		{
			
			Pile selPile = piles.elementAt(i);
			
			for (int j=0; j < selPile.size(); j++)
			{
				// if mouse is inside this Matches region
				if ( selPile.at(j).mouseCollision( mouseX, mouseY ) )
				{
					  return ( new SelectedObjectInfo( i, j ));
				}
			}
			
		}
		
		return null; // mouse does not collide with ANY match
	}
	
	
	/**
	   Post: Determine which pile has been selected by the users cursor
	         if any, & call findMatch() to determine which match has
	         been selected.
	         This function utilises a binary search for speed &
	         efficiency
	         
	         
	   @param  mouseX  the x coordinate of where the mouse left 
	                   clicked our client area. Units in client 
	                   coords as opposed to screen coords.
	                    
	   @param  mouseY  the y coordinate of where the mouse left 
	                   clicked our client area.
	                   
	   @return         returns an object called a SelectedObjectInfo
	                   which contains the index of the selected match 
	                   & the index of the matches parent pile.
	                   
	*/
	public SelectedObjectInfo findSelectedMatchEffic( int mouseX, int mouseY )
	{
		
		int mid;
		int begin = 0;
		int end   = piles.size() - 1;
		
		
		if ( piles.size() <= 0 )
		{
			return null;
		}
		else if ( mouseX < piles.elementAt( begin ).x )
		{
			return null;
		}
		else if ( mouseX > (piles.elementAt( end ).x + piles.elementAt( end ).width) )
		{
			return null;
		}
		else if ( mouseY < piles.elementAt( end ).y )
		{
			return null;
		}
		else if ( mouseY > (piles.elementAt( begin ).y + piles.elementAt( begin ).height) )
		{
			return null;
		}
		
		
		while ( begin <= end )
		{
			
			mid = (begin + end) / 2;
			Pile selPile = piles.elementAt( mid );
			
			
			if ( selPile.mouseCollision( mouseX, mouseY ))
			{
				
				int matchIndex = findMatch( selPile, mouseX, mouseY );
				
				if ( matchIndex != -1 )
				{
					return ( new SelectedObjectInfo( mid, matchIndex ));
				}
				else break;
			}
			else if ( mouseX < selPile.x )
			{
				end = mid - 1;
			}
			else if ( mouseX > (selPile.x + selPile.width) )
			{
				begin = mid + 1;
			}
			
		}
		
		return null;
	}
	
	
	/**
	   Post: Find which Match has been selected by the users cursor
	         & return its index
	         This function utilises a binary search for speed &
	         efficiency
	         
	   @param  selPile  the pile whose region collides with the
	                    mouse coordindates.
	   
	   @param  mouseX   the x coordinate of where the mouse left 
	                    clicked our client area. Units in client 
	                    coords as opposed to screen coords.
	                    
	   @param  mouseY   the y coordinate of where the mouse left 
	                    clicked our client area.
	                    
	   @return          returns the index of the selected match.
	                    If no match has been selected then we
	                    return -1. 
	                    
	*/
	public int findMatch( Pile selPile, int mouseX, int mouseY )
	{
		
		int mid;
		int begin = 0;
		int end   = selPile.size() - 1;
		
		
		while ( begin <= end )
		{
			
			mid = (begin + end) / 2;
			
			
			if ( selPile.myPile.elementAt( mid ).mouseCollision( mouseX, mouseY ) == true )
			{
				return mid;
			}
			else if ( mouseY < selPile.myPile.elementAt( mid ).y )
			{
				begin = mid + 1;
			}
			else if ( mouseY > (selPile.myPile.elementAt( mid ).y + selPile.myPile.elementAt( mid ).height) )
			{
				end = mid - 1;
			}

		}
		
		return -1;
	}
	
	
	/**
	   
	   Post: Make it appear the computer player is thinking about their
	         next move
	   
	   @param  nTime  the duration/time(in milliseconds) we pause for.
	   
	*/
	private void computerPause( int nTime )
	{
		
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
	
	
	/**
	   Post: Store players & winner so we can print out attributes & statistics
	   
	   @param  playerList  a vector containing all players in this game
	   
	   @param  winnerP     the winning player of this game
	   
	*/
	public void sendPlayerStats( Vector <Player> playerList, Player winnerP )
	{
		players = playerList;
		winner  = winnerP;
	}
	
}


/**
 
  Selected Object Info Class
  
  Used as a container to determine the index of which pile &
  the index of which match has been selected.
  
*/
class SelectedObjectInfo
{
	public int pileIndex;
	public int matchIndex;
	
	/**
	 
     Constructor: 
	 
     @param nPile   the index of the selected pile.
	 
	 @param nMatch  the index of the selected match.
	 
	*/
	public SelectedObjectInfo( int nPile, int nMatch )
	{
		
		if ( nPile >= 0 )
		{
			pileIndex = nPile;
		}
		else nPile = 0;
	
		if ( nMatch >= 0 )
		{
			matchIndex = nMatch;
		}
		else nMatch = 0;
		
	}
	
}

