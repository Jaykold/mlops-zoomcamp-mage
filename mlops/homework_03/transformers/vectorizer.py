import pandas as pd

#import the needed library for One-Hot Encoding and Linear Regression
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(df: pd.DataFrame, *args, **kwargs):

    #Change the model features to strings before One Hot encoding
    features = df[['PULocationID', 'DOLocationID']]
    features = features.astype(str)
    X = features.to_dict(orient='records')

    dv = DictVectorizer()
    dv.fit(X)

    X_train = dv.transform(X)
    y_train = df['duration'].values
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_train)

    print(model.intercept_)

    return dv, model