import streamlit as st
import streamlit.components.v1 as components

import boto3
import dotenv
from bs4 import BeautifulSoup
import lib as georisque_lib
import pandas as pd
import locale
from unidecode import unidecode
import debugpy
import os

# Initialize the bedrock client
bedrock = boto3.client('bedrock-runtime', region_name='us-west-2')

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
dotenv.load_dotenv()
cities_coordinates = {
    "Paris": (2.3522, 48.8566),
    "Lyon": (4.8357, 45.7640),
    "Marseille": (5.3698, 43.2965),
    "Toulouse": (1.4442, 43.6047),
    "Bordeaux": (-0.5792, 44.8378),
    "Lille": (3.0573, 50.6292),
    "Nantes": (-1.5536, 47.2184),
    "Strasbourg": (7.7521, 48.5734),
    "Nice": (7.2619, 43.7102),
    "Rennes": (-1.6778, 48.1173),
    "Montpellier": (3.8772, 43.6117),
    "Grenoble": (5.7265, 45.1876),
    "Dijon": (5.0415, 47.3220),
    "Brest": (-4.4871, 48.3904),
    "Le Havre": (0.1077, 49.4944),
    "Reims": (4.0317, 49.2583),
    "Toulon": (5.9290, 43.1242),
    "Amiens": (2.2990, 49.8950),
    "Metz": (6.1757, 49.1193),
    "Clermont-Ferrand": (3.0863, 45.7772),
    "Orléans": (1.9093, 47.9029),
    "Perpignan": (2.8956, 42.6986),
    "Rouen": (1.0993, 49.4432),
    "Saint-Étienne": (4.3872, 45.4397),
    "Nancy": (6.1844, 48.6921),
    "Roubaix": (3.1746, 50.6942),
    "Avignon": (4.8055, 43.9493),
    "Saint-Nazaire": (-2.2060, 47.2735),
    "Poitiers": (0.3404, 46.5802)
}

def initial_lonlat_carte(fichier_html, ville):
    with open(fichier_html, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        # Trouver le script contenant la configuration de la carte
        scripts = soup.find_all("script")

    for script in scripts:
        if "setView" in script.text and ville in cities_coordinates:
            lon,lat = cities_coordinates[ville]
            script.string = script.string.replace(
                "setView([46.010542573717416, -2.3438564735174183], 6)",
                f"setView([{lon}, {lat}], 6)"
            )

    # Sauvegarder le fichier modifié
    with open(fichier_html, "w", encoding="utf-8") as file:
        file.write(str(soup))


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

def plotCarte(map,ville):
    
    #selected_maps = [map_files[risk] for risk in DictRisquesNaturels if risk in map_files and DictRisquesNaturels[risk]["present"]]
    #selected_maps += [map_files[risk] for risk in DictRisquesTechnologiques if risk in map_files and DictRisquesTechnologiques[risk]["present"]]
    
    
    # for map in map_files.keys():
    #     selected_map = map_files[map]
    initial_lonlat_carte(map_files[map], ville)
    CarteHtmlReadFile = open(map_files[map], "r").read()
    st.write(f"Carte des risques {map} identifiés :")
    components.html(CarteHtmlReadFile, height=400)  # Affiche uniquement la première carte trouvée
    
if "messages" not in st.session_state:
    st.session_state.messages = []

chat_input = st.chat_input("Quelle collectivité locale souhaitez-vous analyser ?")
if chat_input:
    response = prompt_ai(chat_input)["output"]["message"]["content"][0]["toolUse"]["input"]
    st.write("Analyse de la collectivité locale : ", response["nom_collectivité"])
    code_insee = response["code_insee"]
    nom_ville = response["nom_collectivité"]
    VilleInfo = getInfoVille(code_insee)
    st.write(VilleInfo)
    
    DictRisquesNaturels = VilleInfo['RapportRisqueJson'].risques_naturels.to_dict()
    DictRisquesTechnologiques = VilleInfo['RapportRisqueJson'].risques_technologiques.to_dict()
    
    # Sélection des cartes associées aux risques présents
    
    # Affichage de la carte associée aux risques (s'il y en a une)
    
    st.table(DictRisquesNaturels)
    st.table(DictRisquesTechnologiques)
    carte_a_afficher = [risque for risque in DictRisquesNaturels if risque in map_files and DictRisquesNaturels[risque]["present"]]
    carte_a_afficher += [risque for risque in DictRisquesTechnologiques if risque in map_files and DictRisquesTechnologiques[risque]["present"]]

    for carte in carte_a_afficher:
        plotCarte(carte, nom_ville)
        
    st.write("Fin de l'analyse de la collectivité locale.")

    

