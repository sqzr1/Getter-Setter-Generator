# Test to gather Data for stocks

from stockDataRetrieval import *
from datetime import now
import time
import os
import sys

def main():
    """ """
    gameRun = True
    stockDataRetrieval.connect()
    stockDataRetrieval.initialise()

    while gameRun:

        # Get Stock stats on the hour
        time = stockDataRetrieval.getHour()
        if time == "17:00":
            gameRun = False
        elif time == 00:
            
        # This goes at bottom of while loop
        # Pause program for 59mins & 40sec
    

    stockDataRetrieval.closeConnection()

if __name__ == "__main__":
    main()


