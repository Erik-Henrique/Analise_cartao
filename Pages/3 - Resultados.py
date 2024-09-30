import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, precision_score, recall_score, roc_auc_score
from imblearn.over_sampling import SMOTE

def app():
#
  
  DATA_URL = (r"https://raw.githubusercontent.com/Erik-Henrique/Analise_cartao/main/Application_Data.csv")
  smote = SMOTE(random_state=0)

  df = pd.read_csv(DATA_URL)
  df.drop(['Applicant_ID','Owned_Work_Phone', 'Owned_Phone', 'Owned_Email'], axis=1, inplace=True)
  _ = pd.get_dummies(df[['Applicant_Gender','Education_Type']])
  df = pd.concat([df, _], axis=1)
    
  df.drop(['Applicant_Gender','Income_Type','Education_Type','Family_Status','Housing_Type','Job_Title','Total_Children','Applicant_Gender_F      '], axis=1, inplace=True)
    
  df.columns = ['possui_carro', 'possui_casa', 'renda_anual', 'possui_celular',
                  'tamanho_familia', 'idade', 'anos_trabalho',
                  'num_mal_pagamento', 'num_bom_pagamento', 'Status','homem',
                  'pos_graduacao','graduado','educacao_incompleta','primario','secundario']
    
  df.homem = df.homem.map({True:1, False:0})
  df.pos_graduacao = df.pos_graduacao.map({True:1, False:0})
  df.graduado = df.graduado.map({True:1, False:0})
  df.educacao_incompleta = df.educacao_incompleta.map({True:1, False:0})
  df.primario = df.primario.map({True:1, False:0})
  df.secundario = df.secundario.map({True:1, False:0})

  X = df.drop('Status', axis=1)
  y = df['Status']
  X, y = smote.fit_resample(X, y)
  df = pd.concat([X, y], axis=1)

  X_treino, X_teste, y_treino, y_teste = train_test_split(df.drop('Status', axis=1), df['Status'], test_size=0.3, random_state=0)
  reg = LogisticRegression(random_state=0)
  reg.fit(X_treino, y_treino)
  r_treino = reg.score(X_treino,y_treino)
  r_teste = reg.score(X_teste,y_teste)
  f1 = f1_score(y_teste, reg.predict(X_teste))
  precisao = precision_score(y_teste, reg.predict(X_teste))
  recall = recall_score(y_teste, reg.predict(X_teste))
  roc =  roc_auc_score(y_teste, reg.predict(X_teste))
  st.write('''## Aqui temos o resultado do nosso modelo de Regressão Logística.''')
  
  
  st.markdown(f'''
                    | Resultado | Base |
                    |---|---|    
                    | {r_teste} | R-quadrado na base de Teste |
                    | {f1} | F-1 Score na base de Teste |
                    | {precisao} | Precisão Score na base de Teste |
                    | {recall} | Recall Score na base de Teste |
                    | {roc} | Curva ROC na base de Teste |
                    ''')
