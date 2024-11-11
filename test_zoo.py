import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_notbornticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-5), "Error")
       
    # Add your additional test cases here.

    def test_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_ticket21_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_Oldman_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    
    def test_Oldman2_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)


if __name__ == '__main__':
    unittest.main()