import pandas as pd
from sklearn.datasets import load_iris

def load_sample_data():
    iris = load_iris(as_frame=True)
    df = iris.frame
    return df