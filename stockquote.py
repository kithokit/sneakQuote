# stock quote application
# Author Kit Ho B


# a class which contains source information
# should I inherit from source class, if oncc 18 is used
import urllib2, urllib, simplejson as json
import time
class source:
    prefix="http://"
    domain="money18.on.cc/"
    state_daily="js/daily/quote/"
    state_real="js/real/quote/"
    state_daily_suffix="_d.js"
    state_real_suffix="_r.js"
    selector = "info/liveinfo_quote.html"
    HTTP_HEADER_REFERER = "Referer"
    
    def __init__(self, stockNo, state):
        #http://money18.on.cc/js/daily/quote/00082_d.js?t=1294559514989
        #http://money18.on.cc/js/real/opening/00082_o.js?t=1294589760951
        if state == "real":
            self.state=source.state_real
            self.suffix=source.state_real_suffix
        elif state == "daily":
            self.state=source.state_daily
            self.suffix=source.state_daily_suffix
        else:
            pass

        self.stockNo=self._modifyStockNo(stockNo)

    # private function
    # @param num , input stock quote
    # @return string with appended stock quote
    # Function: to append 0 for the stock quote
    # Remarks : max no. of digit = 5
    def _modifyStockNo(self,num):
        while len(num)<5:
            num = '0' + num
        return num
        
    def _getsourceURL(self):
        params = urllib.urlencode({'t':'1294639633955'})
        return self.prefix + self.domain + self.state + self.stockNo + \
               self.suffix + "?%s" %params

    def _getsourceReferer(self):
        return self.prefix + self.domain + self.selector

    def getHttpRequest(self):
        request = urllib2.Request(self._getsourceURL())
        request.add_header(self.HTTP_HEADER_REFERER, self._getsourceReferer())
        return request

# Stock object
class stock:
    def __init__(self):
        pass 

    def setPrice(self, price):
        self.price=price
    
    def setVolume(self, volume):
        self.volume=volume

    def setQuoteTime(self, time):
        self.quoteTime=time

    def setDayLow(self, dayLow):
        self.dayLow=dayLow

    def setDayHigh(self, dayHigh):
        self.dayHigh=dayHigh

    def getPrice(self):
        return self.price
    
    def getVolume(self):
        return self.volume


# Class: httpConnector
import sys
class httpConnector:
    def __init__(self, request):
        self.httpRequest=request

    # return a httpResponse
    def retrieveDataFromSource(self):
        responseData = urllib2.urlopen(self.httpRequest)
        return httpResponse(responseData)
    
# Class: httpRespone
import yaml
class httpResponse:

    def __init__(self, data):
        self.data=data

    # return a stock object
    def parseData(self):
        dataSource = self.data
        dataSource = dataSource.read().strip().decode('big5')
        dataSource = dataSource.replace('\t', '')
        dataSource = dataSource.replace(':', ': ')
        print dataSource
        #temp = "{name: \"NEW CENTURY GP\"}"
        dStock = yaml.load(dataSource[dataSource.index("{"):dataSource.index("}")+1])
        #dStock = yaml.load(temp)
        print dStock
        stockObj = stock()
        stockObj.setPrice(dStock['ltp'])
        stockObj.setVolume(dStock['vol'])
        stockObj.setQuoteTime(dStock['ltt'])
        stockObj.setDayLow(dStock['dyl'])
        stockObj.setDayHigh(dStock['dyh'])
        return stockObj
        

if __name__ == "__main__":
    #b = source('82', "daily")
    #a = httpConnect(b)
    #print b.getsourceURL()
    #a.retrieveSource()
    # Get argument, get what it needs
    if (len(sys.argv) < 2):
        print "Usage: <StockNo> -d"
        sys.exit(0)
    else: 
        stockNo = sys.argv[1] 

    #on18httpRequest = source(str(stockNo), "real").getHttpRequest()
    on18httpRequest = source(str(stockNo), "daily").getHttpRequest()
    httpConnect = httpConnector(on18httpRequest)
    httpResponse= httpConnect.retrieveDataFromSource();
    stock = httpResponse.parseData()
    print stock.getPrice()
    print stock.getVolume()
