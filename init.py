import streamlit as st
import importlib
import config 

# Configuração da barra lateral
selection = st.sidebar.radio("Páginas:", ["Início", "Análises gráficas", "Resultados", "Formulário"])

# Dicionário para mapear seleção para o nome do módulo
pages = {
  "Início": "Pages.1- Início",
  "Análises gráficas": "Pages.2 - Análises gráficas",
  "Resultados": "Pages.3 - Resultados",
  "Formulário": "Pages.4 - Formulário"
}

# Importar e renderizar a página selecionada
module = importlib.import_module(pages[selection])
module.app()
