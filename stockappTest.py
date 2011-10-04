import stockquote
import unittest

class StockQuoteTest(unittest.TestCase):
    def setUp(self):
        self.stockquote="5";
        self.realSource  =  stockquote.source(self.stockquote, "real")
        self.dailySource =  stockquote.source(self.stockquote, "daily")
        pass

    def test_source_modifyStockQuote_with_neg1(self):
        stockquote="-1";
        result = self.realSource._modifyStockNo(stockquote)
        print result
        self.assertEqual(result, "0000" + stockquote)

    def test_source_modifyStockQuote_with_0(self):
        stockquote="0";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result, "0000" + stockquote)

    def test_source_modifyStockQuote_with_5(self):
        stockquote="5";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result, "0000" + stockquote)

    def test_source_modifyStockQuote_with_18(self):
        stockquote="18";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result, "000" + stockquote)

    def test_source_modifyStockQuote_with_100(self):
        stockquote="100";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result, "00" + stockquote)

    def test_source_modifyStockQuote_with_2328(self):
        stockquote="2328";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result, "0" + stockquote)

    def test_source_modifyStockQuote_with_62259(self):
        stockquote="62259";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result,  stockquote)

    def test_source_modifyStockQuote_with_100000(self):
        stockquote="100000";
        result = self.realSource._modifyStockNo(stockquote)
        self.assertEqual(result,  stockquote)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(StockQuoteTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
