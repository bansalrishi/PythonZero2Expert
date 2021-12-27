# -*- coding: utf-8 -*-
from unittest import main, TestCase
import unittest
from mock import patch
from StockMarket import StockMarket

class TestStockMarket(object):
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
        #self.quantity = kwargs.get("quantity", 1)
        self.symbol = "GIN"
        self.price = 150
        #self.stock = StockMarketClass.StockMarket()
        
    def test_cal_dividend_yield(self, expected):
        """
        Test calculate value for Common stocks which use
        the last dividend.
        :param float expected:
        :return:
        """
        
        #print("Running calculate_dividend(%s, %s) for Common -> Expected: %s" % (self.symbol, self.price, expected))

        assert StockMarket.cal_dividend_yield(self.symbol, self.price) == expected
        
if __name__ == "__main__": 
    unitTest = TestStockMarket()
    unitTest.test_cal_dividend_yield(0.08666666666666667)