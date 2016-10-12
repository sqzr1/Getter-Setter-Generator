/*
 * 
 */


import java.awt.GridLayout;
import java.util.Vector;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;


public class GameBoard extends JPanel
{
	
	/// Class Variables:
	private static final long serialVersionUID = 1L;
	private Vector <BoardCell> boardCells;
	private int freeCells;
	private ImageIcon defaultCellImg;
	private ImageIcon whiteCellImg;
	private ImageIcon blackCellImg;
	
	
	/// Class Methods:
	
	public GameBoard( GameWindow gameWindow )
	{
		
		this.setLayout( new GridLayout(7,7) );
		this.setBorder( new CompoundBorder (BorderFactory.createRaisedBevelBorder(),
                                            new EmptyBorder(3,3,3,3)) );
		
		boardCells     = new Vector <BoardCell>();
		freeCells      = 0;
		defaultCellImg = new ImageIcon( "emptyCell.png", "CellIcon" );
		whiteCellImg   = new ImageIcon( "whiteCell.png", "WhiteIcon" );
		blackCellImg   = new ImageIcon( "blackCell.png", "BlackIcon" );
		
		
		for (int i=0; i<49; i++)
		{
			boardCells.add( new BoardCell( gameWindow, defaultCellImg, i ) );
			this.add( boardCells.lastElement() );
			freeCells++;
		}
		
		this.validate();
		
	}
	
	
	public void captureCell( int cellID, int playerType ) throws PenteException
	{
		
		// Make sure cellID is a valid index value
		if ( cellID >= 0  &&  cellID < boardCells.size() )
		{
			
			switch ( playerType )
			{
				case 0: 
					boardCells.elementAt(cellID).occupyCell( blackCellImg );
				break;
				case 1: 
					boardCells.elementAt( cellID ).occupyCell( whiteCellImg );
				break;
				default:
					throw new PenteException( -950 );
			}
			
			freeCells--;
			
		}
		else throw new PenteException( -900 );
		
	}
	
	
	public void releaseCell( int cellID ) throws PenteException
	{
		
		if ( cellID >= 0  &&  cellID < boardCells.size() )
		{
			boardCells.elementAt( cellID ).releaseCell( defaultCellImg );
		}
		else throw new PenteException( -900 );
		
	}
	
	
	public boolean isFull()
	{
		
		return ( freeCells <= 0 );
		
	}
	
	
	public void clearBoard()
	{
		
		freeCells = boardCells.size();
		
		for ( int i=0; i<freeCells; i++ )
		{
			boardCells.elementAt(i).releaseCell( defaultCellImg );
		}
		
	}
	
}

