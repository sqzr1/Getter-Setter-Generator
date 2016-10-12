# test create SQL database for stockprogram

import os
import sqlite3
import datetime
import time

### Global Variables ###
class stock:

    code = ""
    purPrice = 0
    purQuant = 0
    price    = []
    recOffer = []
    recBid   = []
    stockVol = []

### Functions ###
def connectDatabase(dbLocation, dbName, tableName):
    """ Establish & Return connection to SQLite Database """

    try:
        if not (os.path.exists(dbLocation)):
            os.mkdir(dbLocation) # create folder/dir

        os.chdir(dbLocation)        # change directory focus to dbLocation
        conn = sqlite3.connect(dbLocation+dbName)
        cur = conn.cursor()
        createTableQ = "create table "+tableName+" (code varchar PRIMARY KEY, purchase_price float, purchase_quantity float, purchase_date varchar);"
        cur.execute(createTableQ)
        conn.commit()
        return conn
    except IOError or OSError:
        print "Connection to database failed"
        return False

def getStockData(conn):
    """ Read SQLite3 database & extract stock data into StockList """

    stockList  = []
    stockQuery = "select recent_price, recent_offer, recent_bid, stock_volume from ? ;"
    cur = conn.cursor()
    cur.execute("select code, purchase_price, purchase_quantity from stocks;")

    for row in cur.fetchall():
        newStock = stock()
        newStock.code     = row[0]
        newStock.purPrice = row[1]
        newStock.purQuant = row[2]
        cur.execute(stockQuery,[newStock.code])
        for rw in cur.fetchall():
            newStock.price.append(rw[0])
            newStock.recOffer.append(rw[1])
            newStock.recBid.append(rw[2])
            newStock.stockVol.append(rw[3])
        stockList.append(newStock)

    return stockList
    
def getDate():
    """ Return todays date in format DD:MM:YYYY """
    time = datetime.datetime.now()
    date = time.strftime("%d:%m:%Y") # string format time (%y)
    return date

def newStockDatabase(conn, stockTable, stockStatsTable, stock):
    """ Add a new stock to SQLite database if not already there
        We save the stocks code, purchase price, quantity purchased
        & date of purchase.                                       """
    cur = conn.cursor()
    try:
        createTableQ = "create table "+stockStatsTable+" (date varchar PRIMARY KEY, recent_price float, recent_offer float, recent_bid float, stock_volume double);"
        stockQuery   = "insert into "+stockTable+" values(?, ?, ?, ?);"
        cur.execute(createTableQ)
        cur.execute(stockQuery,[stock.code,stock.purPrice,stock.purQuant,getDate()])
        conn.commit()
    except IOError or OSError:
        print "Table may already exist or bad SQLite connection."
        return False
    
def writeDatabase(conn, stockList):
    """ Enter recent Stock attributes into SQLite Database """

    cur = conn.cursor()
    date = getDate()

    for stock in stockList:
        tableName = stock.code
        stockquery = "insert into "+tableName+" values(?, ?, ?, ?, ?);"
        cur.execute(query,[date,stock.price[-1], stock.recOffer[-1], stock.recBid[-1], stock.stockVol[-1]])
        conn.commit()

### Main App ###
def main():
    """ Main Application Loop """

    dbLocation = "C:\Users\Sam\Desktop\StockApp/"
    dbName     = "stockData.db"

    print "doing..."
    conn = connectDatabase(dbLocation,dbName,"stock")
    print "done"

    return 0

main()
