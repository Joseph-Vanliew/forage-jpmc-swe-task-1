import unittest
from client3 import get_data_point
from client3 import get_ratio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        # Arrange
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        # Act & Assert
        for quote in quotes:
            self.assertEqual(get_data_point(quote),
                             (quote['stock'],
                              quote['top_bid']['price'],
                              quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        # Arrange
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        # Act & Assert
        for quote in quotes:
            self.assertEqual(get_data_point(quote),
                             (quote['stock'],
                              quote['top_bid']['price'],
                              quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_priceBIsZero(self):
        # Arrange
        price_a = 32.5
        price_b = 0
        # Act & Assert
        self.assertEqual(get_ratio(price_a, price_b), None)

    def test_getRatio_priceBIsNegative(self):
        # Arrange
        price_a = 32.5
        price_b = -3
        # Act & Assert
        self.assertEqual(get_ratio(price_a, price_b), None)

    def test_getRatio_calculateRatio(self):
        # Arrange
        price_a = 32.5
        price_b = 30.3
        # Act & Assert
        self.assertEqual(get_ratio(price_a, price_b), 1.0726072607260726)



if __name__ == '__main__':
    unittest.main()
