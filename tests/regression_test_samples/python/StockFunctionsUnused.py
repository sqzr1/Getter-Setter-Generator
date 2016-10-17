# Some Functions I made for Stock App that I am still attached to

def stockDatabase(textfile):
    """ Obtains a list stocks that we need to search site for
        their current values                                """
    try:
        tFile = open(textfile,'r')
        tempList = tFile.readlines()
        tFile.close()

        codeList = []
        stockList = []
        # Separate each word in tempList into codeList
        for string in tempList:
            codeList += string.split(" ")
        # Create stock obj for each code
        for code in codeList:
            newStock = stock(code,0,0)
            stockList.append(newStock)
        return stockList

    except IOError:
        print "Function Failure: Cause maybe "+textfile+" does not exist"

def getPreviousData(textFile, backupFile):
    """ Obtains Stock previous details from text file """

    try:
        # check if textFile exists & backupFile exists
        # if not create folder & file named database.txt & file named backupDatabase.txt
        tFile = open(textFile,'r')
        contents = tFile.readlines()
        BUFile = open(backupFile,'w')
        BUFile.writelines(contents) # Backup text by: copy database.txt contents into backupDatabase.txt file
        BUFile.close()
        tFile.close()

        code      = ""
        purPrice  = purQuant = 0
        stockList = priceList = recentBidList = recentOfferList = stockPopulList = []
        title     = ['[stock]','[code]','[purchasePrice]','[purchaseQuantity]','[price] ','[recentBid]','[recentOffer]','[stockPopul]']
        var       = [code,purPrice,purQuant,priceList,recentBidList,recentOfferList,stockPopulList]
        index     = 0
        
        for line in contents:
            tempList = line.split(' ')
            
            if (tempList[0]=='[stock]'):
                newStock = stock() # create new stock
                index = 0
            elif (tempList[0]=='[stockPopul]'):
                newStock.setData(code,purPrice,purQuant,priceList,recentBidList,recentOfferList,stockPopulList)
                stockList.append(newStock)
            elif (tempList[0]=='[code]'):
                code = tempList[1]
                print("code= "+tempList[1])
            elif (index > 0 and index < 3):
                var[index-1] = float(tempList[1])
                print("price|quant|= "+str(tempList[1]))
            elif (index >= 3 and index < 7):
                tempList.pop(0)
                if not(tempList): # check if list is empty
                    for ele in tempList:
                        var[index-1].append(float(ele))
            else:
                print "Function Failed: Database Textfile is not formatted correctly. \nConsult backup database text file."
                return False;
            index += 1
        return stockList
    except IOError:
        print "Function Failed: Reasons could be database.txt and/or backupDatabase.txt do not exists \nOR \nText file are not formated correctly"
        return False

def writeStockToFile(textFile, stockList):
    """ Writes stock data to text file """

    try:
        fileT = open(textFile,'w')
        
        for i in stockList:
            stockData = i.stockStats()
            fileT.write(stockData)
        fileT.close()
        return True;
    except IOError:
        print "Function Failed."
        return False

def stockStats(self):
        """ Returns a string containing stock objects'
            data(code,price,etc)                     """
        title = ['[price] ','[recentBid] ','[recentOffer] ','[stockPopul] ']
        lists = [self.price, self.recentBid, self.recentOffer, self.stockPopul]
        result = ""

        result += '[stock] \n'
        result += '[code] '+self.code+' \n'
        result += '[purchasePrice] '+str(self.purchasePrice)+' \n'
        result += '[purchaseQuantity] '+str(self.purchaseQuantity)

        for num in range(len(title)):
            result += '\n'+title[num]
            for x in lists[num]:
                 result += str(x)+' '

        result += '\n'
        return result
