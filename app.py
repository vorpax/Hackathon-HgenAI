import streamlit as st
import boto3
import dotenv
import lib as georisque_lib
import pandas as pd
import debugpy 
import locale
from unidecode import unidecode
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

debugpy.trace_this_thread(1)
debugpy.debug_this_thread()
dotenv.load_dotenv()

StreamlitSession = st.session_state

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
                            "nom_collectivité": {
                                "type": "string",
                                "description": "Nom de la collectivité locale à analyser."
                            },
                            "code_postal": {
                                "type": "string",
                                "description": "Code postal de la collectivité locale à analyser."
                            },
                            "code_insee": {
                                "type": "string",
                                "description": "Code INSEE de la collectivité locale à analyser."
                            }
                        },
                        "required": ["nom_collectivité","code_postal","code_insee"]
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

def risqueTech_to_emoji(risks):
    risk_emoji_map_technologique = {
    "icpe": "⚖️",                                # Industries classées pour la protection de l'environnement
    "nucleaire": "☢️",                           # Symbole de radiation pour le nucléaire
    "canalisations_matieres_dangereuses": "🛢️", # Symbole de baril pour les matières dangereuses
    "pollution_sols": "🌱",                      # Symbole de plante pour la pollution des sols
    "rupture_barrage": "🚧",                     # Symbole de travaux pour la rupture de barrage
    "risque_minier": "⛏️",                       # Symbole de pioche pour le risque minier
    }
    return [risk_emoji_map_technologique.get(risk, "❓") for risk in risks]

def risqueNat_to_emoji(risks):
    risk_emoji_map_naturel = {
    "inondation": "🌊",
    "risque_cotier": "🌊",  # On peut utiliser le même emoji pour l'inondation et le risque côtier
    "seisme": "🌍",
    "mouvement_terrain": "🌋",  # Glissement de terrain ou mouvement de terrain
    "recul_trait_cote": "⏱️",  # Pour indiquer le recul (horloge peut symboliser le temps)
    "retrait_gonflement_argile": "📉",  # Symbole de fluctuation pour le retrait-gonflement
    "avalanche": "🏔️",  # Montagne enneigée
    "feu_foret": "🔥",
    "eruption_volcanique": "🌋",
    "cyclone": "🌪️",
    "radon": "☢️",  # Symbole de radiation pour le radon
    }
    return [risk_emoji_map_naturel.get(risk, "❓") for risk in risks]

    

def create_riskNat_dataframe(risks):
    risk_names = list(risks.keys())
    risk_emojis = risqueNat_to_emoji(risk_names)
    risk_readable_name = [risks[risk]["libelle"] for risk in risk_names]
    risk_presence = ["✅" if risks[risk]["present"] else "❌" for risk in risk_names]
    return pd.DataFrame({
        "RiskName" : [ risk_readable_name[i] + " " + risk_emojis[i] for i in range(len(risk_names))],
        "Emoji": risk_emojis,
        "Presence": risk_presence
    })

def create_riskTech_dataframe(risks):
    risk_names = list(risks.keys())
    risk_readable_name = [risks[risk]["libelle"] for risk in risk_names]
    risk_emojis = risqueTech_to_emoji(risk_names)
    risk_presence = ["✅" if risks[risk]["present"] else "❌" for risk in risk_names]
    return pd.DataFrame({
        "RiskName" : [ risk_readable_name[i] + " " + risk_emojis[i] for i in range(len(risk_names))],
        "Emoji": risk_emojis,
        "Presence": risk_presence
    })

session = boto3.Session()
bedrock = session.client(service_name='bedrock-runtime', region_name="us-west-2")

st.title("EcoRisque")

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_input = st.chat_input("Quelle collectivité locale souhaitez-vous analyser ?")
if chat_input:
    response = prompt_ai(chat_input)["output"]["message"]["content"][0]["toolUse"]["input"]
    st.write("Analyse de la collectivité locale : ", response)
    response["code_insee"]
    
    
    VilleInfo = getInfoVille(response["code_insee"])
    st.write(VilleInfo)
    
    

    ListeRisquesNaturels = []
    ListeTestRisques=VilleInfo['RapportRisqueJson'].risques_naturels
    print(ListeTestRisques)
    DictRisquesNaturels= VilleInfo['RapportRisqueJson'].risques_naturels.to_dict()
    for risqueKey in VilleInfo['RapportRisqueJson'].risques_naturels.attribute_map.keys():
        ListeRisquesNaturels.append(DictRisquesNaturels[risqueKey])
    
    ListeRisquesTechnologiques = []
    DictRisquesTechnologiques= VilleInfo['RapportRisqueJson'].risques_technologiques.to_dict()
    for risqueKey in VilleInfo['RapportRisqueJson'].risques_technologiques.attribute_map.keys():
        ListeRisquesNaturels.append(DictRisquesTechnologiques[risqueKey])
    
    # ParsedDate = pd.to_datetime(row['created_at'])
    # locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    # ParsedDate = ParsedDate.strftime("%d %B %Y, %Hh%M").lower()
    # st.caption(ParsedDate) 
    
    
    st.table(create_riskNat_dataframe(DictRisquesNaturels))
    st.table(create_riskTech_dataframe(DictRisquesTechnologiques))
    
   
    
    def format_catnat_dataframe(dict_risques_list):
        # Create DataFrame from list of dictionaries
        df = pd.DataFrame(dict_risques_list)
        
        # Select and rename columns
        df = df[[
            'libelle_risque_jo',
            'date_debut_evt',
            'date_fin_evt',
            'date_publication_jo',
            'code_national_catnat'
        ]].rename(columns={
            'libelle_risque_jo': 'Risque',
            'date_debut_evt': 'Date Événement',
            'date_fin_evt': 'Date Fin Événement',
            'date_publication_jo': 'Date Publication JO',
            'code_national_catnat': 'Code National'
        })
        
        
        # Convert dates
        date_columns = ['Date Événement', 'Date Fin Événement', 'Date Publication JO']
        
        for col in date_columns:
            df[col] = pd.to_datetime(df[col])
        
        # Sort by most recent event
        df = df.sort_values('Date Événement', ascending=False)
        
        # Format dates in French
        
        for col in date_columns:
            df[col] = df[col].dt.strftime("%d %B %Y, %Hh%M").str.lower()
        
        
        return df
    DictCatastrophesNaturelles= VilleInfo['CatastropheNaturelles'].to_dict()
    # Usage:
    st.caption("Liste des 10 dernières catastrophes naturelles")
    FormatedData = format_catnat_dataframe(DictCatastrophesNaturelles["data"])
    
    
    st.dataframe(FormatedData)
    
    
    st.write("Fin de l'analyse de la collectivité locale.")

    
    
