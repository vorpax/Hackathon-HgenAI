import json
import GeorisqueApi
from GeorisqueApi.rest import ApiException

def get_rapport_risques_json(code_insee):
    api_instance = GeorisqueApi.RapportPDFEtJSONApi()
    try:
        api_response = api_instance.generate_rapport_risque_json(code_insee=code_insee)
        return api_response
    except ApiException as e:
        return {"error": str(e)}

def get_catastrophe_naturelles(code_insee, rayon, latlon):
    api_instance = GeorisqueApi.CATNATApi()
    try:
        api_response = api_instance.recherche_cat_nat(code_insee=code_insee)
        return api_response
    except ApiException as e:
        return {"error": str(e)}

def get_dicrim(code_insee):
    api_instance = GeorisqueApi.DICRIMApi()
    try:
        api_response = api_instance.recherche_risques6(code_insee=code_insee)
        return api_response
    except ApiException as e:
        return {"error": str(e)}

def liste_risques(code_insee):
    api_instance = GeorisqueApi.RisquesApi()
    try:
        api_response = api_instance.recherche_risques4(code_insee=code_insee)
        return api_response
    except ApiException as e:
        return {"error": str(e)}

def get_info_ville(code_insee):
    return {
        "RapportRisqueJson": get_rapport_risques_json(code_insee),
        "DICRIM": get_dicrim(code_insee),
        "ListeRisques": liste_risques(code_insee),
        "CatastropheNaturelles": get_catastrophe_naturelles(code_insee, 10, "46.603354,1.888334")
    }

def lambda_handler(event, context):
    code_insee = event.get('code_insee')
    if not code_insee:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing code_insee parameter')
        }
    
    ville_info = get_info_ville(code_insee)
    
    return {
        'statusCode': 200,
        'body': json.dumps(ville_info)
    }
