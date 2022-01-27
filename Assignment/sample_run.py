# -*- coding: utf-8 -*-

from StockMarket import StockMarket
import logging
import sys
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-10.10s] [%(levelname)-6.6s]  %(message)s")
logger = logging.getLogger()
conHandler = logging.StreamHandler(sys.stdout)
conHandler.setFormatter(logFormatter)
logger.addHandler(conHandler)
logger.setLevel(logging.INFO)




if __name__ == "__main__":
    sMarket = StockMarket()
    
    #Calculate Dividend Yield
    stock1 = "JOE"
    stock2 = "ALE"
    stock3 = "GIN"
    divi_yield = sMarket.cal_dividend_yield(stock1, 150)
    logger.info("Dividend Yield for Stock {0} is {1}".format(stock1, divi_yield))

    #Calculate P/E Ratio
    pe_ratio = sMarket.cal_pe_ratio(stock1, 150)
    logger.info("P/E Ratio for Stock {0} is {1}".format(stock1, pe_ratio))
    
    #Add Trade Record
    status = sMarket.record_trade(stock1, 30, 30, "sell")
    logger.info("{0}: {1}".format(stock1, status))
    status = sMarket.record_trade(stock1, 20, 20, "buy")
    logger.info("{0}: {1}".format(stock1, status))
    status = sMarket.record_trade(stock2, 500, 100, "sell")
    logger.info("{0}: {1}".format(stock2, status))
    status = sMarket.record_trade(stock3, 100, 300, "sell")
    logger.info("{0}: {1}".format(stock3, status))
    
    logger.info("Trade Record: {0}".format(sMarket.show_trade_record()))
    
    #Calculate Volume Weighted Price
    vol_weighted = sMarket.cal_vol_weighted_price("JOE")
    logger.info("Volume Weighted Price for Stock {0} is {1}".format(stock1, vol_weighted))
    
    
    #Calculate Geometric Mean
    geo_mean = sMarket.cal_geometric_mean()
    logger.info("Geometric Mean is {0}".format(geo_mean))