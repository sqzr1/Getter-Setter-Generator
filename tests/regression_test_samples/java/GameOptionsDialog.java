/*
   ******************************************************************************************
   Nim Game
   
   Student: Sam Zielke-Ryner
   SID:     41784707
   
   ******************************************************************************************
   Game Options Dialog Window:
   
   Allows the user to select & alter game attributes including; the number of piles, 
   the number of players & the type of players(Human or Computer).
   
   ******************************************************************************************
*/


import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.border.LineBorder;
import javax.swing.table.DefaultTableModel;
import java.util.*;



public class GameOptionsDialog extends JFrame implements ActionListener
{
	
	/// Class Variables:

	private JPanel mainPanel;
	private JLabel pileNumLbl;
	private JComboBox pileNumCb;
	private JLabel playersLbl;
	private JTable playersTb;
	private JButton addPlayerBt;
	private JButton removePlayerBt;
	private JButton moveUpBt;
	private JButton moveDownBt;
	private JButton cancelBt;
	private JButton beginGameBt;
	
	/// Game Logic Variables
	private NimGameFrame parentFrame;
	private int pileNum;
	private Vector <Player> players;
	
	/// Class Methods:
	
	/**
	   Constructor: 
	   
	   @param parent  the main application frame which declared this object
	*/
	public GameOptionsDialog( NimGameFrame parent )
	{
		
		parentFrame = parent;
		players = new Vector <Player>();
		pileNum = 9;
		
		this.setResizable( false );
		this.setTitle( "Game Options" );
		
		initialiseComponents();
		buildPanel();
		bindComponents();
		
		pack();
		this.setVisible( true );
		//playersTb.setSize( this.getWidth()-20, 100 );
		//playersTb.validate();
		//playersTb.repaint();
	}
	
	
	/**
	   Post: Handles all button messages/events
	*/
	public void actionPerformed( ActionEvent ev )
	{
		
		if ( ev.getSource() == pileNumCb )
		{
			
			JComboBox cb = (JComboBox) ev.getSource();
			pileNum = cb.getSelectedIndex() + 1;
			
		}
		else if ( ev.getSource() == addPlayerBt )
		{
			
			DefaultTableModel  model = (DefaultTableModel) playersTb.getModel();
			int tableSize = playersTb.getRowCount();
			
			Object newPlayer[] = { "Player" + tableSize, new Integer(0) };
			model.insertRow( tableSize-1, newPlayer );
			
			validate();
			
		}
		else if ( ev.getSource() == removePlayerBt )
		{
			
			DefaultTableModel  model = (DefaultTableModel) playersTb.getModel();
			int playersTbSize = playersTb.getRowCount();
			
			// Minimim allowed players = 2
			if ( playersTbSize > 2 )
			{
				int selIndex = playersTb.getSelectedRow();
				
				if ( selIndex != -1 )
					model.removeRow( selIndex );
				
			}
			else JOptionPane.showMessageDialog( this, 
                                                "Error: Minimum number of players is 2.", 
                                                "Error!", JOptionPane.ERROR_MESSAGE );
			
		}
		else if ( ev.getSource() == moveUpBt )
		{
			
			DefaultTableModel  model = (DefaultTableModel) playersTb.getModel();
			int selIndex = playersTb.getSelectedRow();
			
			if ( selIndex > 0 )
			{
				int upperIndex = selIndex - 1;
				model.moveRow( selIndex, selIndex, upperIndex );
			}
			else JOptionPane.showMessageDialog( this, 
                                                "Error: Row cannot move up any further.", 
                                                "Error!", JOptionPane.WARNING_MESSAGE );
			
		}
		else if ( ev.getSource() == moveDownBt )
		{
            
			DefaultTableModel  model = (DefaultTableModel) playersTb.getModel();
			int selIndex = playersTb.getSelectedRow();
			
			if ( selIndex < (playersTb.getRowCount()-1) && selIndex != -1 )
			{
				int lowerIndex = selIndex + 1;
				model.moveRow( selIndex, selIndex, lowerIndex );
			}
			else JOptionPane.showMessageDialog( this, 
					                            "Error: Row cannot move down any further.", 
					                            "Error!", JOptionPane.WARNING_MESSAGE );
			
		}
		else if ( ev.getSource() == cancelBt )
		{
			dispose(); // Is this the correct way to destroy a window??
		}
		else if ( ev.getSource() == beginGameBt )
		{
			
			DefaultTableModel  model = (DefaultTableModel) playersTb.getModel();
			int noOfPlayers = playersTb.getRowCount();
			
			for (int i=0; i<noOfPlayers; i++)
			{
				
				Object playerName = model.getValueAt(i, 0);
				Object playerType = model.getValueAt(i, 1);
				
				// if player type == Human
				if ( (Integer)playerType == 0 )
				{
					 players.add( new Human( (String)playerName ) );
				}
				else players.add( new Computer( (String)playerName ) );
				
			}
			
			parentFrame.newGameEvent( players, pileNum );
			dispose();
		}
		
	}
	
	
	/**
	   Post: Initialise all JComponents in this windows' frame
	*/
	private void initialiseComponents()
	{
		
		String pileOpt[]   = {"1","2","3","4","5","6","7","8","9"};
		String playerCol[] = {"Player Name","Player Type"};
		Object playerInfo[][] = { {"White", new Integer(0)},
				                  {"Black", new Integer(1)} };
		
		mainPanel      = (JPanel) getContentPane();
		pileNumLbl     = new JLabel( "No. of Piles:" );
		pileNumCb      = new JComboBox( pileOpt );
		playersLbl     = new JLabel( "Players" );
		playersTb      = new JTable( new DefaultTableModel(playerInfo, playerCol) );
		addPlayerBt    = new JButton( "Add Player" );
		removePlayerBt = new JButton( "Remove Player" );
		moveUpBt       = new JButton( "Move Up" );
		moveDownBt     = new JButton( "Move Down" );
		cancelBt       = new JButton( "Cancel" );
		beginGameBt    = new JButton( "Begin Game" );
		
		pileNumCb.setSelectedIndex( 8 ); 
		playersTb.setSelectionMode( ListSelectionModel.SINGLE_SELECTION );
		
	}
	
	
	/**
	   Post: Add all JComponents of this frame to our main panel 
	         & set window layout
	*/
	private void buildPanel()
	{
		
		mainPanel.setLayout( new BorderLayout() );
		mainPanel.setBorder( new CompoundBorder (BorderFactory.createRaisedBevelBorder(),
			    	                             new EmptyBorder(10,10,10,10)));
		                                         //new LineBorder( Color.darkGray, 10 ) );
		JPanel nthPanel = new JPanel();
		JPanel ctrPanel = new JPanel();
		JPanel sthPanel = new JPanel();
		JPanel uthPanel = new JPanel();
		Box horizBox    = Box.createHorizontalBox();
		
		nthPanel.setLayout( new GridLayout(2,3) );
		ctrPanel.setLayout( new BorderLayout() );
		//sthPanel.setLayout( new GridLayout(2,4) );
		
		nthPanel.add( new JLabel() );
		nthPanel.add( pileNumLbl );
		nthPanel.add( pileNumCb );
		nthPanel.add( playersLbl );
		nthPanel.add( new JLabel() );
		nthPanel.add( new JLabel() );
		
		ctrPanel.add( playersTb, BorderLayout.WEST );
		
		
		horizBox.add( addPlayerBt );
		horizBox.add( Box.createHorizontalStrut(10) );
		horizBox.add( removePlayerBt );
		horizBox.add( Box.createHorizontalStrut(10) );
		horizBox.add( moveUpBt );
		horizBox.add( Box.createHorizontalStrut(10) );
		horizBox.add( moveDownBt );
		sthPanel.add( horizBox );
		
		horizBox = Box.createHorizontalBox();
		horizBox.add( Box.createHorizontalGlue() );
		horizBox.add( Box.createHorizontalGlue() );
		horizBox.add( cancelBt );
		horizBox.add( Box.createHorizontalStrut(10) );
		horizBox.add( beginGameBt );
		uthPanel.add( horizBox );
		
		/*sthPanel.add( new JLabel() );
		sthPanel.add( new JLabel() );
		sthPanel.add( cancelBt );
		sthPanel.add( beginGameBt );*/
		
		/*sthPanel.add( addPlayerBt );
		sthPanel.add( removePlayerBt );
		sthPanel.add( moveUpBt );
		sthPanel.add( moveDownBt );
		sthPanel.add( new JLabel() );
		sthPanel.add( new JLabel() );
		sthPanel.add( cancelBt );
		sthPanel.add( beginGameBt );
		 */
		
		
		mainPanel.add( nthPanel, BorderLayout.NORTH );
		mainPanel.add( ctrPanel );
		//mainPanel.add( Box.createHorizontalStrut(20) );
		mainPanel.add( sthPanel, BorderLayout.SOUTH );
		mainPanel.add( uthPanel, BorderLayout.EAST );
		
	}
	
	
	/**
	   Post: Add relevant JComponents to event listeners
	*/
	private void bindComponents()
	{
		
		//playersTb.addActionListener( this );
		pileNumCb.addActionListener( this );
		addPlayerBt.addActionListener( this );
		removePlayerBt.addActionListener( this );
		moveUpBt.addActionListener( this );
		moveDownBt.addActionListener( this );
		cancelBt.addActionListener( this );
		beginGameBt.addActionListener( this );
		
	}
	
}

