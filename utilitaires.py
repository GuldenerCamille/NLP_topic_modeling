import gensim
from gensim import corpora, models
import re
import os
import shutil
import mysql.connector
import requests
import heapq
import streamlit as st





# Fonction pour récupérer les données depuis l'API.
def send_data_to_api(data:dict, url="http://modeltopic.azurewebsites.net/data/post"):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return
    # st.success("Données insérées avec succès.")
    return st.error("Erreur lors de l'insertion des données.")

# Fonction pour afficher les données depuis l'API.
def get_data_from_api(url="http://modeltopic.azurewebsites.net/data/get"):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("data")
        return data
    return st.error("Erreur lors de la récupération des données.")

# Fonction pour supprimer les données via l'API.
def delete_data_via_api(url="http://modeltopic.azurewebsites.net/data/delete"):
    response = requests.delete(url)
    if response.status_code == 200:
        print("Les données ont été supprimées avec succès.")
    else:
        print("Erreur lors de la suppression des données.")
