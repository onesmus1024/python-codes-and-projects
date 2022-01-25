import pandas as pd
import matplotlib.pyplot as plt


insurance_df = pd.read_csv('data/insurance.csv')
insurance_df=insurance_df.drop(labels='region',axis=1)
#one hot encoding for sex
insurance_df['sex_num']=insurance_df['sex'].replace({'male':1,'female':0})
#one hot encoding for smoker
insurance_df['smoker_num']=insurance_df['smoker'].replace({'yes':1,'no':0})
insurance_df=insurance_df.drop(labels=['sex','smoker'],axis=1)
print(insurance_df.head())
print(insurance_df.dtypes)
print(insurance_df[insurance_df['sex_num'].isna()].count())
insurance_df.to_csv('data/cleanedinsurancedata.csv',index_label=False)