/*
 * 
 */


import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;



public class GameWindow extends JFrame implements ActionListener
{
	
	/// Class Variables:
	private static final long serialVersionUID = 1L;
	private JPanel mainPanel;
	private JPanel componentPanel;
	private JTextField gameStatusField;
	
	private GameController gameController;

	
	/// Class Methods:
	
	public GameWindow( GameController gameController )
	{
		
		this.gameController = gameController;
		
		this.setSize( 400, 400 );
		this.setTitle( "Pente Game: Assignment 1" );
		this.setMinimumSize( new Dimension(500,650) );
		this.setDefaultCloseOperation( EXIT_ON_CLOSE );
		
		initVariables();
		
		// Dont make window visible yet
		
	}
	
	
	public void initVariables()
	{
		
		
	}
	
	public void initComponents( GameBoard gameBoard )
	{
		
		mainPanel       = (JPanel) getContentPane();
		componentPanel  = new JPanel();
		gameStatusField = new JTextField( "Game Beginning..." );
		JButton undo    = new JButton( "Undo" );
		JButton redo    = new JButton( "Redo" );
		JButton clear   = new JButton( "Clear" );
		
		mainPanel.setLayout( new BorderLayout(1,3) );
		componentPanel.setLayout( new FlowLayout() );
		mainPanel.setBorder( new CompoundBorder (BorderFactory.createRaisedBevelBorder(),
                                                 new EmptyBorder(10,10,10,10)) );
		gameStatusField.setEditable( false );
		
		componentPanel.add( undo );
		componentPanel.add( redo );
		componentPanel.add( clear );
		
		mainPanel.add( gameBoard, BorderLayout.NORTH );
		mainPanel.add( componentPanel, BorderLayout.CENTER );
		mainPanel.add( gameStatusField, BorderLayout.SOUTH );
		
		// Bind button actions
		undo.addActionListener( this );
		redo.addActionListener( this );
		clear.addActionListener( this );
		
		this.pack();
		this.validate();
		this.setVisible( false );
		
	}
	
	
	public void actionPerformed( ActionEvent ev )
	{
		
		Object src = ev.getSource();
		
		
		try
		{
			if ( ((JButton)src).getText() == "Undo" )
			{
				gameController.windowProc( GameController.GameMessage.UNDO, null );
			}
			else if ( ((JButton)src).getText() == "Redo" )
			{
				gameController.windowProc( GameController.GameMessage.REDO, null );
			}
			else if ( ((JButton)src).getText() == "Clear" )
			{
				gameController.windowProc( GameController.GameMessage.GAME_BEGIN, null );
			} 
			else 
			{
				gameController.windowProc( GameController.GameMessage.MOVE, src );
			}
		}
		catch ( Exception e )
		{
			// Catch if we cast to a JButton when we are not allowed to!!!
			System.out.println( e.getMessage() );
			System.out.println( e.getCause() );
		}
		
	}
	
	
	public void printGameStatus( String statusStr )
	{
		
		// gameStatusField.setText( "Blah" ); //statusStr );
		
	}
	
}