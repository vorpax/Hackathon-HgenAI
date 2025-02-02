import requests
import json

# Remplacez par l'URL de votre API Gateway
API_URL = "https://xl0ip6a1k9.execute-api.us-west-2.amazonaws.com/prod"

# Définir les paramètres à envoyer
payload = {
    "input_text": "Analyser ce document",
    "document_s3_uri": "s3://mon-bucket/Document gestions des risques en France/DICRIM communes de France/DICRIM Avignon.pdf"
}

# Définir les headers
headers = {
    "Content-Type": "application/json"
}

# Envoyer la requête POST
response = requests.get(API_URL, headers=headers, data=json.dumps(payload))

# Afficher la réponse
if response.status_code == 200:
    print("Réponse API:", response.json())
else:
    print(f"Erreur {response.status_code}: {response.text}")
