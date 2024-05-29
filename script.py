import requests
import pandas as pd
import os

def download(url,dataset='data_file.csv'):
    os.makedirs('data/raw', exist_ok=True)
    response=requests.get(url)
    file_path = os.path.join('data/raw', dataset)
    with open(file_path,'wb') as file:

        file.write(response.content)

def data_cleaned():
  
  datas=pd.read_csv('./data/raw/data_file.csv')
  os.makedirs('data/cleaned', exist_ok=True)
  # traitement des valeurs manquantes par la moyenne
  for i in datas.columns:
    p=datas[i].isnull().sum()
    if p!=0:
      if datas[i].dtype in [int, float]:
         datas[i].fillna(value=datas[i].mean(),inplace=True)
      else :
        mode_value = datas[i].mode()[0]
        datas[i].fillna(value=mode_value, inplace=True)
    # Traitement des valeurs dupliquées
    datas.drop_duplicates(inplace=True)
    datas.to_csv('./data/cleaned/data_cleaned.csv')
    return datas

