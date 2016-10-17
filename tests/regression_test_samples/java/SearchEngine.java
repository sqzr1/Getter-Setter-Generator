/*
   VCoder Project: WebScraping Google Searches for Search Data
   
   Description: I came across a project on VCoder.com of someone wanting a webscraper of google that 
                imports a set of search terms from a csv file, queries google with that search term,
                obtains the number of search results obtained & the time the search took & finally
                saving all the search result data to a csv file.
*/


/**
 * Class: An abstract class that will identify & store search result information 
 *        from when passed HTML tag information
 */
public abstract class SearchEngine
{
	
	/// Class Variables:
	
	protected enum SearchState { QUANT_SEARCH, TIME_SEARCH, NULL };
	protected SearchState searchState;
	public Object[][]     targetElementInfo;
	//public String         targetElement;
	//public String         targetID;
	public String         webAddress;
	protected double      searchTime;
	protected double      searchQuantity;
	
	
	/// Class Methods:
	
	public SearchEngine( String _webAddress, Object[][] _targetElementInfo ) // String _targetElement, String _targetID )
	{
		//targetElementInfo       = _targetElementInfo;
		//targetElement           = _targetElement;
		//targetID                = _targetID;
		searchState             = SearchState.QUANT_SEARCH;
		webAddress              = _webAddress;
		searchTime              = -1;
		searchQuantity          = -1;
	}
	
	
	abstract public boolean  saveSearchData( String[] HTMLTagData );
	
	
	/**
	 * Post: Return the search time & quantity relating to a search result
	 * 
	 * @return  return an array of type double containing search result data
	 */
	public double[] retrieveSearchData()
	{
        double searchData[] = { searchTime, searchQuantity };
        resetSearchData();
		
		return searchData;
	}
	
	
	/**
	 * Post: Reset search reset related variables when we have identified all 
	 * search result data so we can look at the next search term
	 * 
	 */
	public void resetSearchData()
	{
		searchState             = SearchState.QUANT_SEARCH;
		searchTime              = -1;
		searchQuantity          = -1;
	}
	
	
	/**
	 * Post: Convert a string of numerical text to a double
	 * 
	 * @param  numData  a string of numerical text
	 * @return          numData value converted to a double 
	 */
	public double convertToDecimal( String numData )
	{
		double result = 0;
		double c      = 1;
		
		// if ( Character.isDigit( numData[ numData.indexOf( "." ) -1 ] )  &&  Character.isDigit( numData[ numData.indexOf( "." ) +1 ] ) )
		if ( numData.contains( "." ) ) 
		{
			c /= Math.pow( 10, numData.length() - numData.indexOf( "." ) );
		}

		for (int i=numData.length()-1; i>=0; i--)
		{
			if ( Character.isDigit( numData.charAt(i) ) )
			{
				result += ((int)numData.charAt(i) - '0') * c;
				c      *=  10;
			}
		}
		System.out.println( "" + (float) result );
		
		return result;
	}
	
}



class GoogleEngine extends SearchEngine
{
	
	/// Class Methods:
	
	public GoogleEngine()
	{
		// http://www.google.com/search?q=%s
		super( "http://www.google.com/search?q=%s", null );
		
		searchState                  = SearchState.QUANT_SEARCH;
		this.targetElementInfo       = new Object[2][2]; 
		this.targetElementInfo[0][0] = "div";
		this.targetElementInfo[0][1] = "id=resultStats ";
		this.targetElementInfo[1][0] = " nobr";
		this.targetElementInfo[1][1] = "id=";
	}
	
	/**
	 * Post: Determine if HTMLTagData is a HTML tag we are looking for & if so, store the HTML 
	 *       tags text contents
	 * 
	 * @param HTMLTagData  array containing a HTML tags element type, text content & suplimentary
	 *                     data - such as id, class, href, etc.
	 * @return             return true if we identified & stored search result data else false
	 * 
	 */
	public boolean  saveSearchData( String[] HTMLTagData )
	{
		
		switch ( searchState )
		{
			case NULL:
			{
				return false;
			}
			case QUANT_SEARCH:
			{
				if ( HTMLTagData[0].equals( "div" )  &&  HTMLTagData[2].equals( "id=resultStats " ) )
				{
					System.out.println( "Quant text = " + HTMLTagData[1] );
					searchQuantity          = convertToDecimal( HTMLTagData[1] );
					searchState             = SearchState.TIME_SEARCH;
				}
			}
			break;
			case TIME_SEARCH:
			{
				// && HTMLTagData[2].startsWith( "(" )  &&  HTMLTagData[2].endsWith( ")" ) )
				if ( HTMLTagData[0].equals( "nobr" )  &&  HTMLTagData[2].equals( "undefined" ) )
				{
					System.out.println( "Time text = " + HTMLTagData[1] );
					searchTime              = convertToDecimal( HTMLTagData[1] );
					searchState             = SearchState.NULL;
				}
			}
			break;
			default:
			{
				return false;
			}
		}
		
		return true;
	}
	
}



class YahooEngine extends SearchEngine
{
	
	/// Class Methods:
	
	public YahooEngine()
	{
		super( "http://au.search.yahoo.com/search?p=%s&fr=yfp-t-501&ei=UTF-8", null );
		// super( "http://au.search.yahoo.com/search?p=%s&fr=yfp-t-501&ei=UTF-8", "strong", "id=resultCount " );
		
		searchState                  = SearchState.QUANT_SEARCH;
		this.targetElementInfo       = new Object[1][2]; 
		this.targetElementInfo[0][0] = "strong";
		this.targetElementInfo[0][1] = "id=resultCount ";
	}
	
	/**
	 * Post: Determine if HTMLTagData is a HTML tag we are looking for & if so, store the HTML 
	 *       tags text contents
	 * 
	 * @param HTMLTagData  array containing a HTML tags element type, text content & suplimentary
	 *                     data - such as id, class, href, etc.
	 * @return             return true if we identified & stored search result data else false
	 * 
	 */
	public boolean  saveSearchData( String[] HTMLTagData )
	{
		switch ( searchState )
		{
			case NULL:
			{
				return false;
			}
			case QUANT_SEARCH:
			{
				if ( HTMLTagData[0].equals( "strong" )  &&  HTMLTagData[2].equals( "id=resultCount " ) )
				{
					searchQuantity          = convertToDecimal( HTMLTagData[1] );
					searchState             = SearchState.NULL;
				}
			}
			break;
			default:
			{
				return false;
			}
		}
		
		return true;

	}
	
}

