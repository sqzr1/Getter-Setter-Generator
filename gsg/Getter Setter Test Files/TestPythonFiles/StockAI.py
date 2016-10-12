# Stock Trading AI

def sellForProfit(stock):
    """ If conditions are met then we return True to notify user
    to sell stock
    Conditions: if stock's current price has maintained a 10% PROFIT
                for the last 3 checkups: sell stock """

    criteria_met = True
    ten_profit = stock.purchasePrice*1.1
    x = -1
    
    if len(stock.price) < 3:
        stop_value = len(stock.price)*-1
    else:
        stop_value = -3
    
    while x>=stop_value:
        if stock.price[x] < ten_profit:
           criteria_met = False
        x -= 1

    return criteria_met

def sellToOffload(stock):
    """ Post: If conditions are met then we return True to notify user
              to sell stock
        Conditions: if stock's current price has maintained a 10% LOSS
              for the last 3 checkups: sell stock """

    ten_loss = stock.purchasePrice*0.9
    criteriaMet = True
    x = -1

    if len(stock.price) < 3:
        stop_value = len(stock.price)*-1
    else:
        stop_value = -3
    
    while x>=stop_value:
        if stock.price[x] >= ten_loss:
           criteria_met = False
        x -= 1

    return criteria_met

def setStopLimit(stock, limit):
    """ Pre: limit must be data type float 
        Post: Sets stocks limit to sell.  """

    if isinstance(limit,float):
        stock.stopLimit = limit
        return True
    else: return False

def isHighDemmand(stock):
    """ Post: Returns true if stock's market availability/volume
              is LOW, ie, stock is HIGH demmand """

    ten_ownership = stock.purQuantity*10
    volume_change = -5
    
    if stock.stockVol <= ten_ownership:
        return True
    elif len(stock.stockVol) > 10:
        if percentageChange(stock.stockVol[-1],stockVol[10]) <= volume_change:
            return True

    return False

def percentageChange(Ax, Bx):
    """ Returns the percentage change between floats Ax & Bx """
    change = ((Ax/Bx)*100)-100
    return change

if __name__ == "__main__":

    newStock = stock()
    sellForProfit(newStock)
    sellToOffload(newStock)
    SetStopLimit(newStock,2)
    isHighDemmand(stock)
