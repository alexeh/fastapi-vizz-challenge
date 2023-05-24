import os

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def get_encoder():
    data = pd.read_csv(os.getcwd() + "/predictor/temp_files/emissions.csv")
    unique_countries = data['Country'].unique().tolist()
    encoder = OneHotEncoder(categories=[unique_countries], sparse=False)
    encoder.fit(np.array(unique_countries).reshape(-1, 1))
    return encoder
