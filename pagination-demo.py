import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Pagination Demo",
    layout = "wide"
)

@st.experimental_singleton
def read_file(filename):
    return pd.read_csv(f'./data/{filename}', encoding = 'utf-8', delimiter=',')

df = read_file('movies.csv')

st.header("Movie Data Set")

n = 10 #how many entry we'd like to see each page.

#we are creating our page counter value here.
if 'page_counter' not in st.session_state:
    st.session_state['page_counter'] = 0

last_page = len(df)//n


page, __, prev, next, __ = st.columns([1,5,1,1,20]) #it'a little tricky, since streamlit doesn't have a innate center method. you can always use external css to centerize objects.

if prev.button('<'):
    if st.session_state['page_counter'] > 0:
        st.session_state['page_counter'] -= 1

if next.button('>'):
    if st.session_state['page_counter'] < last_page-1:
        st.session_state['page_counter'] += 1

page.button(f'{int(st.session_state["page_counter"])+1}/{last_page}', disabled = True)

st.dataframe(df[st.session_state['page_counter']*n:(st.session_state['page_counter']+1)*n])