import gradio as gr
import boto3
import json
import time
import os

# Client AWS Bedrock

bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")

def generate_content(prompt):
    # Appel au modèle AWS Bedrock pour générer le contenu
    response = bedrock.invoke_model(
        modelId="mistral.mistral-large-2407-v1:0",  # Remplacer par ton modèle spécifique
        body=json.dumps({"inputText": prompt})
    )

    content = response["body"].read().decode("utf-8")  # Récupérer le contenu généré
    
    # Sauvegarder le contenu dans un fichier (par exemple un fichier texte)
    file_path = "/tmp/generated_document.txt"  # Exemple de chemin où le fichier est enregistré
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    
    return content, file_path  # Retourner le contenu HTML et le chemin du fichier

def process_request_with_loading(prompt):
    # Afficher un message de chargement avant la génération
    time.sleep(2)  # Simule un temps de traitement

    # Processus pour générer le contenu
    result_text, file_path = generate_content(prompt)
    
    # Retourner le texte généré et le chemin du fichier après la génération
    return result_text, file_path  # Utiliser 'return' pour retourner les deux valeurs

# Création de l'interface Gradio avec un design moderne
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown("# 📝 Générateur de Document avec AWS Bedrock")
    gr.Markdown("### Entrez votre prompt ci-dessous pour générer un document")

    with gr.Row():
        prompt_input = gr.Textbox(label="🔹 Entrez votre prompt", placeholder="Décrivez le document souhaité...", lines=3)

    with gr.Row():
        generate_btn = gr.Button("🚀 Générer le document")
    
    output_text = gr.HTML()  # Sortie sous forme de HTML
    output_file = gr.File()  # Fichier pour télécharger le document généré

    # Ajout de la fonction avec génération de contenu
    generate_btn.click(
        fn=process_request_with_loading,
        inputs=prompt_input,
        outputs=[output_text, output_file]
    )

# Lancer l'interface
iface.launch(share=True)
