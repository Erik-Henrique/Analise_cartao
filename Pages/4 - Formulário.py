import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

st.set_page_config(layout='wide',
                   page_title='Banco X',
                   page_icon='https://png.pngtree.com/png-vector/20211030/ourmid/pngtree-letter-x-logo-png-image_3990472.png')


page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://www.shutterstock.com/shutterstock/photos/1684808446/display_1500/stock-vector-widescreen-abstract-financial-chart-with-uptrend-line-graph-and-candlestick-on-black-and-white-1684808446.jpg");
    background-size: cover;
    }
    [data-testid="stSidebarContent"] {
    background-image: url("https://scontent-gru1-1.xx.fbcdn.net/v/t39.30808-6/291779830_105699482202577_6654195867880689942_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeFmWDx72lVg_Xqax3nN15UAM7OA3lH5H_czs4DeUfkf93MF8MNtwes4i-94OtkabFUcBhgc2icdjFNl0_a83aOR&_nc_ohc=7LpSckNKdsoQ7kNvgF7eG5B&_nc_ht=scontent-gru1-1.xx&oh=00_AYB3PEuRb6OtaU79IjMzaFMdP4Ko3GJ7j2MvUiRfTsAElA&oe=66516BCB");
    background-size: cover;
    }
    [data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)
  

st.write('## Formulario para análise de liberação do cartão de crédito')


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

X_treino, X_teste, y_treino, y_teste = train_test_split(df.drop('Status', axis=1), df['Status'], test_size=0.3, random_state=0)
reg = LogisticRegression(random_state=0)
reg.fit(X_treino, y_treino)

carro = st.number_input("Possui carro?", value=None, placeholder="1 para sim, 0 para não")
casa = st.number_input("Possui casa?", value=None, placeholder="1 para sim, 0 para não")
salario = st.number_input("Salário anual", value=None, placeholder="Insira um número")
telefone = st.number_input("Possui telefone?", value=None, placeholder="1 para sim, 0 para não")
familia = st.number_input("Número de integrantes da família", value=None, placeholder="Insira um número")
idade = st.number_input("Idade", value=None, placeholder="Insira um número")
emprego = st.number_input("Tempo no atual emprego em anos", value=None, placeholder="Insira um número")
atraso = st.number_input("Pagamentos atrasados", value=None, placeholder="Insira um número")
em_dia = st.number_input("Pagamentos em dia", value=None, placeholder="Insira um número")
sexo = st.number_input("Sexo", value=None, placeholder="1 para masculino, 0 para feminino")
graduaçao = st.selectbox(
   "Escolaridade",
   ("Pós-graduação", "Graduação", "Educação incompleta", "Primário", "Secundário"),

   placeholder="Selecione sua escolaridade",
)


if graduaçao == "Pós-graduação":
    pos = 1
    graduado = 0
    incompleto = 0
    primario = 0 
    secundario = 0
elif graduaçao == "Graduação":
    pos = 0
    graduado = 1
    incompleto = 0
    primario = 0 
    secundario = 0
elif graduaçao == "Educação incompleta":
    pos = 0
    graduado = 0
    incompleto = 1
    primario = 0 
    secundario = 0
elif graduaçao == "Primário":
    pos = 0
    graduado = 0
    incompleto = 0
    primario = 1 
    secundario = 0
elif graduaçao == "Secundário":
    pos = 0
    graduado = 0
    incompleto = 0
    primario = 0 
    secundario = 1



dados = [[carro,casa,salario,telefone,familia,idade,emprego,atraso,em_dia,sexo,pos,graduado,incompleto,primario,secundario]]
novo = pd.DataFrame(dados, columns=['possui_carro','possui_casa','renda_anual','possui_celular','tamanho_familia','idade','anos_trabalho','num_mal_pagamento','num_bom_pagamento','homem','pos_graduacao','graduado','educacao_incompleta','primario','secundario'])
st.write(novo)



if novo.isna().sum().max() > 0:
    st.write('## Por favor, preencha todos os campos.')
elif st.button("Gerar análise") and novo.isna().sum().max() == 0:
    if reg.predict(novo) == 1:
        st.write('### O cliente foi aprovado para a liberação do cartão de crédito!')
    else:
        st.write('### O cliente não foi aprovado para a liberação do cartão de crédito!')
    st.button("Fazer nova análise", type="primary")
