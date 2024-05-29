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
  
def remove_attributes():
    # Load the data using the download_data() function
   
    data=pd.read_csv('./data/cleaned/data_cleaned.csv',sep=";")
    # List of attributes that are not needed
    cols_to_remove = ['length', 'margin_up']

    # Loop through the columns to remove
    for col in cols_to_remove:
        # Drop the specified column from the DataFrame
        data.drop([col], axis=1, inplace=True)

    # Return the modified data after attribute removal
    return data

