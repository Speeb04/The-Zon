import pandas as pd

INPUT_FILE_NAME = 'data/taxi_data.parquet'
OUTPUT_FILE_NAME = 'data/taxi_data.csv'

if __name__ == "__main__":
    data = pd.read_parquet(INPUT_FILE_NAME)
    data.to_csv(OUTPUT_FILE_NAME, index=False)
