import streamlit as st
import importlib
import config 

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Início", "Análises gráficas", "Resultados", "Formulário"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "Pages.1- Início",
  "Visualizar os dados": "Pages.2- Análises gráficas",
  "Mapa de nascimentos": "Pages.3- Resultados",
  "Análises gráficas": "Pages.4- Formulário"
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()
