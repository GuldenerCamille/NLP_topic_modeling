from utilitaires import get_data_from_api, delete_data_via_api
import streamlit as st
import pandas as pd

def data():
    data = get_data_from_api()
    st.write(pd.DataFrame(data, columns=["id", "input", "prediction"]))

    if st.button("supprimer les données"):
        delete_data_via_api()

data()
