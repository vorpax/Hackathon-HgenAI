import streamlit as st
import boto3
import dotenv
import lib as georisque_lib
import pandas as pd
import debugpy 

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
    
    st.table(pd.DataFrame(ListeRisquesNaturels))
    st.table(pd.DataFrame(ListeRisquesTechnologiques))
    debugpy.breakpoint()
    st.write("Fin de l'analyse de la collectivité locale.")

