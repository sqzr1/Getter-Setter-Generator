/*
   VCoder Project: WebScraping Google Searches for Search Data
   
   Description: I came across a project on VCoder.com of someone wanting a webscraper of google that 
                imports a set of search terms from a csv file, queries google with that search term,
                obtains the number of search results obtained & the time the search took & finally
                saving all the search result data to a csv file.
*/

import java.awt.Dimension;
import java.io.File;


/**
 * Class: Controller component of the MVC model: Interprets user input & calls related model functions
 * 
 * @author Soribo
 *
 */
public class SearchController
{
	/// Class Variables:
	
	private View             appView;
	private SearchModel      appModel;
	public enum AppMessage { SR_READ_CSV_FILE, SR_GET_SEARCH_DATA, SR_SAVE_SEARCH_DATA, SR_CHANGE_ENGINE, SR_CLOSE };
	
	
	/// Class Methods:
	
	public SearchController()
	{
		appView  = new View( this, new Dimension(600, 400) );
		appModel = new SearchModel( appView );
	}
	
	
	/**
	 * Post: Main window proceedure that receives all user input as an ApplicationMessage, 
	 *       interprets message & calls related Model component functions
	 * 
	 * @param msg     enumeration message that relates to the GUI action/input that the user has performed
	 * @param wParam  extra information relating to the users action/input such as a file name, file, array etc.
	 * 
	 */
	public void windowProc( AppMessage msg, Object wParam )
	{
		
		switch ( msg )
		{
			case SR_READ_CSV_FILE:
			{
				appModel.readCSVFile( (File) wParam );
			}
			break;
			case SR_GET_SEARCH_DATA:
			{
				appModel.performActions();
			}
			break;
			case SR_SAVE_SEARCH_DATA:
			{
				appModel.writeCSVFile( (File) wParam );
			}
			break;
			case SR_CHANGE_ENGINE:
			{
				appModel.setSearchEngine( (Integer) wParam );
			}
			break;
			case SR_CLOSE:
			{
				System.exit(0);
			}
			break;
			default:	
			break;
		}
	}
	
	
	/// Main:

	/**
	 * Main Thread: Creates a SearchController object then ends
	 */
	public static void main( String[] args )
	{
		@SuppressWarnings("unused")
		SearchController control = new SearchController();
	}
	
}


