/*
   VCoder Project: WebScraping Google Searches for Search Data
   
   Description: I came across a project on VCoder.com of someone wanting a webscraper of google that 
                imports a set of search terms from a csv file, queries google with that search term,
                obtains the number of search results obtained & the time the search took & finally
                saving all the search result data to a csv file.
*/


import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.Enumeration;
import java.util.Vector;
import javax.swing.BorderFactory;
import javax.swing.Box;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.border.Border;
import javax.swing.border.CompoundBorder;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileFilter;
import javax.swing.table.DefaultTableModel;



/**
 * 
 * Class: The View component of the MVC model. This class displays the visual/graphical
 *        component of the application & takes user input.
 *
 */
public class View extends JFrame implements ActionListener
{
	/// Class Variables:
	
	private static final long  serialVersionUID = 1L;
	private SearchController   appController;
	private JPanel             mainPanel;
	private JButton            importCSVFile;
	private JButton            getSearchData;
	private JButton            saveCSVFile;
	private JTable             searchResultsTable;
	public  File               curFile;
	
	static class EngineSelectionRbPanel 
	{
		  public static Container createEngineSelectionPanel( View _appView, String elements[], String title) 
		  {
		    JPanel selectionPanel = new JPanel();
		    Box hBox              = Box.createHorizontalBox();
		    selectionPanel. setPreferredSize( new Dimension(5, 0) );

		    if (title != null) 
		    {
		      Border border = BorderFactory.createTitledBorder( title );
		      selectionPanel.setBorder( border );
		    }

		    ButtonGroup rbGroup = new ButtonGroup();
		    JRadioButton engineRb;

		    for (int i = 0, n = elements.length; i < n; i++) 
		    {
		      engineRb = new JRadioButton( elements[i] );
		      hBox     .add( engineRb);
		      hBox     .add( Box.createHorizontalStrut( 5 ) );
		      rbGroup  .add( engineRb );
		      engineRb .addActionListener( _appView );
		    }
		    
		    hBox.setSize( 50, 20 );
		    hBox.setBackground( Color.red );
		    selectionPanel .add( hBox );
		    
		    // Select 1st button
		    if ( elements.length > 0 )
		    {
		    	@SuppressWarnings("rawtypes")
				Enumeration buttonEn = rbGroup.getElements();
		    	JRadioButton firstRb = (JRadioButton) buttonEn.nextElement();
		    	rbGroup.setSelected( firstRb.getModel(), true );
		    }
		    
		    return selectionPanel;
		  }
		  
	}
	
	
	
	/// Class Methods:
	
	public View( SearchController _appController, Dimension _windowDim )
	{
		this.setSize( _windowDim );
		this.setTitle( "VCoder Project" );
		this.setDefaultCloseOperation( EXIT_ON_CLOSE );
		
		appController = _appController;
		curFile       = new File( System.getProperty("user.dir") );
		initComponents();
		
		this.validate();
		this.setVisible( true );
	}
	
	
	/**
	 * Post: Foward input messages & complimentary data to the Controller component/
	 *       class so we can interpret the users input & perform the users intended
	 *       actions
	 * 
	 * @param e  ActionEvent object containing information about the input 
	 *           we have received such as the input device that has received
	 *           the input & etc.
	 */
	@Override
	public void actionPerformed( ActionEvent e ) 
	{
		
		Object src = e.getSource();
		
		if ( src == importCSVFile )
		{
			File inputFile = showFileDialog( FileChooser.ChooserType.OPEN_DIALOG );
			
			if ( inputFile != null )
			{
				appController.windowProc( SearchController.AppMessage.SR_READ_CSV_FILE, inputFile );
			}
		}
		else if ( src == getSearchData )
		{
			appController.windowProc( SearchController.AppMessage.SR_GET_SEARCH_DATA, null );
		}
		else if ( src == saveCSVFile )
		{
			File outputFile = showFileDialog( FileChooser.ChooserType.SAVE_DIALOG );
			
			if ( outputFile != null )
			{
				appController.windowProc( SearchController.AppMessage.SR_SAVE_SEARCH_DATA, outputFile );
			}
		}
		else if ( src instanceof JRadioButton )
		{
			changeSearchEngine( ((JRadioButton) src).getText() );
		}
		else appController.windowProc( SearchController.AppMessage.SR_CLOSE, null );
		
	}
	
	
	/**
	 * Post: Initialise & build the GUI of this application
	 * 
	 */
	public void initComponents()
	{
		String colNames[] = { "Search Term", "No. of Search Results", "Search Time" };
		
		mainPanel                = (JPanel) getContentPane();
		Box buttonPanel          = Box.createVerticalBox();
		Box searchResultPanel    = Box.createVerticalBox();
		JButton exitBt           = new JButton( "Exit" );
		importCSVFile            = new JButton( "Import Search Terms" );
		getSearchData            = new JButton( "Retrieve Search Data" );
		saveCSVFile              = new JButton( "Save Search Data"     );
		searchResultsTable       = new JTable( new DefaultTableModel(null, colNames) );
		JScrollPane scrollPane   = new JScrollPane( searchResultsTable );
		JLabel searchTableLbl    = new JLabel( "Search Results" );
		Container engineRbGrp    = EngineSelectionRbPanel.createEngineSelectionPanel( this, 
				                                                                      new String[] {"Google", "Yahoo"},
				                                                                      "Search Engine" );
		
		mainPanel          .setLayout( new BorderLayout() );
		searchResultsTable .setPreferredScrollableViewportSize(new Dimension(390,400) );
		searchResultsTable .setSelectionMode( ListSelectionModel.MULTIPLE_INTERVAL_SELECTION );
		searchResultsTable .setFillsViewportHeight( true );
		importCSVFile      .setPreferredSize( new Dimension(160,30) );
		getSearchData      .setPreferredSize( new Dimension(160,30) );
		saveCSVFile        .setPreferredSize( new Dimension(160,30) );
		searchTableLbl     .setBackground( Color.red );
		
		mainPanel          .setBorder( new CompoundBorder (BorderFactory.createRaisedBevelBorder(),
                                                           new EmptyBorder(10,10,10,10)));
		
		buttonPanel        .add( Box.createVerticalStrut( 10 ) );
		buttonPanel        .add( importCSVFile );
		buttonPanel        .add( Box.createVerticalStrut( 10 ) );
		buttonPanel        .add( getSearchData );
		buttonPanel        .add( Box.createVerticalStrut( 10 ) );
		buttonPanel        .add( saveCSVFile );
		buttonPanel        .add( Box.createVerticalStrut( 10 ) );
		buttonPanel        .add( engineRbGrp );
		buttonPanel        .add( Box.createVerticalGlue() );
		buttonPanel        .add( exitBt, BorderLayout.SOUTH );
		
		searchResultPanel  .add( searchTableLbl );
		searchResultPanel  .add( scrollPane );
		
		mainPanel          .add( buttonPanel, BorderLayout.WEST );
		mainPanel          .add( Box.createHorizontalStrut( 10 ), BorderLayout.CENTER );
		mainPanel          .add( searchResultPanel, BorderLayout.EAST );
		
		importCSVFile      .addActionListener( this );
		getSearchData      .addActionListener( this );
		saveCSVFile        .addActionListener( this );
		exitBt             .addActionListener( this );
		
	}
	
	
	/**
	 * Post: Show a message dialog & inform the application user of an
	 *       invalid action or error that has occured
	 * 
	 * @param errorMsg  the error message to be displayed in the message dialog
	 * 
	 */
	public void showErrorDialog( String errorMsg )
	{
		JOptionPane.showMessageDialog( this, errorMsg, "Error:", 
				                       JOptionPane.ERROR_MESSAGE );
	}
	
	
	/**
	 * Post: Open a save or open file dialog & allow an application user to select a file to
	 *       work with
	 * 
	 * @param dialogType  enumeration variable used to identify whether you want to display 
	 *                    an open file dialog or a save file dialog
	 * @return            return the selected file the user has selected in the FileDialog &
	 *                    which they wish append/work with
	 *                    
	 */
	public File showFileDialog( FileChooser.ChooserType dialogType )
	{
		
		FileChooser fileDialog = new FileChooser( this, dialogType, curFile );
		
		int returnVal = fileDialog.showDialog();
		
		if ( returnVal == JFileChooser.APPROVE_OPTION )
		{
			File outputFile = fileDialog.getSelectedFile();
			curFile         = outputFile;
			return outputFile;
		}
		
		return null;

	}
	
	
	/**
	 * Post: Visually change the selected search engine that we wish to use to obtain search 
	 *       results with & foward a message to the Controller component so we can logically
	 *       change the selected search engine
	 * 
	 * @param rbText  the search engine the user want to work with (as a string variable)
	 * 
	 */
	public void changeSearchEngine( String rbText )
	{
		if ( rbText == "Google" )
		{
			appController.windowProc( SearchController.AppMessage.SR_CHANGE_ENGINE, 0 );
		}
		else // ( rbText == "Yahoo" )
		{
			appController.windowProc( SearchController.AppMessage.SR_CHANGE_ENGINE, 1 );
		}
	}
	
	
	/**
	 * Post: Display the search result data obtained by the Model component in our JTable
	 *       so the application user can view it
	 *       Uses a different method to identify which JTable row to place search result 
	 *       data into
	 * 
	 * @param rows  a 2d array ([rows][search result data]) containing the search result 
	 *              data that we wish to display in the JTable
	 * 
	 */
	public void updateTableRow( Object[][] rows )
	{
		DefaultTableModel model   = (DefaultTableModel) searchResultsTable.getModel();
		boolean searchTermPresent = false;
		
		for ( int j=0; j<rows.length; j++ )
		{
			String searchTerm = (String) rows[j][0];
			
			for ( int i=0; i<model.getRowCount(); i++ )
			{
				String currentTerm = (String) model.getValueAt( i, 0);
				
				if ( currentTerm == searchTerm )
				{
					model.setValueAt( rows[j][1], i, 1);
					model.setValueAt( rows[j][2], i, 2);
					searchTermPresent = true;
				}
			}
			
			if ( !searchTermPresent )
			{
				model.addRow( rows[j] );
			}
			
			searchTermPresent = false;
		}
	
	}
	
	
	/**
	 * Post: Display the search result data obtained by the Model component in our JTable
	 *       so the application user can view it
	 *       Uses a different method to identify which JTable row to place search result 
	 *       data into
	 * 
	 * @param rows  a 2d array ([rows][search result data]) containing the search result 
	 *              data that we wish to display in the JTable
	 * 
	 */
	public void updateTableRowEx( Object[][] rows )
	{
		DefaultTableModel model     = (DefaultTableModel) searchResultsTable.getModel();
		Vector <String> searchTerms = new Vector <String>();
		
		
		// Get all search terms pressent
		for ( int i=0; i<model.getRowCount(); i++ )
		{
			searchTerms.add( (String) model.getValueAt( i, 0 ) );
		}
		
		
		// Append row or insert new search term data
		for ( int i=0; i<rows.length; i++ )
		{
			Object curTerm = rows[i][0];
			
			if ( searchTerms.contains( curTerm ) )
			{
				int curRow = searchTerms.indexOf( curTerm );
				model.setValueAt( rows[i][1], curRow, 1);
				model.setValueAt( rows[i][2], curRow, 2);
			}
			else model.addRow( rows[i] );
		}
	}
	
	
	/**
	 * Post: Delete all rows from the JTable
	 * 
	 */
	public void clearTable()
	{
		DefaultTableModel model = (DefaultTableModel) searchResultsTable.getModel();
		
		while ( model.getRowCount() > 0 )
		{
			model.removeRow( 0 );
		}
	}
	
}



/**
 * 
 * Class: Extends the JFileChooser to make it more simple to use.
 *        A programmer can easily create an open or save dialog
 *        just by creating an object of this class & using an
 *        enumeration to define which type they wish
 *
 */
class FileChooser extends JFileChooser
{
    /// Class Variables:
	
	public enum ChooserType  { OPEN_DIALOG, SAVE_DIALOG };
	private static final long  serialVersionUID = 1L;
	private ChooserType        dialogType;
	private JFrame             parentFrame;
	
	class ExtensionFileFilter extends FileFilter
	{
		
		private String validExt;
		private String description;
		
		public ExtensionFileFilter( String _description, String _validExt )
		{
			validExt    = _validExt;
			description = _description;
		}
		
		public boolean accept(File file) 
		{
		    if ( file.isDirectory() ) 
		    {
		      return true;
		    } 
		    else 
		    {
		      String path = file.getAbsolutePath().toLowerCase();
		      
		      if ( (path.endsWith(validExt) && (path.charAt(path.length() - validExt.length() - 1)) == '.') ) 
		      {
		          return true;
		      }
		    }
		    
		    return false;
		}

		@Override
		public String getDescription() 
		{
			return description;
		}
		
	}
	
	/// Class Methods:
	
	public FileChooser( JFrame _parentFrame, ChooserType _dialogType, File currentDir )
	{
		parentFrame = _parentFrame;
		dialogType  = _dialogType;
		
		FileFilter fileFilter = new ExtensionFileFilter("Only allow csv files", "csv" );
		this.setFileFilter( fileFilter );
		this.setFileSelectionMode( JFileChooser.FILES_ONLY );
		this.setCurrentDirectory( currentDir );
		//this.setAcceptAllFileFilterUsed( false );
	}
	
	
	public int showDialog()
	{
		int decision;
		
		if ( dialogType == ChooserType.OPEN_DIALOG )
		{
			this.setDialogTitle( "Select a csv file to open" );
			decision = this.showOpenDialog( parentFrame );
		}
		else // ( dialogType == ChooserType.SAVE_DIALOG )
		{
			this.setDialogTitle( "Save as: Type a file name or select an existing csv file to overwrite" );
			decision = this.showSaveDialog( parentFrame );
		}
		
		return decision;
	}
	
	
	public void approveSelection( )
	{
		
		File selFile = getSelectedFile( );
		String path  = selFile.getAbsolutePath().toLowerCase();
	      
	    
		if ( !path.endsWith("csv") ) 
	    {
			JOptionPane.showMessageDialog( this, "Only files with the extension csv can be used in this program", 
					                       "Error:", JOptionPane.ERROR_MESSAGE );
			return;
	    }
		
		
		if ( dialogType == ChooserType.SAVE_DIALOG )
		{
			
			if( selFile != null && selFile.exists() )
			{
				// Ask the user if they are sure they want to overwrite the
				// existing file
				int response = JOptionPane.showConfirmDialog( this, 
				"The file " + selFile.getName() + " already exists. Do you want to replace the existing file?", "Notify:", 
				JOptionPane.YES_NO_OPTION ); 
				
				if ( response != JOptionPane.YES_OPTION ) 
				{ 
					return;
				}
			}
		}
		
		super.approveSelection();
	}
	
}


