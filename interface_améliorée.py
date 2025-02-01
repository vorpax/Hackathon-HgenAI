import gradio as gr
import boto3
import json
import time

# Client AWS Bedrock
bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")

def generate_content(prompt):
    # Appel au modèle AWS Bedrock pour générer le contenu
    response = bedrock.invoke_model(
        modelId="bedrock-foundation-model-id",  # Remplacer par notre modèle spécifique
        body=json.dumps({"inputText": prompt})
    )

    content = response["body"].read().decode("utf-8")  # Récupérer le contenu généré
    return content  # Retourner le contenu généré (HTML, PDF, etc.)

def process_request_with_loading(prompt):
    # Afficher un message de chargement avant la génération
    yield "⏳ Génération en cours... Patientez, cela prend un instant."
    time.sleep(2)  # Simule un temps de traitement

    # Processus pour générer le contenu
    result = generate_content(prompt)
    
    yield result  # Retourne le contenu généré

# Création de l'interface Gradio avec un design moderne
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown("# 📝 Générateur de Document avec AWS Bedrock")
    gr.Markdown("### Entrez votre prompt ci-dessous pour générer un document")

    with gr.Row():
        prompt_input = gr.Textbox(label="🔹 Entrez votre prompt", placeholder="Décrivez le document souhaité...", lines=3)

    with gr.Row():
        generate_btn = gr.Button("🚀 Générer le document")
    
    output_text = gr.HTML(visible=False)  # Sortie sous forme de HTML
    output_file = gr.File(visible=False)  # Fichier pour télécharger le document généré
    progress = gr.Progress(visible=False)  # Barre de progression

    # Ajout de la fonction avec progression
    generate_btn.click(
        fn=process_request_with_loading,
        inputs=prompt_input,
        outputs=[output_text, output_file, progress]
    )

# Lancer l'interface
iface.launch()
