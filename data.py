from dbconnect.connector import Connection
import streamlit as st


@st.cache_data(ttl=3600)
def get_all_players():
    conn = Connection(password=st.secrets["db"]["password"])
    query = "SELECT DISTINCT(player_id),player,squad,season,squad_number FROM fbref"
    return conn.query(query)
