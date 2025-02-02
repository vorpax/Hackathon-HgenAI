import boto3
import json

# Configurer le client Bedrock
client = boto3.client('bedrock-agent-runtime', region_name='us-west-2')
# # Identifiant du Knowledge Base
# knowledge_base_id = "XBWFQCFXVI"
# model_id = "mistral.mistral-large-2407-v1:0"
# model_arn = "arn:aws:bedrock:model/anthropic.claude-v2"
# session_id = str(uuid.uuid4())
# Identifiants
knowledge_base_id = "XBWFQCFXVI"  # Remplace par ton ID de Knowledge Base
model_arn = "arn:aws:bedrock:us-west-2::foundation-model/mistral.mistral-large-2402-v1:0"  # Remplace par l'ARN correct du modèle
kms_key_arn = "arn:aws:kms:us-west-2:248189928368:key/f1e5827c-133a-4713-b2fa-11d689fe687c"  # Remplace par ton KMS Key ARN
modelId = "mistral.mistral-large-2402-v1:0"



def retrieve_and_generate_info_from_rag(query):
    
    # Appel à l'API de Bedrock
    response = client.retrieve_and_generate(
    input={"text": query},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": knowledge_base_id,
            "modelArn": model_arn,
            "generationConfiguration": {
                "inferenceConfig": {
                    "textInferenceConfig": {
                        "maxTokens": 8192,
                        "stopSequences": ["###"],
                        "temperature": 0.3,
                        "topP": 0.9
                    }
                },
                "promptTemplate": {
                    "textPromptTemplate": "Voici les informations pertinentes trouvées :\n\n$search_results$\n\nRéponds à la question suivante en utilisant ces résultats : {query}"
                }
            }
        }
    },
    sessionConfiguration={
        "kmsKeyArn": kms_key_arn
    },
)

    # Afficher les résultats
    return response["output"]["text"]


def recherche_document(collectivite,risque="tous les risques"):
    schema = {
        "document": {
            "nom": "Nom du document - Nom de la commune",
            "edition": "Année de publication",
            "lien": "URL du document si disponible",
            "organisme_responsable": "Nom de l'organisme ou de la municipalité",
            "contact": {
            "adresse": "Adresse de la mairie/organisme",
            "telephone": "Numéro de contact",
            "email": "Email officiel",
            "site_web": "Site officiel"
            }
        },
        "synthese": {
            "objectif": "Informer les citoyens sur les risques majeurs présents sur le territoire de la commune.",
            "contenu": [
            "Risques naturels et technologiques identifiés",
            "Impact potentiel sur la population et les infrastructures des risques",
            "Consignes de sécurité et actions de prévention pour faire face aux risques",
            ]
        },
        "identification_risques": [
            {
            "type": "Risque_1",
            "description": "Description du risque_1",
            "zones_concernees": ["Zones concernées"],
            "exemples_passes": ["dates à laquelle le risque s'est produit"]
            },
            {
            "type": "Risque_n",
            "description": "Description du risque_n",
            "zones_concernees": ["Zones concernées"],
            "exemples_passes": ["dates à laquelle le risque s'est produit"]
            },
        ],
        "actions_adaptation": {
            "mesures_preventives": ["Mesures préventives mises en place par la municipalité pour faire face à chaque risque individuellement"],
            "mesure_compensatoire" : ["Mesures compensatoires mises en place par la municipalité pour compenser les effets des risques sur la population et les infrastructures"],
            "mesure_autres": ["Autres mesures mises en place par la municipalité pour faire face aux risques et non listé précédemment mais présent dans le document"]
        },
        "niveau_confiance": {
            "pertinence": {
            "note": "note sur 10 de confiance dans le document basé sur la qualité des informations fournies, la date de publication et la source.",
            "commentaire": "Commentaire sur la pertinence des informations fournies."
            },
            "exhaustivite": {
            "note":  "note sur 10 d'exhaustivité du document basé sur la quantité et la variété des informations fournies sur les risques et les mesures de prévention.",
            "commentaire": "Commentaire sur l'exhaustivité des informations fournies."
            },
            "lisibilite": {
            "note": "note sur 10 de lisibilté du document basé le niveau de complexité du document et la présence d'image et de graphique aidant à la lisibilité.",
            "commentaire": "Commentaire sur la lisibilité des informations fournies."
            }
        }
    }
    prompt = f"""Tu es un spécialiste de l'analyse des risques naturels et technologiques. Tu as accès à une base de données contenant des informations sur les risques 
    majeurs présents sur le territoire de la commune de  {collectivite} et les alentours. Dans un premier temps tu dois faire une liste des documents mentionnant {collectivite} et {risque} de la 
    forme [f"titres des documents mentionnant {collectivite} et {risque}"], tu peux ensuite élargir la recherche aux régions et département comportant {collectivite} et mentionnant {risque}. 
    Tu dois ensuite pour chaque document fournir un JSON structuré selon les instructions suivantes :
    
    ### JSON OUTPUT FORMAT: {json.dumps(schema, indent=4)}
    
    ### INSTRUCTIONS:
    - **SEULEMENT** renvoyer la liste des documents et des JSON valide.
    - Compléter par N/A les informations manquantes pour **TOUJOURS** renvoyer un json même s'il manque des données 
    - La reponse est **OBLIGATOIREMENT** enfermé entre `<json>` et `</json>`.
    - Pas d'explication sur pourquoi tu ne peux pas fournir les informations, AUCUN texte supplémentaire.
    - N'invente aucune donnée que tu n'a pas explicitement trouvé dans les documents, complete seulement le JSON par N/A si l'information n'est pas présente et sort obligatoirement un json
    
    ### REPONSE:
    <json>
    """
    sortie_kb = retrieve_and_generate_info_from_rag(prompt)
    print(sortie_kb)
