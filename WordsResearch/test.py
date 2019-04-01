import numpy as np
import csv
import pandas as pd
from googletrans import Translator
# translator = Translator()
# df = pd.read_csv('flightdata.csv')
# df["language"] = df["language"].astype(str)
# df['translated_word'] = translator.translate('who', src="en", dest=df["language"].get(0)).text
# print(df)


data = pd.read_csv('flightdata.csv')
translator = Translator()
# Init empty dataframe with much rows as `data`
df = pd.DataFrame(index=range(0,len(data)))

def translate_row(row):
    ''' Translate elements A and B within `row`. '''
    a = translator.translate(row[4], dest='Fr')
    return pd.Series([a.text])


for i, row in enumerate(data.values):
    # Fill empty dataframe with given serie.
    df.loc[i] = translate_row(row)

print(df)