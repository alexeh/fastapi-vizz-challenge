from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np



def preprocess_data(filepath: str):
    # Read the CSV file
    data = pd.read_csv(filepath)
    # Drop unnecessary columns
    data = data.drop(columns=['Sector', 'Parent sector'])

    # Melt the dataframe to have a long format with 'year' and 'emissions' columns
    data = data.melt(id_vars=['Country'], var_name='year', value_name='emissions')

    # Convert the year column to integer
    data['year'] = data['year'].astype(int)


    # Split data into input features and output
    X = data[['Country', 'year']]
    y = data['emissions']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Create the encoder
    encoder = OneHotEncoder(handle_unknown='ignore')
    X_train_encoded = encoder.fit_transform(X_train[['Country']])
    X_test_encoded = encoder.transform(X_test[['Country']])

    # Combine the encoded 'Country' column with the 'year' column
    X_train_final = np.hstack([X_train_encoded.toarray(), X_train['year'].values.reshape(-1, 1)])
    X_test_final = np.hstack([X_test_encoded.toarray(), X_test['year'].values.reshape(-1, 1)])

    return X_train_final, y_train


