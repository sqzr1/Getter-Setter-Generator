"""
 *Stock Data Builder*
   Algorithm:
      - Search website for stock
      - Get website HTML source code
      - Search code for target stock data(price,dividends,etc..)
      - Add data to SQLite 3 Database
"""

import sys
import os
import sqlite3
import datetime
import time
import urllib2

### Global Variables ###
MENU = "***Stock Program*** \n\n1. Add a Stock to track \n2. Get Todays Tracking Data \n3. Exit \nEnter decision: "
TARGET = '<th scope="row" class="row"><a href="/asx/research/companyInfo.do?by=asxCode&asxCode=%s">%s</a>'
ASX_URL = 'http://www.asx.com.au/asx/markets/priceLookup.do?by=asxCodes&asxCodes='

class Stock:
    code             = ""
    purchasePrice    = 0
    purchaseQuantity = 0
    price            = []  # list of recent prices
    recentBid        = []  # list of recent bids for Stock
    recentOffer      = []  # list of recent offers for Stock
    stockVol         = []  # list of stock quantity available on market
    def __init__(self):
        """ Default Constructor """
        self.code             = ""
        self.purchasePrice    = 0
        self.purchaseQuantity = 0
        self.price            = []
        self.recentBid        = []
        self.recentOffer      = []
        self.stockVol         = []
        
    def constructor(self, stockCode, purPrice, purQuant):
        """ Constructor """
        self.code             = stockCode
        self.purchasePrice    = purPrice
        self.purchaseQuantity = purQuant

    def setData(self, stockCode, purPrice, purQuant, priceList, reBidList, reOffList, popList):
        """ Defines & implements the objects' public variables """
        self.code             = stockCode     
        self.purchasePrice    = purPrice
        self.purchaseQuantity = purQuant
        self.price            = priceList
        self.recentBid        = reBidList
        self.recentOffer      = reOffList
        self.stockVol         = popList

        self.printStats()

    def updateData(self, priceEle, bidEle, offerEle, populEle):
        """ Adds data to stock object's lists """
        self.price.append(priceEle)
        self.recentBid.append(bidEle)
        self.recentOffer.append(offerEle)
        self.stockVol.append(populEle)

    def printStats(self):
        """ Output Stock attributes """
        
        print "Stock Code: "+self.code
        print "Stock Purchase Price: "+str(self.purchasePrice)
        print "Stock Quantity Owned: "+str(self.purchaseQuantity)
        print "***Initial Investment Value: "+str(self.purchasePrice*self.purchaseQuantity)
        if self.price:
            print "Stock Current Price: "+str(self.price[-1])
            print "Recent Bid: "+str(self.recentBid[-1])
            print "Recent Offer: "+str(self.recentOffer[-1])
            print "Total Stock Volume in market: "+str(self.stockVol[-1])
            print "***Present Investment Value: "+str(self.price[-1]*self.purchaseQuantity)       
        print "\n" 


### Functions ###
def connectDatabase(dbLocation, dbName, tableName):
    """ Establish & Return connection to SQLite Database """

    try:
        if not os.path.exists(dbLocation):
            os.mkdir(dbLocation) # create folder/dir

        os.chdir(dbLocation)        # change directory focus to dbLocation
        conn = sqlite3.connect(dbLocation+dbName)
        cur = conn.cursor()
        try:
            createTableQ = "CREATE TABLE IF NOT EXISTS "+tableName+" (code varchar PRIMARY KEY, purchase_price float, purchase_quantity float, purchase_date varchar);"
            cur.execute(createTableQ)
            conn.commit()
        except IOError:
            print "Failed to determine if table "+tableName+" exists."
            pass
        return conn
    except (IOError, OSError):
        print "Connection to database failed"
        return None

def retrieveStockDatabase(conn, tableName):
    """ Read SQLite3 database & extract stock data into StockList """

    stockList  = []
    stockQuery = "select recent_price, recent_offer, recent_bid, stock_volume from "
    cur = conn.cursor()
    cur.execute("select code, purchase_price, purchase_quantity from "+tableName+";")

    for row in cur.fetchall():
        newStock = Stock()
        newStock.code             = row[0]
        newStock.purchasePrice    = row[1]
        newStock.purchaseQuantity = row[2]
        cur.execute(stockQuery+row[0]+";")
        for rw in cur.fetchall():
            newStock.price.append(rw[0])
            newStock.recentOffer.append(rw[1])
            newStock.recentBid.append(rw[2])
            newStock.stockVol.append(rw[3])
        stockList.append(newStock)

    return stockList
    
def getDate():
    """ Return todays date in format DD:MM:YYYY """
    time = datetime.datetime.now()
    date = time.strftime("%d:%m:%Y") # string format time (%y)
    return date

def getHour():
    """ Return todays time(Hour only) in 24hr format """
    time = datetime.datetime.now()
    hour = time.hour
    return hour

def isListed(stock_code):
    """ Returns true if stock_code represents a listed stock on
    ASX website """
    try:
        sourceBuffer  = urllib2.urlopen(ASX_URL+stock_code)
        responde_code = sourceBuffer.code
        error_line    = '<p class="error">Sorry, no prices were retrieved at this time.</p>'
        if not error_line in sourceBuffer.read():
           return True
        else: return False
    except IOError:
        return False
    

def newStockDatabase(conn, stockTable, stock):
    """ Add a new stock to SQLite database if not already there
        We save the stocks code, purchase price, quantity purchased
        & date of purchase.                                       """
    cur = conn.cursor()
    try:
        createTableQ = "CREATE TABLE IF NOT EXISTS "+stock.code+" (date varchar, hour integer, recent_price float, recent_offer float, recent_bid float, stock_volume double);"
        stockQuery   = "INSERT INTO "+stockTable+" values(?, ?, ?, ?);"
        cur.execute(createTableQ)
        cur.execute(stockQuery,[stock.code,stock.purchasePrice,stock.purchaseQuantity,getDate()])
        conn.commit()
    except (sqlite3.OperationalError, msg):
        print "Table &/or column names may already exist or bad SQLite connection."
        return None

def webFormat(URL):

    if not URL.startswith("http://"):
        URL = "http://"+URL

    return URL

def getSource(URL):
    """ Retrieve HTML source code from website URL &
        save in sourceBuffer                       """

    try:
        URL = webFormat(URL) # make sure URL contains essential "http://"
        sourceBuffer = urllib2.urlopen(URL)
        #print '\nResponse code = ',sourceBuffer.code
        #print 'Response headers = ',sourceBuffer.info()
        #print 'Actual URL = ',sourceBuffer.geturl()
        sourceCode = sourceBuffer.read()
        sourceBuffer.close()
        return sourceCode

    except IOError:  # URLError
        print "Function Failed: Reasons could be invalid URL name \nOR \nHTML protocol message transfer failure."
        return None # function failed

def getTargetText(targetStrtData, targetEndData, dataBuffer):
    """ Grabs target text that lies inside 'dataBuffer' string
        between targetStrtData & targetEndData                """

    try:
        result = dataBuffer.split(targetStrtData)
        result.pop(0)
        result = result[0].split(targetEndData)
        result.pop(1)
        return result
    except IOError:
        print "Function Failed: Reasons could be targetStrtData and/or targetEndData is not present in dataBuffer."
        return None

def getStockData(htmlText, selectedStock):
    """ Extract stock data(stock code,price,etc) from htmlText """
    try:
        # Here I extract my number data from HTML text
        tempList = []
        for string in htmlText:
            for i in string.split('>'): 
                for e in i.split():
                        if '.' in e and e[0].isdigit():
                            tempList.append(float(e))
                        elif '-' in e and e[-1].isdigit():
                            tempList.append(float(e))
                        elif ',' in e and e[0].isdigit():
                            # remove ',' chars
                            e = e.replace(',','')
                            tempList.append(float(e))
                        elif e[0].isdigit():
                            tempList.append(float(e))

        selectedStock.updateData(tempList[0],tempList[2],tempList[3],tempList[-1])

    except IOError:
        print "Function Failed: Reasons could be: sites HTML data has changed. Consult author of program."
        return None

def createStockTracker(stockCode,stockPrice,stockQuant, stockList):
    """ Add a new stock to the database to track """
    newStock = Stock()
    newStock.constructor(stockCode,stockPrice,stockQuant)
    stockList.append(newStock)
    return stockList

def writeStockToDatabase(conn, stock):
    """ Write ONLY this Stock's attributes to SQLite Database """

    cur = conn.cursor()
    date = getDate()
    hour = getHour()

    tableName = stock.code
    stockquery = "insert into "+tableName+" values(?, ?, ?, ?, ?, ?);"
    cur.execute(query,[date,hour,stock.price[-1], stock.recentOffer[-1], stock.recentBid[-1], stock.stockVol[-1]])
    conn.commit()

def writeAllToDatabase(conn, stockList):
    """ Enter recent Stock attributes into SQLite Database """

    cur = conn.cursor()
    date = getDate()
    hour = getHour()

    for stock in stockList:
        tableName = stock.code
        stockQuery = "insert into "+tableName+" values(?, ?, ?, ?, ?, ?);"
        cur.execute(stockQuery,[date,hour,stock.price[-1], stock.recentOffer[-1], stock.recentBid[-1], stock.stockVol[-1]])
        conn.commit()

### Input Functions ###
def inputNewStock():
    """ """
    badInput = True

    while badInput==True:
        try:
            print "*Please note only an Australian Securities Exchange(ASX) listed stock can be tracked in Version 1.0."
            code     = raw_input("Please enter the ASX code for the stock you wish to track: ")
            price    = float(input("Please enter the individual stock value for "+code+": "))
            quantity = float(input("Please enter the number/quantity of stocks purchased: "))
            # Check if stock is listed on ASX website
            if isListed(code.upper()):
                badInput = False
                
                break;
            else:
                print "\nError: There is no stock with the code: "+code+" listed on the ASX Stock Exchange. Please try again. \n"
                badInput = True
        except (SyntaxError, OverflowError, NameError):
            if raw_input("\n*** Incorrect input *** \nNote: ASX code cannot be more than 3 chars. Press 'x' to exit or anything else to try again: ")=='x':
                return False
        print "\n\n"
        badInput = True
        
    result_tuple = (code.upper(),price,quantity)
    return result_tuple

### Main program loop ###
def main():
    programEnd = False;
    dbLocation = os.path.realpath(os.path.dirname(sys.argv[0])) #os.path.dirname(sys.path[0])
    dbLocation = dbLocation+'\Python - StockTracker Database/'
    dbName = "stockData.db"                                     #os.path.join(dbLocation, "stockData.db") 
    stockTable = "stocks"

    conn = connectDatabase(dbLocation,dbName,stockTable)
    stockList = retrieveStockDatabase(conn,stockTable)

    for s in stockList:
        s.printStats()

    while not programEnd:
        
        decision = input(MENU) # Print Menu
       
        if decision==1:

            result = inputNewStock() # result = (stock_code,stock_price,stock_quantity)
            
            if result:
                stockList = createStockTracker(result[0],result[1],result[2],stockList)
                newStockDatabase(conn,stockTable,stockList[-1])
                print "\n** New Stock **"
                stockList[-1].printStats()
                print "The stock "+result[0]+" was successfully added to our database. \nNow every time the program runs it will automatically track this stock & obtain its stock attributes\n\n"
                # TO DO:
                # get new stock recent Data from internet etc.
                # add stock data to data base
        elif decision==2:
            if len(stockList)>0:
                for Stock in stockList:
                    print ""
                    URL = ASX_URL+Stock.code
                    sourceCode = getSource(URL)
                    targetData = getTargetText(TARGET %(Stock.code,Stock.code),"</tr>",sourceCode)
                    getStockData(targetData,Stock)
                    Stock.printStats()
                writeAllToDatabase(conn,stockList)
            else:
                print "You must first identify a stock to follow. \nPlease select option 1."
        elif decision==3:
            print "Thank you for using Stock Program. Goodbye.\n"
            programEnd = True # Exit program         

    conn.close()
    return # End program

if __name__ == "__main__":
    main()
