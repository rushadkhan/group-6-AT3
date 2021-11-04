import unittest
import streamlit as st
import pandas as pd
import sys

sys.path.append('D:\Assignment\src')
from text import TextColumn

class TextTest(unittest.TestCase):

    @classmethod
    def startclass(self):
        inputdata = pd.Series(['ABC', 'DEF', 'Ab', 'cd', 'abc', '123', None, 'ef', 'ABC', " "])
        column_name = "Data"
        self.text = TextColumn(column_name, inputdata)

    @classmethod
    def endclass(cls):
        print("end class")

    def test_name(self):
        self.text.get_name()
        self.assertEqual(self.text.name, "Data")

    def test_unique(self):
        self.text.get_unique()
        self.assertEqual(self.text.unique, '7')

    def test_missing(self):
        self.text.get_missing()
        self.assertEqual(self.text.missing, '1')

    def test_empty(self):
        self.text.get_empty()
        self.assertEqual(self.text.empty, '1')

    def test_whitespace(self):
        self.text.get_whitespace()
        self.assertEqual(self.text.white, '1')

    def test_lowercase(self):
        self.text.get_lowercase()
        self.assertEqual(self.text.lower, '3')

    def test_uppercase(self):
        self.text.get_uppercase()
        self.assertEqual(self.text.upper, '3')

    def test_alpha(self):
        self.text.get_alphabet()
        self.assertEqual(self.text.alpha, '8')

    def test_digit(self):
        self.text.get_digit()
        self.assertEqual(self.text.digit, '1')

    def test_mode(self):
        self.text.get_mode()
        self.assertEqual(self.text.mode, 'ABC')

    def test_barchart(self):
        inputdata = pd.Series(['ABC', 'DEF', 'Ab', 'cd', 'abc', '123', None, 'ef', 'ABC', " "])
        testchart = st.bar_chart(inputdata.value_counts())
        self.text.get_barchart()
        self.assertEqual(self.text.barchart, testchart)

    def test_frequent(self):
        self.text.get_frequent()
        self.assertEqual(self.text.frequency['value'][0], 'ABC')

if __name__ == '__main__':
    unittest.main()
