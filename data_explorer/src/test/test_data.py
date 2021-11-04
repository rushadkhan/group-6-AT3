# To be filled by students
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

#Now establish it as a Dataset object
test_dataset = Dataset(name=test_name, df=test_df)

#Now we have our dummy object we can test each function on it

class TestGetName(unittest.TestCase):
    def test_function(self):
        name_test = test_dataset.get_name()
        self.assertEqual(name_test, 'test_name')
        
class TestGetNRows(unittest.TestCase):
    def test_function(self):
        nrow_test = test_dataset.get_n_rows()
        self.assertEqual(nrow_test, 11)
        
class TestNCols(unittest.TestCase):
    def test_function(self):
        ncol_test = test_dataset.get_n_cols()
        self.assertEqual(ncol_test, 3)
        
class TestGetColsList(unittest.TestCase):
    def test_function(self):
        test_cols = test_dataset.get_cols_list()
        self.assertEqual(test_cols, ['Date', 'Product', 'Value'])
        
class TestColsType(unittest.TestCase):
    def test_function(self):
        test_dtype = test_dataset.get_cols_dtype()
        self.assertEqual(test_dtype['Data Type'].tolist(), [dtype('<M8[ns]'), dtype('O'), dtype('float64')])
        
class TestNDups(unittest.TestCase):
    def test_function(self):
        test_dups = test_dataset.get_n_duplicates()
        self.assertEqual(test_dups, 1)
        
class TestNMissing(unittest.TestCase):
    def test_function(self):
        test_missing = test_dataset.get_n_missing()
        self.assertEqual(test_missing, 1)
        
class TestHead(unittest.TestCase):
    def test_function(self):
        test_head = test_dataset.get_head()
        self.assertEqual(test_head.shape[1], 5)
        
class TestTail(unittest.TestCase):
    def test_function(self):
        test_tail = test_dataset.get_tail()
        self.assertEqual(test_tail.shape[1], 5)
        
class TestSample(unittest.TestCase):
    def test_function(self):
        test_sample = test_dataset.get_sample()
        self.assertEqual(test_sample.shape[1], 5)
        
class TestNumCols(unittest.TestCase):
    def test_function(self):
        test_nums = test_dataset.get_numeric_columns()
        self.assertEqual(test_nums.count(), 1)
        
class TestTxtCols(unittest.TestCase):
    def test_function(self):
        test_txt = test_dataset.get_text_columns()
        self.assertEqual(test_txt.count(), 1)
        
class TestDateCols(unittest.TestCase):
    def test_function(self):
        test_date = test_dataset.get_date_columns()
        self.assertEqual(test_date.count(), 1)