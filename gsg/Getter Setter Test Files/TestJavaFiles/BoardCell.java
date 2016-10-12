/*
 * 
 */


import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JButton;


public class BoardCell extends JButton
{
	
	/// Class Variables:
	private static final long serialVersionUID = 1L;
    public int ID;
	
	/// Class Methods:
	
	public BoardCell( ActionListener gameWindow, ImageIcon defaultIcon, int ID )
	{
		
		this.setIcon( defaultIcon );
		this.addActionListener( gameWindow );
		this.ID = ID;
		
	}
	
	
	public void occupyCell( ImageIcon playerIcon )
	{
		
		this.setIcon( playerIcon );
		this.setEnabled( false );
		
	}
	
	
	public void releaseCell( ImageIcon defaultIcon )
	{
		
		this.setIcon( defaultIcon );
		this.setEnabled( true );
		
	}
	
}