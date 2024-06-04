from io import BytesIO
import requests

import pandas as pd 


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader



@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:

    url = 'https://drive.google.com/file/d/12iR5YoUIwpDTRmFOadNeAWr4h87S387u/view?usp=sharing'
    response = requests.get(url)
    print(">>>>>>>>")
    print(type(response.content))
    if response.status_code != 200:
        raise Exception(response.text)
    
    df = pd.read_parquet(BytesIO(response.content))

    return df
