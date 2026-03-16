import pytest
import pandas as pd
from src.features.build_features import build_features

def test_build_features():
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    df_out = build_features(df)
    assert isinstance(df_out, pd.DataFrame)
    assert df_out.shape == df.shape
