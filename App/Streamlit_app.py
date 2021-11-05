from data import Dataset
from numeric import NumericColumn
from text import TextColumn
import streamlit as st
import pandas as pd


st.title('Data Explorer Tool')
file = st.file_uploader("Upload file", type=['csv'])

#This if/else statement avoids an error appearing before the user uploads a file.
if not file:
    st.write('Please upload a CSV file to begin')
else:
    df = pd.read_csv(file)
    dataset = Dataset(name=file.name, df=df)
    
    #Overall Information
    st.header('1. Overall Information')
    st.write(f'**Name of Table:** {dataset.get_name()}')
    st.write(f'**Number of Rows:** {dataset.get_n_rows()}')
    st.write(f'**Number of Columns:** {dataset.get_n_cols()}')
    st.write(f'**Number of Duplicated Rows:** {dataset.get_n_duplicates()}')
    st.write(f'**Number of Rows with Missing Values:** {dataset.get_n_missing()}')
    st.write(f'**List of Columns:** {dataset.get_cols_list()}')
    st.write(f'**Type of Columns:**')
    st.table(pd.DataFrame.from_dict(dataset.get_cols_dtype(), orient='index', columns=['type']).astype(str))
    filter_rows = st.slider('Select the number of rows to be displayed', 1, 50, 5)
    st.write(f'**Top Rows of Table**')
    st.dataframe(dataset.get_head(n=filter_rows))
    st.write(f'**Bottom Rows of Table**')
    st.dataframe(dataset.get_tail(n=filter_rows))
    st.write(f'**Random Sample Rows of Table**')
    st.dataframe(dataset.get_sample(n=filter_rows))
    convert_date = st.multiselect('Which columns do you want to convert to dates', dataset.get_text_columns())
    for column in convert_date:
        dataset.df[column] = pd.to_datetime(dataset.df[column])
    
    #Numeric column section
    st.header('2. Numeric Column Information')
    for col in dataset.get_numeric_columns():
        num_col = NumericColumn(col_name=col, serie=dataset.df[col])
        st.subheader(f'2.{dataset.get_numeric_columns().index(col)} Field Name: **{num_col.col_name}**')
        st.table(pd.DataFrame.from_dict({'Number of Unique Values': num_col.get_unique(), 'Number of Rows with Missing Values': num_col.get_missing(), 'Number of Rows with 0': num_col.get_zeros(), 'Number of Rows with Negative Values': num_col.get_negatives(), 'Average Value': num_col.get_mean(), 'Standard Deviation Value': num_col.get_std(), 'Minimum Value': num_col.get_min(), 'Maximum Value': num_col.get_max(), 'Median Value': num_col.get_median()}, orient='index', columns=['value']))
        st.bar_chart(num_col.get_histogram())
        st.table(num_col.get_frequent())
    
    #Text column Information
    st.header('3. Text Column Information')
    for col in dataset.get_text_columns():
        text_col = TextColumn(col_name=col, serie=dataset.df[col])
        st.subheader(f'3.{dataset.get_text_columns().index(col)} Field Name: **{text_col.col_name}**')
        st.table(pd.DataFrame.from_dict({'Number of Unique Values': str(text_col.get_unique()), 'Number of Missing Values': str(text_col.get_missing()), 'Number of Rows with Empty Strings': str(text_col.get_empty()), 'Number of Rows with Whitespace': str(text_col.get_whitespace()), 'Number of Rows all Lowercase': str(text_col.get_lowercase()), 'Number of Rows all Uppercase': str(text_col.get_uppercase()), 'Number of Rows Alphabet Only': str(text_col.get_alphabet()), 'Number of Rows Digit Only': str(text_col.get_digit()), 'Mode': text_col.get_mode()}, orient='index', columns=['value']))
        st.bar_chart(text_col.get_barchart())
        st.table(text_col.get_frequent())
