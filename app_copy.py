import streamlit as st
import boto3
import dotenv
import lib as georisque_lib
import pandas as pd
import locale
from unidecode import unidecode
import debugpy
import os

# Initialize the bedrock client
bedrock = boto3.client('bedrock')

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')


debugpy.listen(("localhost", 5678))  # Listen for incoming debug connections
debugpy.wait_for_client()  # Wait for debugger to attach before continuing
debugpy.breakpoint()  # Optional: set a breakpoint

dotenv.load_dotenv()

st.set_page_config(layout="wide")  # Permet d'afficher plus d'éléments sur l'écran

StreamlitSession = st.session_state

# Chargement du logo
st.image("LOGO4.png", width=250)

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
    "retrait_gonflement_argile": "Cartes HTML/carte_argiles.html",
    "avalanche": "Cartes HTML/carte_avalanches.html",
    "risque_minier": "Cartes HTML/carte_cavites.html",
    "cyclone": "Cartes HTML/carte_cyclone.html",
    "feu_foret": "Cartes HTML/carte_feu.html",
    "inondation": "Cartes HTML/carte_inondations.html",
    "icpe": "Cartes HTML/carte_installations.html",
    "pollution_sols": "Cartes HTML/carte_soldanger.html",
    "radon": "Cartes HTML/carte_radon.html",
    "canalisations_matieres_dangereuses": "Cartes HTML/carte_rescanal.html",
    "seisme": "Cartes HTML/carte_seisme.html",
    "mouvement_terrain": "Cartes HTML/carte_terrain.html"
}

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_input = st.chat_input("Quelle collectivité locale souhaitez-vous analyser ?")
if chat_input:
    response = prompt_ai(chat_input)["output"]["message"]["content"][0]["toolUse"]["input"]
    st.write("Analyse de la collectivité locale : ", response)
    code_insee = response["code_insee"]
    
    VilleInfo = getInfoVille(code_insee)
    st.write(VilleInfo)
    
    DictRisquesNaturels = VilleInfo['RapportRisqueJson'].risques_naturels.to_dict()
    DictRisquesTechnologiques = VilleInfo['RapportRisqueJson'].risques_technologiques.to_dict()
    
    # Sélection des cartes associées aux risques présents
    selected_maps = [map_files[risk] for risk in DictRisquesNaturels if risk in map_files and DictRisquesNaturels[risk]["present"]]
    selected_maps += [map_files[risk] for risk in DictRisquesTechnologiques if risk in map_files and DictRisquesTechnologiques[risk]["present"]]
    
    # Affichage de la carte associée aux risques (s'il y en a une)
    if selected_maps:
        st.write("Carte des risques identifiés :")
        st.components.v1.iframe(selected_maps[0], height=500)  # Affiche uniquement la première carte trouvée
    
    st.table(DictRisquesNaturels)
    st.table(DictRisquesTechnologiques)
    
    st.write("Fin de l'analyse de la collectivité locale.")