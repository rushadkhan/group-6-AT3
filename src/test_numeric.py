import unittest
import pandas as pd
import numpy as np
from data import Dataset

import unittest
import pandas as pd
import numpy as np
from data import Dataset

#Set up a dummy dataset
dates = pd.date_range('2021-10-15', periods=10, freq='D')
products = ['a','b','c','d','e','f','g','h', np.NaN, 'i']
vals = [1,2,3,4,5,6,7,8,9,10]
test_df = pd.DataFrame({'Date': dates, 'Product' : products, 'Value' : vals}) 
test_df = test_df.append({'Date':pd.to_datetime('2021-10-15'), 'Product': 'a', 'Value':1}, ignore_index=True)

#Establish the dummy dataset as Dataset object
test_dataset = Dataset(name=test_name, df=test_df)

#Test each function in the numeric.py file on the dummy Dataset

class TestGetName(unittest.TestCase):
    def test_function(self):
        name_test = test_dataset.get_name()
        self.assertEqual(name_test, 'test_name')

class TestGetUnique(unittest.TestCase):
    def test_function(self):
        unique_test = test_dataset.get_unique()
        self.assertEqual(unique_test, 10)

class TestGetMissing(unittest.TestCase):
    def test_function(self):
        missing_test = test_dataset.get_missing()
        self.assertEqual(missing_test, 0)

class TestGetZeroes(unittest.TestCase):
    def test_function(self):
        zeroes_test = test_dataset.get_zeroes()
        self.assertEqual(zeroes_test, 0)

class TestGetNegatives(unittest.TestCase):
    def test_function(self):
        negatives_test = test_dataset.get_negatives()
        self.assertEqual(negatives_test, 0)

class TestGetMean(unittest.TestCase):
    def test_function(self):
        mean_test = test_dataset.get_mean()
        self.assertEqual(mean_test, 5.5)

class TestGetStd(unittest.TestCase):
    def test_function(self):
        std_test = test_dataset.get_std()
        self.assertEqual(std_test, 3.03)

class TestGetMin(unittest.TestCase):
    def test_function(self):
        min_test = test_dataset.get_min()
        self.assertEqual(min_test, 1)

class TestGetMax(unittest.TestCase):
    def test_function(self):
        max_test = test_dataset.get_max()
        self.assertEqual(max_test, 10)

class TestGetMedian(unittest.TestCase):
    def test_function(self):
        median_test = test_dataset.get_median()
        self.assertEqual(median_test, 5.5)

class TestGetFrequent(unittest.TestCase):
    def test_function(self):
        frequent_test = frequent_dataset.get_frequent()
        self.assertEqual(frequent_test, 1,2,3,4,5,6,7,8,9,10)



