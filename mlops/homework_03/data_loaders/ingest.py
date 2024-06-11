from io import BytesIO
import requests

import pandas as pd 


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader



@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:

    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet'
    response = requests.get(url)
    print(type(response.content))
    if response.status_code != 200:
        raise Exception(response.text)
    
    df = pd.read_parquet(BytesIO(response.content))

    return df
