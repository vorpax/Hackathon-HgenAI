import streamlit as st
import streamlit.components.v1 as components

import boto3
import dotenv
from bs4 import BeautifulSoup
import lib as georisque_lib
import pandas as pd
import locale
from appel_knowledge_basis import retrieve_info_from_rag
from unidecode import unidecode
import debugpy
import os
from PIL import Image

# Initialize the bedrock client
bedrock = boto3.client('bedrock-runtime', region_name='us-west-2')

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
dotenv.load_dotenv()

StreamlitSession = st.session_state

# Chargement du logo
st.image("./logo/LOGO4.png", width=250)

# Titre

@st.cache_resource
def prompt_ai(text):
    tool_list = [
        {
            "toolSpec": {
                "name": "information_collectivite",
                "description": "Permet d'obtenir des informations sur une collectivité locale.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "nom_collectivité": {"type": "string", "description": "Nom de la collectivité locale à analyser."},
                            "code_postal": {"type": "string", "description": "Code postal de la collectivité locale à analyser."},
                            "code_insee": {"type": "string", "description": "Code INSEE de la collectivité locale à analyser."}
                        },
                        "required": ["nom_collectivité", "code_postal", "code_insee"]
                    }
                },
            }
        }
    ]
    st.session_state.messages.append({"content": [{"text": text}], "role": "user"})
    response = bedrock.converse(
        modelId="mistral.mistral-large-2407-v1:0",
        toolConfig={"tools": tool_list, "toolChoice": {"any": {}}},
        messages=st.session_state.messages,
    )
    return response

@st.cache_resource
def getInfoVille(code_insee):
    return georisque_lib.GetInfoVille(code_insee)

# Association des risques aux cartes correspondantes
map_files = {
    "retrait_gonflement_argile": "Cartes_HTML/carte_argiles.html",
    "avalanche": "Cartes_HTML/carte_avalanches.html",
    "risque_minier": "Cartes_HTML/carte_cavites.html",
    "cyclone": "Cartes_HTML/carte_cyclone.html",
    "feu_foret": "Cartes_HTML/carte_feu.html",
    "inondation": "Cartes_HTML/carte_inondations.html",
    "icpe": "Cartes_HTML/carte_installations.html",
    "pollution_sols": "Cartes_HTML/carte_soldanger.html",
    "radon": "Cartes_HTML/carte_radon.html",
    "canalisations_matieres_dangereuses": "Cartes_HTML/carte_rescanal.html",
    "seisme": "Cartes_HTML/carte_seisme.html",
    "mouvement_terrain": "Cartes_HTML/carte_terrain.html"
}

def load_legend_image(risk_name):
    legend_path = f"Légendes/{risk_name}/risques.png"
    if os.path.exists(legend_path):
        return Image.open(legend_path)
    return None

def plotCarte(map, ville):
    CarteHtmlReadFile = open(map_files[map], "r").read()
    st.write(f"Carte des risques {map} identifiés :")
    components.html(CarteHtmlReadFile, height=400)
    
    # Affichage de la légende correspondante
    legend_image = load_legend_image(map)
    if legend_image:
        st.image(legend_image, caption=f"Légende pour {map}")

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_input = st.chat_input("Quelle collectivité locale souhaitez-vous analyser ?")
if chat_input:
    response = prompt_ai(chat_input)["output"]["message"]["content"][0]["toolUse"]["input"]
    st.session_state.messages.append({"content": [{"text": f"Analyse de la collectivité {response['nom_collectivité']}"}], "role": "assistant"})

    st.write("Analyse de la collectivité locale : ", response["nom_collectivité"])
    code_insee = response["code_insee"]
    nom_ville = response["nom_collectivité"]
    VilleInfo = getInfoVille(code_insee)
    
    DictRisquesNaturels = VilleInfo['RapportRisqueJson'].risques_naturels.to_dict()
    DictRisquesTechnologiques = VilleInfo['RapportRisqueJson'].risques_technologiques.to_dict()
    
    st.table(DictRisquesNaturels)
    st.table(DictRisquesTechnologiques)
    
    carte_a_afficher = [risque for risque in DictRisquesNaturels if risque in map_files and DictRisquesNaturels[risque]["present"]]
    carte_a_afficher += [risque for risque in DictRisquesTechnologiques if risque in map_files and DictRisquesTechnologiques[risque]["present"]]

    for carte in carte_a_afficher:
        plotCarte(carte, nom_ville)
        
    st.write("Fin de l'analyse de la collectivité locale.")
