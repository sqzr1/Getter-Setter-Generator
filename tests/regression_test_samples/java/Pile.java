/*
   ******************************************************************************************
   Nim Game
   
   Student: Sam Zielke-Ryner
   SID:     41784707
   
   ******************************************************************************************
   Pile & Match Class:
   
   Pile object contains a vector of match objects.
   ******************************************************************************************
*/

import java.util.*;
import java.awt.*;
import java.awt.geom.*;

public class Pile
{
	
	// Class Variables:
	
	public Vector <Match> myPile;
	private int freeMatches;
	public int x;
	public int y;
	public int width;
	public int height;
	
	public class Match
	{
		// Class Variables
		public char value;
		public char playerAlias;
		public int x;
		public int y;
		public int width;
		public int height;
		
		public Match()
		{
			// Constructor: 
			
			value  = '*';
			x      = 0;
			y      = 0;
			width  = 1;
			height = 1;
			playerAlias = '0';
		}
		
		public void setAttributes( int xPos, int yPos, int nWidth, int nHeight )
		{
			// Post: Set this objects logical attributes
			
			x      = xPos;
			y      = yPos;
			width  = nWidth;
			height = nHeight;
		}
		
		public void drawMatch( Graphics2D g2d )
		{
			// Post: Draws this object using 2d graphics according to its 
			//       state(value variable)
			
			
			switch ( value )
			{
				case '*':
				{	
					Ellipse2D.Double objRegion = new Ellipse2D.Double( x, y, width, height );
					g2d.fill( objRegion );
					
					g2d.setColor( Color.red);
					Ellipse2D.Double Region = new Ellipse2D.Double( x, y, 2, 2 );
					g2d.fill( Region );
					
					g2d.setColor( Color.blue);
					Ellipse2D.Double egion = new Ellipse2D.Double( x+width, y+height, 2, 2 );
					g2d.fill( egion );
					
					g2d.setColor( Color.black);
				}
				break;
				case 'x':
				{
					
					Line2D leftLn  = new Line2D.Double( x, y, x+width, y+height );
					Line2D rightLn = new Line2D.Double( x+width, y, x, y+height );
					g2d.setColor( Color.red);
					g2d.draw( leftLn );
					g2d.draw( rightLn );
					
					g2d.setColor( Color.black);
					value = playerAlias;
				}
				break;
				default:
					    // do nothing
				break;
			}
		}
		
		public boolean mouseCollision( int mouseX, int mouseY )
		{
			// Post: Returns true if the mouse has clicked inside this matches 
			//       region
			
			if ( (mouseX >= x && mouseX <= (x+width))  &&  (mouseY >= y && mouseY <= (y+height)) && (value == '*') )
			{	
				return true;
			}
			else return false;
			
		}
		
	}
	

	
	// Class Methods:
	
	public Pile(  int xPos, int yPos, int nWidth, int nHeight, int nSize )
	{
		// Constructor:
		
		myPile      = new Vector <Match>();
		x           = xPos;
		y           = yPos;
		width       = nWidth;
		height      = nHeight;
		freeMatches = nSize;
		
		for (int i=0; i<nSize; i++)
		{
			myPile.add( new Match() );
		}
	}
	
	
	public int capacity()
	{
		// Post: Return the capacity of this pile
		
		return myPile.size();
	}
	
	public int size()
	{
        // Post: Return the remaining matches in this pile
		
		return freeMatches;
	}
	
	
	public Match at( int index )
	{
		// Post: Return the Match object at the specified index
		
		if ( index >= 0 && index < myPile.size() )
		{
			return myPile.elementAt( index );
		}
		else return null;
		
	}
	
	
	public int remove( int matchIndex, char alias )
	{
		// Post: Remove n Matches from the pile & return the number of 
		//       matches we have removed
		
		
		int index = matchIndex; 
		
		if ( index < 0 )
		{
			return 0;
		}
		
		while ( index < this.capacity() && myPile.elementAt( index ).value == '*' )
		{
			myPile.elementAt( index ).value       = 'x';
			myPile.elementAt( index ).playerAlias = alias;
			freeMatches--;
			index++;
		}
		
		return index - matchIndex;
	    
	}
	
	
	public int replace(  int nMatches, char alias )
	{
		// Post: Replace n Matches back into the pile
		
		int pileCapacity = this.capacity();
		
		for (int i = 0, index = freeMatches; i<nMatches && freeMatches <= pileCapacity; i++, index++)
		{
			myPile.elementAt( index ).value = '*';
			freeMatches++;
		}
		
		return freeMatches;
		
	}
	
	
	public boolean mouseCollision( int mouseX, int mouseY )
	{
		// Post: Returns true if the mouse has clicked inside this piles' region
		
		if ( (mouseX >= x && mouseX <= (x+width))  &&  (mouseY >= y && mouseY <= (y+height)) && (freeMatches > 0) )
		{	
			return true;
		}
		else return false;
		
	}
	
	
	public Dimension getPostion()
	{
		// Post: Returns this objects x,y position as an Dimension object
		
		return  ( new Dimension(x, y) );
	}
	
	
	public Dimension getDimensions()
	{
		// Post: Returns this objects dimensions
		
		return ( new Dimension(width, height) );
	}
	
	
	public void clearHeap()
	{
		// Post: Replace all matches in pile(heap)
		
		while ( freeMatches != this.capacity() )
		{
			myPile.elementAt( freeMatches ).value = '*';
			freeMatches++;
		}
	}
	
}

