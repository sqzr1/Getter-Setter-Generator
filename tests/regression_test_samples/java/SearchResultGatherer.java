/*
   VCoder Project: WebScraping Google Searches for Search Data
   
   Description: I came across a project on VCoder.com of someone wanting a webscraper of google that 
                imports a set of search terms from a csv file, queries google with that search term,
                obtains the number of search results obtained & the time the search took & finally
                saving all the search result data to a csv file.
*/


import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.HttpURLConnection;
import java.util.Vector;
import javax.swing.text.MutableAttributeSet;
import javax.swing.text.html.HTML;
import javax.swing.text.html.HTMLEditorKit;
import javax.swing.text.html.parser.ParserDelegator;



/**
 * 
 * Class: An extension(specialisation) of the HTMLEditorKit.ParserCallback class.
 *        This class is designed to receive a list search terms & a SearchEngine
 *        object, obtain the search result data by querying the search engine
 *        over the internet, parse the result HTML source code for the search 
 *        result data (search result quantity & search time) & store said data
 *
 */
public class SearchResultGatherer extends HTMLEditorKit.ParserCallback implements Runnable
{

	/// Class Variables:
	
	int index = 0;
	
	private Vector <SearchResult> searchResults;
	private SearchEngine          searchEngine;
	private View                  appView;
	private HTMLTag               curHTMLTag;
	@SuppressWarnings("unused")
	private static final String   YAHOO_WEBADDRESS  = "http:/au.search.yahoo.com/search?p=%s&fr=yfp-t-501&ei=UTF-8";
	@SuppressWarnings("unused")
	private static final String   GOOGLE_WEBADDRESS = "http:/www.google.com.au/search?hl=en&source=hp&biw=&bih=&q=%s";
	
	
	/// Class Methods:
	
	public SearchResultGatherer( Vector <SearchResult> _searchResults, SearchEngine _searchEngine, View _appView )
	{
		searchResults     = _searchResults;
		searchEngine      = _searchEngine;
		appView           = _appView;
		curHTMLTag        = null;

		Thread thisThread = new Thread( this );
		thisThread.start();
		// Maybe do
		// thisThread.invokeAndWait();
	}
	
	
	/**
	 * Post: Override of the Thread class method Run(). Purpose is to
	 *       search the selected search engine for each search term inside
	 *       the vector searchResults & parse the returned HTML source code
	 *       for the search result data & store it
	 *       
	 */
	@Override
	public void run() 
	{
		// Maybe add
		// if ( !Thread.interrupted() )
		for ( int i=0; i<searchResults.size(); i++ )
		{
			String  searchQuery   = String.format( searchEngine.webAddress, searchResults.get(i).searchTerm );
			boolean searchSuccess = extractTimeAndQuantity( searchQuery );
			
			if ( searchSuccess )
			{
				//searchTime                        = Double.parseDouble( searchData[0].toString() );
				//searchQuantity                    = Integer.parseInt  ( searchData[1].toString() );
				double searchData[]                 = searchEngine.retrieveSearchData();
				searchResults.get(i).searchTime     = searchData[0];
				searchResults.get(i).searchQuantity = (int) searchData[1]; 
				Object newRows[][]                  = new Object[1][3];
				newRows[0]                          = searchResults.get(i).getTableElement();
				
				appView.updateTableRow( newRows );
			}
			else appView.showErrorDialog( "Failure retrieving & parsing google source code from internet" );
		}
		
	}
	
	
	/**
	 * Post: Return the search results we obtained when we searched 
	 *       the selected search engine for the search result data
	 * 
	 * @return  return a copy of the searchResults vector
	 * 
	 */
	@SuppressWarnings("unchecked")
	public Vector <SearchResult> getSearchResults()
	{
		return (Vector <SearchResult>) searchResults.clone();
	}
	
	
	/**
	 * Post: Open the selected search engines webpage containing a search term query,
	 *       then parse the returned HTML source code for the search result data
	 * 
	 * @param websiteAddress  the web address of the search engine with the search term 
	 *                        query attached
	 * @return                return true if HTML source code parsing was successful else
	 *                        return false
	 *                        
	 */
	public boolean extractTimeAndQuantity( String websiteAddress )
	{
		
		Reader r;
		Object sourceCode;

		try
	    {
			URL website           = new URL( websiteAddress );
			HttpURLConnection web = (HttpURLConnection) website.openConnection();
			web.setRequestProperty( "User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10" );
			
			synchronized ( this ) 
			{
				sourceCode = web.getContent();
				//System.out.println( sourceCode );
			}
			
            if ( sourceCode instanceof InputStream ) 
            {
                r          = new InputStreamReader( (InputStream) sourceCode );
            }
            else if ( sourceCode instanceof Reader ) 
            {
                r          = (Reader) sourceCode;
            }
            else 
            {
            	appView   .showErrorDialog( "Bad URL content type." );
            	return false;
            }
            
            HTMLEditorKit .Parser parser = new ParserDelegator();
            parser        .parse( r, this, true );
            System.out.println( "Finished parsing this page");
            
            r.close();
            
	    }
	    catch (MalformedURLException mue) 
	    {

	        // appView.showErrorDialog( "Error: MalformedURLException occurred" );
	        mue.printStackTrace();
	        return false;

	    } 
	    catch (IOException ioe) 
	    {

	    	// appView.showErrorDialog( "Error: IOException occurred" );
	        ioe.printStackTrace();
	        return false;
	    }
	    
	    
	    return true;
	}
	
	
	/**
	 * Post: Override the parent objects method for parsing a HTML element start tag.
	 *       Create a HTMLTag object & store its HTML element type & supplimentary 
	 *       data(id, class, href, etc.)
	 * 
	 * @param t    HTML tag element type (div, p, h1, a, etc.)
	 * @param a    HTML tag suplimentary data
	 * @param pos  
	 * 
	 */
	public void handleStartTag( HTML.Tag t, MutableAttributeSet a, int pos ) 
	{
		curHTMLTag = new HTMLTag( t, a );
    }
	
	
	/**
	 * Post: Override the parent objects method for parsing a HTML element text contents.
	 *       Store the current HTMLTag object's text contents
	 * 
	 * @param arg0  HTML tag elements' text contents ( <p> THIS TEXT </p>)
	 * @param arg1  HTML tag elements' text as an integer
	 * 
	 */
	public void handleText( char[] arg0, int arg1 )
	{
		curHTMLTag.setTagText( arg0 );
		// System.out.println( curHTMLTag.toString() );
		searchEngine.saveSearchData( curHTMLTag.getTagDetails() );
	}
	
}



/**
 * 
 * Class: An OO representation of a HTML tag/element. We store the HTML elements
 *        type, text content & suplimentary data (id, class, href, etc.)
 *
 */
class HTMLTag
{
	/// Class Variables:
	
	private String tagType;
	private String tagText;
	private String tagSuplData; // Tag Supplimentary Data
	
	
	/// Class Methods:
	
	public HTMLTag( HTML.Tag _tagType, MutableAttributeSet _tagSuplData )
	{
		tagType     = _tagType.toString();
		tagText     = "undefined";
		tagSuplData = _tagSuplData.toString();
		
		if ( tagSuplData.equals( "" ) )
		{
			tagSuplData = "undefined";
		}
	}
	
	/**
	 * Post: Set this HTML tags text contents (<p> THIS TEXT </p>)
	 * 
	 * @param _tagText  the new contents of this HTML tags text contents
	 * 
	 */
	public void setTagText( char[] _tagText )
	{
		tagText = new String( _tagText );
	}
	
	/**
	 * Post: Return this HTML tag objects' tag data so we can check if it is
	 *       a tag that the SearchEngine object is looking for, ie, is it the 
	 *       search quantity tag, the search time tag etc.
	 * 
	 * @return return a string array containing the HTML tag type, text &
	 *         supplimentary data
	 * 
	 */
	public String[] getTagDetails()
	{
		String tagDetails[] = { tagType, tagText, tagSuplData };
		
		return tagDetails;
	}
	
	public String toString()
	{
		return ( tagType + ", " + tagText + ", " + tagSuplData );
	}
	
}

