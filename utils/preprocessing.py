from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import pandas as pd


def preprocess_data(df):

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Fill missing values using mean
    imputer = SimpleImputer(strategy='mean')

    imputed_data = imputer.fit_transform(numeric_df)

    # Scale the data
    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(imputed_data)

    return scaled_data, numeric_df.columns