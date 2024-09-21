import streamlit as st
import pandas as pd

def app():
#
  
  st.markdown(page_bg_img, unsafe_allow_html=True)
    
  st.write("# Bem vindo  👋")
    
  st.write('''#### Este é um Web App desenvolvido para análisar a liberação de um cartão de crédito para nossos clientes.''')
    
  DATA_URL = (r"https://raw.githubusercontent.com/Erik-Henrique/Analise_cartao/main/Application_Data.csv")
    # Adicionando o data frame a uma variável
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
  
  st.write('''## Esta é a base de dados dos nossos clientes, fique à vontade para explorar.''')
  st.write(' ')
    
    
    
  st.write(' ')
  st.write('### Para visualizar o Data Frame, basta indicar o indice inicial, final e as colunas:') 
  st.write(' ')
   
  col1, col2 = st.columns(2)
  
  with col1:
        st.markdown('''
                    | Variável | Significado |
                    |---|---|    
                    | possui_carro | Se o cliente possui carro - 1 = Sim  0 = Não |
                    | possui_casa | Se o cliente possui casa própria - 1 = Sim  0 = Não |
                    | renda_anual | Valor da renda anual |
                    | possui_celular | Se o cliente possui celular - 1 = Sim  0 = Não |
                    | tamanho_familia | Quantidade de integrantes da família do cliente |
                    | idade | Idade do cliente |
                    | anos_trabalho | Tempo de trabalho na empresa atual |
                    | num_mal_pagamento | Quantidade de vezes que o cliente pagou atrasado |
                    | num_bom_pagamento | Quantidade de vezes que o cliente pagou no prazo |
                    | Status | Se foi liberado o cartão ou não - 1 = Sim  0 = Não |
                    | homem | Se o cliente é do sexo masculino - 1 = Sim  0 = Não |
                    | pos_graduacao | Se o cliente possui pós graduação - 1 = Sim  0 = Não |
                    | graduado | Se o cliente possui graduação - 1 = Sim  0 = Não |
                    | educacao_incompleta | Se o cliente não concluiu os estudos - 1 = Sim  0 = Não |
                    | primario | Se o cliente terminou apenas o primario - 1 = Sim  0 = Não |
                    | secundario | Se o cliente terminou apenas o secundario - 1 = Sim  0 = Não |
                    ''')
  
  
  with col2:
      number1 = st.number_input('Indice inicial', value = 0)
      number2 = st.number_input('Indice final', value = 27027)
      colunas = st.multiselect('Seletor de colunas',default= 'Todas as variáveis',                   
                                                  options=['Todas as variáveis','possui_carro', 'possui_casa', 'renda_anual', 'possui_celular',
                                                           'tamanho_familia', 'idade', 'anos_trabalho',
                                                           'num_mal_pagamento', 'num_bom_pagamento', 'Status','homem',
                                                           'pos_graduacao','graduado','educacao_incompleta','primario','secundario'])
    
    
    
      if 'Todas as variáveis' not in colunas:
           if st.button('Visualizar o Data Frame'):
                  st.write(df[colunas][int(number1):int(number2)+1])
    
      if 'Todas as variáveis' in colunas:
           if st.button('Visualizar o Data Frame'):
                  st.write(df[int(number1):int(number2)+1])

