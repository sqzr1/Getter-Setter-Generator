/*
   VCoder Project: WebScraping Google Searches for Search Data
   
   Description: I came across a project on VCoder.com of someone wanting a webscraper of google that 
                imports a set of search terms from a csv file, queries google with that search term,
                obtains the number of search results obtained & the time the search took & finally
                saving all the search result data to a csv file.
*/


import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Vector;



/**
 * 
 * Class: Model component of the MVC model. Performs the logical activities of the application
 *
 */
public class SearchModel
{
	/// Class Variables:
	
	private View                   appView;
	private Vector <SearchResult>  searchResults;
	private SearchEngine           engine;
	
	
	/// Class Methods:
	
	public SearchModel( View _appView )
	{
		
		appView        = _appView;
		searchResults  = new Vector <SearchResult>();
		engine         = new GoogleEngine();
		
		/*
		// Start Debugging
		String a[] = {"Pony", "Horse", "Manican"};
		for (int i=0; i<a.length; i++)
		{
			searchResults.add( new SearchResult( a[i] ) );
		}
		
		try 
		{
			File file = new File( "m.csv" );
			file.createNewFile();
			file.setWritable( true );
			writeCSVFile( file );
		} 
		catch (IOException e)
		{
			e.printStackTrace();
		}
		// End Debugging
		*/
		
	}
	
	
	/**
	 * Post: Use the internet to search the selected search engine for all search terms 
	 *       in the vector searchResults & obtain the search result quantity & time
	 *       it took to search for the search term
	 * 
	 */
	public void performActions()
	{
		
		/*
		if ( curFile == null )
		{
			appView.showErrorDialog( "Please define an input file" );
			return false;
		}
		*/
		
		SearchResultGatherer gatherer = new SearchResultGatherer( searchResults, engine, appView );
		searchResults                 = gatherer.getSearchResults();
		
	}
	
	
	/**
	 * Post: Toggle the selected search engine we use to obtain search result data
	 * 
	 * @param engineType  integer, if 1 we want to set yahoo as out search engine 
	 *                    else we want google
	 */
	public void setSearchEngine( int engineType )
	{
		switch ( engineType )
		{
			case 1:
			{
				engine = new YahooEngine();
			}
			break;
			default:
			{
				engine = new GoogleEngine();
			}
			break;
		}
	}
	
	
	/**
	 * Post: Read a CSV file to obtain a list of search terms (&/or search result data) to 
	 *       gather search result data for
	 *       
	 * @param inputFile  a CSV file containing a list of search terms(Strings)
	 * @return           return true if opening file & parsing was successful else false
	 * 
	 */
	public boolean readCSVFile( File inputFile )
	{
			
		try
		{
			searchResults.clear();
			
			BufferedReader infile = new BufferedReader( new FileReader( inputFile ) );
			StringTokenizer st    = null;
			String inline         = "";
			
			
			while ( (inline = infile.readLine()) != null )
			{
				st = new StringTokenizer( inline, "," );
				
				String searchTerm     = st.nextToken();
				double compData[]     = { -1, -1 };
				int index             = 0;

				while ( st.hasMoreTokens() && index < 2 )
				{
					
					try                   { compData[ index ] = Double.parseDouble( st.nextToken() ); }
					catch ( Exception e ) { compData[ index ] = -1; }
					
					index++;
				}
				
				searchResults.add( new SearchResult( searchTerm, (int) compData[0], (double) compData[1] ) );

			}
			
			
			sendSearchResults();
			
		}
		catch ( IOException e )
		{
			appView.showErrorDialog( "" + e.getMessage() );
			return false;
		}
		catch ( Exception e   )
		{
			appView.showErrorDialog( "" + e.getMessage() );
			return false;
		}
		
		
		return true;
		
	}
	
	
	/**
	 * Post: Write search result data to a CSV file. Data includes; search term, no. of search results 
	 *       & the time the search took
	 *       
	 * @param outputFile  a writtable CSV file to save our search result data to 
	 * @return            return true if file writting was successfule else false
	 */
	public boolean writeCSVFile( File outputFile )
	{
		
		try
		{
			@SuppressWarnings("unused")
			boolean fileExists = outputFile.createNewFile();
			
			if ( !outputFile.isFile()  ||  !outputFile.canWrite() )
			{
				appView.showErrorDialog( "Not a file or cant write it" );
				return false;
			}
			
			BufferedWriter outfile = new BufferedWriter( new FileWriter( outputFile.getAbsolutePath() ) );
			String outputStr       = "";
			
			for ( int i=0; i<searchResults.size(); i++ )
			{
				outputStr = searchResults.get(i).toString();
				outfile.append( outputStr );
				outfile.flush();
			}
			
		}
		catch ( IOException e )
		{
			appView.showErrorDialog( "" + e.getMessage() );
			return false;
		}
		catch ( Exception e   )
		{
			appView.showErrorDialog( "" + e.getMessage() );
			return false;
		}
		
		
		return true;
	}
	
	
	/**
	 * Post: Send search result data(in the form of 2d Object array [row][data]) to the 
	 *       View components' JTable so we can display it
	 * 
	 */
	public void sendSearchResults()
	{
		Object results[][] = new Object[ searchResults.size() ][3];
		
		for ( int i=0; i<searchResults.size(); i++ )
		{
			results[i] = searchResults.get(i).getTableElement();
		}
		
		appView.clearTable();
		appView.updateTableRow( results );
	}
	
}


/**
 * 
 * Class: Data-Store class used to store a search results data including the search term, 
 *        quantity of search results & the time it took for the search engine to perform
 *        the search
 *
 */
class SearchResult
{
	
	/// Class Variables:
	
	public String searchTerm;
	public double searchTime;
	public int    searchQuantity;
	
	
	/// Class Methods:
	
	public SearchResult( String _searchTerm )
	{
		searchTerm     = _searchTerm;
		searchTime     = -1;
		searchQuantity = -1;
	}
	
	public SearchResult( String _searchTerm, int _searchQuantity, double _searchTime )
	{
		searchTerm     = _searchTerm;
		searchTime     = _searchTime;
		searchQuantity = _searchQuantity;
	}
	
	public String toString()
	{
		return searchTerm + "," + searchQuantity + "," + searchTime + "\n";
	}
	
	/**
	 * Post: Format this objects search result data into an object array so we can 
	 *       simply add this search results data to a JTable component
	 * 
	 * @return return an Object array of size 3 containing the search term, quantity
	 *         & time the search engine took to perform the search
	 */
	public Object[] getTableElement()
	{
		Object result[] = { searchTerm, searchQuantity, searchTime };
		
		if ( searchQuantity <= -1 )
		{
			result[1] = "undefined";
		}
		
		if ( searchTime <= -1 )
		{
			result[2] = "undefined";
		}
		
		return result;
	}
	
}



