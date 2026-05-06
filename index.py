import pandas as pd
import streamlit as st
import plotly.express as px
from services import filtro_anual, filtro_planos

df = pd.read_excel('base.xlsx', sheet_name=1)

st.set_page_config(page_title="Dashboard Assinaturas Xbox")
st.title('Dashboard - Amostra de Assinaturas Xbox Live')

st.header('Total de vendas de planos anuais com EA Pass e Minecraft Pass agregados')

col1, col2, col3 = st.columns(3)

col1.metric(label='Total Geral:',value= filtro_anual(df, 'Yes', 'Yes'),border=True)
col2.metric(label='Total apenas EA Pass:',value= filtro_anual(df, 'Yes', 'No'),border=True)
col2.metric(label='Total apenas Minecraft Pass:',value= filtro_anual(df, 'No', 'Yes'),border=True)

st.header('Adesão de cada modalidade de plano')
sub_mon = (df['Subscription Type'] == 'Monthly').sum()
sub_annual = df['Subscription Type'].value_counts()['Annual']
sub_quart = df['Subscription Type'].value_counts()['Quarterly']
data_chart = {
    'Plano': ['Mensal', 'Quaternal', 'Anual'],
    'Qtd': [sub_mon, sub_quart, sub_annual]
}

# gera gráfico
fig = px.bar(
    data_chart,
    x = 'Plano',
    y = 'Qtd',
    text_auto=True
)
st.plotly_chart(fig, width='stretch')

st.header('Quantidade de planos anuais que optaram ou não pela auto renovação')
st.progress(filtro_planos(df, 'Yes'),text='Sim',width='stretch')
st.progress(filtro_planos(df, 'No'),text='Não',width='stretch')
