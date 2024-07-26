# -*- coding: utf-8 -*-
"""
Anthony Franklin

Jul 19th 2024
"""
class Stock:
    def __init__(self, symbol, name, shares):
      self.symbol = symbol
      self.name = name
      self.shares = shares
      self.DataList = [] #List of daily stock data
      
    def __str__(self):
        return f'{self.symbol}, {self.name}, {self.shares}'
    
    def __repr__(self):
        return f'{self.symbol}, {self.name}, {self.shares}'
    
    def add_data(self, stock_data):
        self.DataList.append(stock_data)
    
    # @property 
    # def symbol(self):
    #     return self._symbol
    
    # @symbol.setter
    # def symbol(self, symbol):
    #     raise RuntimeWarning("Cannot Change The Stock's Symbol")
    
    # @property
    # def name(self):
    #     return self._name
    # @name.setter
    # def name(self, name):
    #     self._name = name
    
    # @property
    # def shares(self):
    #     return self._shares
    # @shares.setter
    # def shares(self, shares):
    #     raise RuntimeWarning("Use buy() or sell() to change number of shares.")
    # def buy(self, amount):
    #     self._shares = self._shares + amount
    # def sell(self, amount):
    #     self._shares = self._shares - amount
        
    #Add price data
    def add_data(self, price_data):
        self.DataList.append(price_data)
        
class DailyData:
    def __init__(self, date, close, volume):
        self.date = date
        self.close = close
        self.volume = volume
    
    # @property 
    # def date(self):
    #     return self._date
    # @date.setter 
    # def date(self, date):
    #     self._date = date
    
    # @property 
    # def close(self):
    #     return self._close
    # @close.setter 
    # def close(self, close):
    #     self._close = close
        
    # @property 
    # def volume(self):
    #     return self._volume
    # @volume.setter 
    # def volume(self, volume):
    #         self._volume = volume
            
        
myStock = Stock("AAPL", "Apple", 3456)

# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.

def main():
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Stock
    print("Testing Add Stock...",end="")
    try:
        testStock = Stock("TEST","Test Company",100)
        print("Successful!")
    except:
        print("***Adding Stock Failed!")
        error_count = error_count+1
        error_list.append("Stock Constructor Error")
    # Test Change Symbol
    print("Test Change Symbol...",end="")
    try:
        testStock.symbol = "NEWTEST"
        if testStock.symbol == "NEWTEST":
            print("Successful!")
        else:
            print("***ERROR! Symbol change unsuccessful.")
            error_count = error_count+1
            error_list.append("Symbol Change Error")
    except:
        print("***ERROR! Symbol change failed.")
        error_count = error_count+1
        error_list.append("Symbol Change Failure")
    print("Test Change Name...",end="")
    try:
        testStock.name = "New Test Company"
        if testStock.name == "New Test Company":
            print("Successful!")
        else:
            print("***ERROR! Name change unsuccessful.")
            error_count = error_count+1
            error_list.append("Name Change Error")
    except:
        print("***ERROR! Name change failed.")
        error_count = error_count+1
        error_list.append("Name Change Failure")
        print("Test Change Name...",end="")
    try:
        testStock.shares = 2000
        if testStock.shares == 2000:
            print("Successful!")
        else:
            print("***ERROR! Shares change unsuccessful.")
            error_count = error_count+1
            error_list.append("Shares Change Error")
    except:
        print("***ERROR! Shares change failed.")
        error_count = error_count+1
        error_list.append("Shares Change Failure")
        

    # Test add daily data
    print("Creating daily stock data...",end="")
    daily_data_error = False
    try:
        dayData = DailyData("1/1/20",float(14.50),float(100000))
        testStock.add_data(dayData)
        if testStock.DataList[0].date != "1/1/20":
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Date")
        if testStock.DataList[0].close != 14.50:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Closing Price")
        if testStock.DataList[0].volume != 100000:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Volume")  
    except:
        print("***ERROR! Add daily data failed.")
        error_count = error_count + 1
        error_list.append("Add daily data Failure!")
        daily_data_error = True
    if daily_data_error == True:
        print("***ERROR! Creating daily data failed.")
    else:
        print("Successful!")
    
    if (error_count) == 0:
        print("Congratulations - All Tests Passed")
    else:
        print("-=== Problem List - Please Fix ===-")
        for em in error_list:
            print(em)
    print("Goodbye")

# Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    main()
