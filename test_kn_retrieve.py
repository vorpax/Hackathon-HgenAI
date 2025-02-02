import boto3
import json
from gradio_app.ChatbotLib import *

# Clients AWS Bedrock
agent_client = boto3.client('bedrock-agent-runtime', region_name='us-west-2')  # Pour récupérer les documents
model_client = boto3.client('bedrock-runtime', region_name='us-west-2')  # Pour invoquer le modèle LLM

# Identifiants
knowledge_base_id = "XBWFQCFXVI"  # Remplace par ton Knowledge Base ID
model_id = "mistral.mistral-large-2402-v1:0"

def retrieve_from_rag(query):
    """ Récupère des informations depuis la base de connaissances via AWS Bedrock RAG. """
    response = agent_client.retrieve(
        knowledgeBaseId=knowledge_base_id,
        retrievalQuery={"text": query}  # Format correct en dict
    )
    # print(response)
    return response.get("retrievedDocuments", [])

def generate_response(query):
    """ Génère une réponse basée sur les documents récupérés et un modèle LLM. """
    retrieved_docs = retrieve_from_rag(query)

    # Extraction du contenu des documents récupérés
    documents_content = "\n\n".join([doc["content"] for doc in retrieved_docs])
    # print(documents_content)
    # Construire le prompt pour le modèle
    schema = {
        "document": {
            "nom": "string",
            "annee_edition": "int",
            "lien": "string",
            "organisme_responsable": "string",
            "contact": {
            "adresse": "string",
            "telephone": "int",
            "email": "string",
            "site_web": "string"
            }
        },
        "synthese": {
            "objectif": "string",
            "contenu": "list of string"
        },
        "identification_risques": [
            {
            "type_de_risque": "string",
            "description": "string",
            "zones_concernees": "list of string",
            "exemples_passes": "list of int"
            }
        ],
        "actions_adaptation": {
            "mesures_preventives": "list of string",
            "mesure_compensatoire" : "list of string",
        },
        "niveau_confiance": {
            "pertinence": {
            "note": "int",
            "commentaire": "string"
            },
            "exhaustivite": {
            "note": "int",
            "commentaire": "string"
            },
            "lisibilite": {
            "note": "int",
            "commentaire": "string"
            }
        }
    }
    collectivite = "Avignon"
    risque = "risques d'inondation"
    prompt = f"""Tu es un spécialiste de l'analyse des risques naturels et technologiques. Analyse les données présentes dans le fichier texte 
    et renvoie un fichier JSON compléter 
    
    ### JSON OUTPUT FORMAT: {json.dumps(schema, indent=4)}
    ### fichier texte à ANALYSER: {documents_content}
    
    ### INSTRUCTIONS:
    - **ONLY** output valid JSON.
    - The response **MUST** be enclosed between `<json>` and `</json>`.
    - No explanations, no additional text.
    - If you don't have the information you **MUST** replace it by "N/A" and DO NOT create data not present in the document
    
    ### REPONSE:
    <json>
    """

    messages = convert_chat_messages_to_converse_api(chat_with_model(new_text=prompt))
    return messages[-1]["content"][0]["text"]

# print(messages[-1]["content"][0]["text"])

# Exemple d'utilisation
query = """Donne moi toutes les informations importantes du DICRIM Avignon, sur les risques d'inondation à Avignon et les mesures mises en place pour y faire face parmis tous les documents 
concernant Avignon et les risques d'inondation."""

response = generate_response(query)
print(response)
