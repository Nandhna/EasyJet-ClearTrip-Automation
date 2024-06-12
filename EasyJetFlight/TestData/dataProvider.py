import pytest
import pandas as pd


@pytest.fixture
def get_excel_data():
    df = pd.read_excel("..//ExcelData//test_data.xlsx",sheet_name='Sheet1')
    data = df.to_dict(orient='records')
    print(data)
    return data
