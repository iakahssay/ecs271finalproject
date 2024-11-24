import pandas as pd
import sys
from os import path
from nltk.tokenize import word_tokenize
from nltk import download
from tqdm import tqdm


rawData = pd.read_csv('smaller_dataset.csv',usecols=['title','NER','directions'],nrows=1000)
# print(rawData.dtypes)
# print(rawData.columns)
# print(rawData.iloc[0])
# print(rawData['directions'][0])

colnames = ['title', 'ingredients', 'instructions', 'separator']
colnames2 = ['title', 'ingredients', 'separator1', 'instructions', 'separator2']

#Originally Parsed Dataset 
df = pd.DataFrame(columns=colnames)
df['title'] = rawData['title']
df['ingredients'] = rawData['NER']
df['instructions'] = rawData['directions']
df['separator'] = '</>separator</>'

#Parsed Dataset with Seperator between Ingredient List and Instruction List
df2 = pd.DataFrame(columns=colnames2)
df2['title'] = rawData['title']
df2['ingredients'] = rawData['NER']
df2['separator1'] = '</>separator</>'
df2['instructions'] = rawData['directions']
df2['separator2'] = '</>separator</>'

print("Columns: \n", df.columns)
print("\n Iloc: \n", df.iloc[0])
print("\nTitle: \n", df['title'][0])
print("\nIngredients[0]: \n", df['ingredients'][0])
print("\nInstructions[0]: \n", df['instructions'][0])
print("\nSeperator[0]: \n", df['separator'][0])
print("\nShape: \n", df.shape)

df.to_csv('df_tokenized_with_separator.txt', header = None, sep=' ',index=False,quotechar="'")
df2.to_csv('df_tokenized_with_2_separators.txt', header = None, sep=' ',index=False,quotechar="'")