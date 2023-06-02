import streamlit as st
import gensim
from gensim import corpora, models
import re
import os
import shutil
import heapq
from utilitaires import send_data_to_api

# Page Accueil
def main():

    st.set_page_config(layout="wide")

    texte = st.text_area("Veuillez saisir le texte")

    if st.button("Envoyer"):
        send_data_to_api(data={"feature": texte})

main()


# bisous bisous
