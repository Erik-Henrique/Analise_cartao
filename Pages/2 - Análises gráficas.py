import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
#  
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
  
  st.markdown('## Aqui você pode ver algumas análises gráficas interessantes sobre a distribuição dos nossos dados:')
  
  seleção = st.selectbox(
        'Selecione a análise desejada:',
        ('TAMANHO DA FAMÍLIA x RENDA', 'NÚMERO DE MALS PAGAMENTOS x RENDA', 'SEXO x NÚMERO DE MALS PAGAMENTOS', 'TAMANHO DA FAMÍLIA x NÚMERO DE MALS PAGAMENTOS', 'ANOS TRABALHADOS NA MESMA EMPRESA x NÚMERO DE MALS PAGAMENTOS', 'NÚMERO DE BONS PAGAMENTOS x NÚMERO DE MALS PAGAMENTOS'), 
         index = None, placeholder= 'Clique aqui para selecionar a análise desejada')
  
  
  if seleção == 'TAMANHO DA FAMÍLIA x RENDA':
    col1, col2 = st.columns(2)
  
    with col1:
        sns.scatterplot(x='tamanho_familia', y='renda_anual', hue='Status', data=df)
        st.pyplot()
    
    with col2:
       st.write('### Análise')
       st.write('Aqui notamos uma diminuição da renda a medida que o número de integrantes da família aumenta, o que pode nos dizer que:')
       st.write('- As famílias com até dois integrantes provavelmente tem as maiores rendas pois sua composição seja em grande maioria parceiros que vivem juntos e ambos geram renda.')
       st.write('- As famílias com muitos integrantes (> 4) podem ter muitos membros que não gerem renda causando assim a diminuição da renda a medida que a família aumenta.')
  
  elif seleção == 'NÚMERO DE MALS PAGAMENTOS x RENDA':
    col1, col2 = st.columns(2)
  
    with col1:
        sns.scatterplot(x='num_mal_pagamento', y='renda_anual', hue='Status', data=df)
        st.pyplot()
    
    with col2:
       st.write('### Análise')
       st.write('- Clientes com maiores rendas tendem a ter menos ou nenhum registro de mau pagamento')
       st.write('- Aqui podemos ver uma relação clara entre a liberação do cartão de crédito com o número de mals pagamentos')
  
  elif seleção == 'SEXO x NÚMERO DE MALS PAGAMENTOS':
    col1, col2 = st.columns(2)
  
    with col1:
        sns.scatterplot(x='homem', y='num_mal_pagamento', hue='Status', data=df)
        st.pyplot()
    
    with col2:
       st.write('### Análise')
       st.write('Aqui notamos que não parece haver distinção entre homens e mulheres quanto a quantidade de maus pagamentos')
  
  elif seleção == 'TAMANHO DA FAMÍLIA x NÚMERO DE MALS PAGAMENTOS':
    col1, col2 = st.columns(2)
  
    with col1:
        sns.scatterplot(x='tamanho_familia', y='num_mal_pagamento', hue='Status', data=df)
        st.pyplot()
    
    with col2:
       st.write('### Análise')
       st.write('- Aqui vemos que apesar das famílias com menos de 4 integrantes terem as melhores rendas, as famílias com mais registros de serem maus pagadores estão nessa faixa.')
  
  elif seleção == 'ANOS TRABALHADOS NA MESMA EMPRESA x NÚMERO DE MALS PAGAMENTOS':
    col1, col2 = st.columns(2)
  
    with col1:
        sns.scatterplot(x='anos_trabalho', y='num_mal_pagamento', hue='Status', data=df)
        st.pyplot()
    
    with col2:
       st.write('### Análise')
       st.write('- Aqui vemos que pessoas recém empregadas tendem a ter mais propenção a serem maus pagadores.')
  
  elif seleção == 'NÚMERO DE BONS PAGAMENTOS x NÚMERO DE MALS PAGAMENTOS':
    col1, col2 = st.columns(2)
  
    with col1:
        sns.scatterplot(x='num_bom_pagamento', y='num_mal_pagamento', hue='Status', data=df)
        st.pyplot()
    
    with col2:
       st.write('### Análise')
       st.write('Aqui vemos uma clara divisão entre a liberação dos cartões ou nãos.')      
       st.write('- Quando o número de maus pagamentos é muito superior ao de bons pagamentos o cliente normalmente tem a liberação do cartão rejeitada.')   
       st.write('- Quando o número de maus pagamentos é maior ou igual ao número de bons pagamentos o cliente tem seu cartão recusado.')    
       st.write('- Em alguns casos apenas o fato do cliente ter mais pagamentos em dia já serve para que seu cartão seja liberado.')    
