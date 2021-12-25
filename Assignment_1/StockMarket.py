# -*- coding: utf-8 -*-
from datetime import datetime
import time

class StockMarket():
    __GBCE = { 'TEA': 
             {'type': "Common",
              'l_dividend': 0,
              'f_divident': None,
              'par_value': 100
              },
             'POP': 
             {'type': "Common",
              'l_dividend': 8,
              'f_divident': None,
              'par_value': 100
              },
             'ALE': 
             {'type': "Common",
              'l_dividend': 23,
              'f_divident': None,
              'par_value': 60
              },
             'GIN': 
             {'type': "Preferred",
              'l_dividend': 8,
              'f_divident': 2,
              'par_value': 100
              },
             'JOE': 
             {'type': "Common",
              'l_dividend': 13,
              'f_divident': None,
              'par_value': 250
              }
             }
    def __init__(self):
        self.__TRRECORD = {}

    def cal_dividend_yield(self, stock, price):
        """
        Function to Calculate Dividend Yield
        :param stock: Its the symbol of a stock
        :param price: Price of the Stock
        :return: Dividend Yield
        """
        if stock in self.__GBCE:
            record = self.__GBCE[stock]
            divYield = 0
            try:
                if record['type'] == "Common":
                    divYield = record['l_dividend'] / price
                else:
                    divYield = (record['f_dividend'] * record['par_value']) / price
                return divYield
            except ZeroDivisionError as Z:
                return ("Price can't be zero")
        else:
            raise Exception("Stock Symbol not Found")
            
    def cal_pe_ratio(self, stock, price):
        """
        Function to Calculate P/E Ratio
        :param stock: Its the symbol of a stock
        :param price: Price of the Stock
        :return: P/E Ratio if Stock exist in GBCE table
        """
        if stock in self.__GBCE:
            dividend = self.cal_dividend_yield(stock, price)
            peRatio = dividend / price
            return peRatio
        else:
            raise Exception("Stock Symbol not Found")
    
    def cal_vol_weighted_price(self, stock, timeslot = 5):
        """
        Function to Calculate Volume Weighted Stock Price
        :param stock: Its the symbol of a stock
        :param timeslot(default = 5 min): Consider trade in last x minutes
        :return: Volume Weighted Stock Price if Stock traded in last x minutes
                 else 0
        """        
        timenow = datetime.now().timestamp()
        total_quantity = 0
        summation_price_quantity = 0
        for key in self.__TRRECORD:
            delta = (timenow - key) / 60
            if delta < timeslot and self.__TRRECORD[key]['symbol'] == stock:
                summation_price_quantity += self.__TRRECORD[key]['price'] * self.__TRRECORD[key]['volume']
                total_quantity += self.__TRRECORD[key]['volume']
        if total_quantity == 0:
            return 0
        else:
            return summation_price_quantity / total_quantity
                
    def cal_geometric_mean(self):
        """
        Function to Calculate Geometric Mean
        :return: Geometric Mean if at least one Stock traded in last x minutes
                 else 1
        """
        geometric = 1
        no_of_stock = 0
        for key in self.__GBCE:
            p = self.cal_vol_weighted_price(key)
            if p != 0:
                geometric *= p
                no_of_stock += 1
        return pow(geometric, no_of_stock)
            
    
    def validate_mode(self, mode):
        """
        Function to Validate whether Mode is either of Buy or Sell
        :param mode: Mode of transaction in stock
        :return: True is mode is either buy or sell otherwise False
        """
        valid_mode = ['sell', 'buy']
        if mode.lower() in valid_mode:
            return True
        else:
            return False
                    
    def record_trade(self, stock, quantity, price, mode):
        """
        Function to Record Trade Details of Known Stock
        :param stock: Its the symbol of a stock
        :param quantity: How much quantity of stock is traded
        :param price: Price of the Stock
        :return:  
        """
        if stock in self.__GBCE and self.validate_mode(mode):
            timenow = datetime.now().timestamp()
            time.sleep(0.0001)
            self.__TRRECORD[timenow] = {
            'mode' : mode,
            'price': price,
            'volume': quantity,
            'symbol': stock
            }
            print("Stock Record added successfully")
        else:
            print("Not a Valid Stock: {0}".format(stock))

    def show_trade_record(self):
        """
        Function to print Record Trade Details
        :return: 
        """        
        print(self.__TRRECORD)
            
            
s = StockMarket()
print(s.cal_dividend_yield("JOE", 150))
print(s.cal_pe_ratio("JOE", 150))

s.record_trade("JOE", 30, 30, "sell")
s.record_trade("JOE", 20, 20, "buy")
s.record_trade("ALE", 500, 100, "sell")
s.record_trade("GIN", 100, 300, "sell")
s.show_trade_record()
print(s.cal_vol_weighted_price("JOE"))
print(s.cal_geometric_mean())
