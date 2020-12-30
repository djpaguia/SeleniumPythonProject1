import unittest                                          # unittest module or package is important and needs to be imported.
from Examples import Example


class MyTestCase(unittest.TestCase):                     # unittest.TestCase - TestCase class is called from the unittest package.
    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    @classmethod                                         # @classmethod - annotation used to define the class method
    def tearDownClass(cls):
        print("This will run once after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")

    def test_add(self):                                  # Always name your unit tests starting with the word, "test".
        self.assertEqual(Example.add(self, 10, 20), 30)
        self.assertEqual(Example.add(self, 0, 0), 0)
        self.assertEqual(Example.add(self, -1, 1), 0)

    def test_sub(self):
        result = Example.sub(self, 50, 30)
        self.assertEqual(result, 20)

    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
