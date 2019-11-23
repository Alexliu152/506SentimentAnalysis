import os, shutil
import pandas as pd
import numpy as np



def convert_to_unix_dates(df):
	df['date'] = pd.to_datetime(df['date'].str.replace('Updated ', ''), infer_datetime_format=True).astype(np.int64) // 10**9 + 18000

	return df


def remove_empty_articles(df):
	try:
		return df[df['body'].notnull()]
	except:
		return df[df['body_text'].notnull()]


def move_file(file):
	shutil.move('./Datasets/{}'.format(file), './Datasets/Raw/{}'.format(file))



for file in os.listdir('./Datasets/'):
    if file.endswith('.csv'):
    	print('Cleaning: ', file)

    	df = pd.read_csv(file)
    	df = remove_empty_articles(df)
    	df = convert_to_unix_dates(df)

    	df.to_csv('./Datasets/Cleaned/{}.csv'.format(file.split('.')[0]))
    	move_file(file)