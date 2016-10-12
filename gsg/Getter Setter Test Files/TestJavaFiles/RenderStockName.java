package hirondelle.stocks.table;

import javax.swing.table.*;
import hirondelle.stocks.quotes.Stock;
import hirondelle.stocks.util.Util;

/**
* Display a {@link Stock} in a table cell by placing the
* full name in the cell, and by providing its Yahoo ticker 
* (including suffix for the {@link hirondelle.stocks.quotes.Exchange}) as tooltip.
*/
final class RenderStockName extends DefaultTableCellRenderer {
  
  public void setValue(Object aValue) {
    Object result = aValue;
    if ( (aValue != null) && (aValue instanceof Stock) ) {
      Stock stock = (Stock) aValue;
      result = stock.getName();
      StringBuilder tooltip = new StringBuilder("Yahoo Ticker: ");
      tooltip.append(stock.getTicker());
      String suffix = stock.getExchange().getTickerSuffix();
      if ( Util.textHasContent(suffix) ) {
        tooltip.append(".");
        tooltip.append(suffix);
      }
      setToolTipText( tooltip.toString() );
    } 
    super.setValue(result);
  }   
}