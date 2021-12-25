# -*- coding: utf-8 -*-
from datetime import datetime
from time import sleep

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
                print("Stock Price can't be zero")
        else:
            raise Exception("Stock Symbol not Found")
            
    def cal_pe_ratio(self, stock, price):
        if stock in self.__GBCE:
            dividend = self.cal_dividend_yield(stock, price)
            peRatio = dividend / price
            return peRatio
        else:
            raise Exception("Stock Symbol not Found")
    
    def cal_vol_weighted_price(self, stock, timeslot = 5):
        timenow = datetime.now().timestamp()
        total_quantity = 0
        summation_price_quantity = 0
        for key in self.__TRRECORD:
            delta = (timenow - key) / 60
            if delta < timeslot and self.__TRRECORD[key]['symbol'] == stock:
                summation_price_quantity += self.__TRRECORD[key]['price'] * self.__TRRECORD[key]['volume']
                total_quantity += self.__TRRECORD[key]['volume']
        if total_quantity == 0:
            return "No Trade in Stock: {0} in last {1} Minutes".format(stock, timeslot)
        else:
            return summation_price_quantity / total_quantity
                
    def cal_geometric_mean(self):
        geometric = 0
        no_of_stock = 0
        for key in self.__GBCE:
            pass
    
    def validate_mode(self, mode):
        valid_mode = ['sell', 'buy']
        if mode.lower() in valid_mode:
            return True
        else:
            return False
                    
    def record_trade(self, stock, quantity, price, mode):
        if stock in self.__GBCE and self.validate_mode(mode):
            timenow = datetime.now().timestamp()
            self.__TRRECORD[timenow] = {
            'mode' : mode,
            'price': price,
            'volume': quantity,
            'symbol': stock
            }
            sleep(0.05)
        else:
            print("Not a Valid Stock: {0}".format(stock))

    def show_trade_record(self):
        print(self.__TRRECORD)
            
            
s = StockMarket()
print(s.cal_dividend_yield("JOE", 150))
print(s.cal_pe_ratio("JOE", 150))

s.record_trade("JOE", 30, 30, "sell")
s.record_trade("JOE", 20, 20, "buy")
s.record_trade("ALE", 500, 100, "sell")
s.record_trade("GIN", 100, 300, "sell")
s.show_trade_record()
print(s.cal_vol_weighted_price("POP"))
