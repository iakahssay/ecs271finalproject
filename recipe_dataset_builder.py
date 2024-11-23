

import pandas as pd
import sys
from os import path
from nltk.tokenize import word_tokenize
from nltk import download
from tqdm import tqdm


rawData = pd.read_csv('RecipeNLG_dataset.csv',usecols=['title','NER','directions'],nrows=125000)
# print(rawData.dtypes)
# print(rawData.columns)
# print(rawData.iloc[0])
# print(rawData['directions'][0])

colnames = ['title', 'ingredients', 'instructions', 'separator']
df = pd.DataFrame(columns=colnames)
df['title'] = rawData['title']
df['ingredients'] = rawData['NER']
df['instructions'] = rawData['directions']
df['separator'] = '</>separator</>'

# print(df.columns)
print(df.iloc[3])
# print(df['title'][0])
# print(df['ingredients'][0])
print(df['instructions'][3])
# print(df['separator'][0])
print(df.shape)


df.to_csv('df_tokenized_with_separator.txt', header = None, sep=' ',index=False,quotechar="'")