import pytest
import pandas as pd
import numpy as np
from src.data.load_data import load_raw_data

def test_load_raw_data(tmp_path):
    # Create a dummy csv
    d = tmp_path / "data"
    d.mkdir()
    p = d / "test.csv"
    p.write_text("a,b,c\n1,2,3")
    
    df = load_raw_data(str(p))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 3)
